import requests
from copy import deepcopy
import xmltodict as xml
from src.date_util import convert_time, convert_date
import re
import datetime
from kanren import run, eq, membero, var, conde, Relation, facts, fact, Var
from collections import OrderedDict

def __clean_key__(key):
	"""
	Helper function used in clean
	:param key: String, representing a key in a dictionary
	:return: String, representing a cleaned key in a dictionary
	"""
	return str(re.sub("([a-z])([A-Z1-9])", lambda m: m.group(1) + "_" + str(m.group(2)).lower(),
					  str(key).replace("@", ""))).lower()


def __clean__(section):
	"""
	Private helper function used by `sections`. Goes through an individual dictionary describing a section and
	makes sure the data types, structures, etc described by the raw dictionary are correct and properly pythonic.
	"""
	unsafe_keys = ["Requirement", "@StartDate", "@EndDate", "@Status", "@CurrentEnrollment", "@MaxEnrollment",
				   "@MinCredit", "@MaxCredit", "Meeting"]
	clean_section = {}

	for key in list(section.keys()):
		if key not in unsafe_keys:
			clean_section[__clean_key__(key)] = deepcopy(section[key])
		if key in ["@CurrentEnrollment", "@MaxEnrollment", "@MinCredit", "@MaxCredit"]:
			clean_section[__clean_key__(key)] = int(section[key])
		if key == "@StartDate":
			clean_section["date_span"] = (convert_date(section["@StartDate"]), convert_date(section["@EndDate"]))
		if key == "@Status":
			clean_section["status"] = \
				"Closed" if section[key] == "C" \
					else "open" if section[key] == "O" \
					else "hold" if section[key] == "H" \
					else "cancelled" if section[key] == "X" \
					else "unknown"
		if key == "Meeting":
			if type(section[key]) is dict or type(section[key]) is OrderedDict:
				clean_section["meetings"] = [__clean_meeting__(section[key])]
			elif type(section[key]) is list:
				clean_section["meetings"] = list(map(__clean_meeting__, section[key]))
			else:
				raise Exception(
					"Meetings should either be a dictionary or a list!\nReceived: " + str(type(section[key])))
		if key == "Requirement":
			if type(section[key]) is dict or type(section[key]) is OrderedDict:
				clean_section["requirements"] = [__clean_requirements__(section[key])]
			elif type(section[key]) is list:
				clean_section["requirements"] = list(map(__clean_requirements__, section[key]))
			else:
				raise Exception(
					"Requirements should either be a dictionary or a list!\nReceived: " + str(type(section[key])))

	return clean_section


def __clean_requirements__(requirement):
	"""
	Helper function used in __clean__, handles `@Requirement` key.
	"""
	control_codes = lambda cc: "" if cc == "(BLANK)" \
		else "Course corequisite required" if cc == "CC" \
		else "Section corequisite required" if cc == "CS" \
		else "Activity corequisite required" if cc == "CA" \
		else "Prerequisite course required" if cc == "RQ" \
		else "(cont.) Prerequisite course reqd" if cc == "R&" \
		else "Prereq course reqd w/ min grade" if cc == "RQM" \
		else "(cont.) Prereq reqd w/ min grade" if cc == "RM&" \
		else "Prerequisite test required" if cc == "RQT" \
		else "(cont.) Prerequisite test required" if cc == "RT&" \
		else "Concurrent Prereq course required" if cc == "NQ" \
		else "(cont.) Concur Prereq course reqd" if cc == "N&" \
		else "Concur Prereq reqd w/ min grade" if cc == "NQM" \
		else "(cont.) Concur Prereq w/ min grade" if cc == "NM&" \
		else "By Application Only" if cc == "MB" \
		else "Prerequisite Required" if cc == "MP" \
		else "Corequisite Required" if cc == "MC" \
		else "Lab Fee Required" if cc == "ML" \
		else "Permission of Advisor Required" if cc == "MA" \
		else "Permission of Instructor Required" if cc == "MI" \
		else "Department Head Approval Required" if cc == "MH" \
		else "No Credit Course for Departmental Majors" if cc == "MN" \
		else "Studio course; No general Humanities credit" if cc == "MS" \
		else "Women Only" if cc == "MW" \
		else "Auditors need instructor permission" if cc == "PAU" \
		else "Permission needed from Continuing ED" if cc == "PCG" \
		else "Permission needed from department" if cc == "PDP" \
		else "Permission needed from instructor" if cc == "PIN" \
		else "Undergrads need instructor permission" if cc == "PUN" \
		else "UGs need permission of Dean of UG Academics" if cc == "PUA" \
		else "unknown"
	return {
		"description": control_codes(requirement["@Control"]) + ": " + requirement["@Value1"]
					   + (", " + requirement["@Value2"] if requirement["@Value2"] != "" else ""),
		"code_list": list(filter(lambda s: s != "",
								 [requirement["@Control"], requirement["@Value1"], requirement["@Value2"]])),
	}


def __clean_meeting__(meeting):
	"""
	Private helper function used by `__clean__`, handles `@Meeting` key.
	"""
	unsafe_keys = ["@Day", "@StartTime", "@EndTime"]
	clean_meeting = {}

	for key in list(meeting.keys()):
		if key not in unsafe_keys:
			clean_meeting[__clean_key__(key)] = deepcopy(meeting[key])
		else:
			weekdays = lambda d: \
				"monday" if d == "M" \
					else "tuesday" if d == "T" \
					else "wednesday" if d == "W" \
					else "thursday" if d == "R" \
					else "friday" if d == "F" \
					else "saturday" if d == "S" \
					else "unknown"
			if key == "@Day":
				clean_meeting["day"] = [weekdays(day_code) for day_code in meeting[key]] if "TBA" not in meeting[
					key] else ["TBA"]
			if key == "@StartTime":
				clean_meeting["time_span"] = (convert_time(meeting["@StartTime"]), convert_time(meeting["@EndTime"]))

	return clean_meeting


def available_terms():
	"""
	Returns a list of python dictionaries representing the semesters and terms that the server knows about.
	The two valid keys in each dictionary are `"code"`, which is the term code described,
	and `"description"`, which is a short description of what the term is.
	:return: (list of dict's) A list of terms the server knows about
	"""
	rterms = requests.get("https://web.stevens.edu/scheduler/core/core.php?cmd=terms")

	if rterms.status_code == 200:
		return list(
			map(lambda d: {"code": d["@Code"], "description": d["@Name"]}, xml.parse(rterms.text)["Terms"]["Term"]))
	else:
		raise Exception("Request returned invalid status code " + str(rterms.status_code) + ".")

def semester(term_code):
	"""
	Returns a python dictionary representing the course sections available in a semester.
	See docs/home.md for details about possible keys and values the dictionaries can have.
	:param term_code: Term code representing the semester (i.e. 2019F)
	:return: List of sections representing the course sections available in that semester.
	"""
	if term_code in list(map(lambda d: d["code"], available_terms())):
		rsections = requests.get("https://web.stevens.edu/scheduler/core/core.php?cmd=getxml&term=" + term_code)
		if rsections.status_code == 200:
			data = xml.parse(rsections.text)["Semester"]
			return {
				"semester": data["@Semester"],  # semester code, like 2019F
				"sections": tuple(map(lambda d: __clean__(d), data["Course"]))
			}
		else:
			raise Exception("Request returned invalid status code " + str(rsections.status_code) + ".")
	else:
		raise ValueError("The provided term code was invalid. \nExpected one of the following:" +
						 ", ".join(list(map(lambda d: d["code"], available_terms()))) + "\nReceived: " + term_code)


def course_sections(term, course_name):
	"""
	Retreives all sections related to a specific course from a term.
	:param course_name: String representing the name of the course (i.e. "CS 115")
	:param term: Either a semester object (list of maps representing sections in a semeseter) or a string representing a term-code.
	:return: All sections in the semester relating to the course.
	"""
	if type(term) is list:
		return list(filter(lambda section: course_name in section["section"], term))
	if type(term) is dict:
		return list(filter(lambda section: course_name in section["section"], term["sections"]))
	if type(term) is str:
		return list(filter(lambda section: course_name in section["section"], semester(term)["sections"]))


def section_corequisite_combinations(term, section):
	"""
	Returns a list containing every possible way a section's corequisites can be satisfied, excluding the activity corequisites.
	An individual combination should only contain section call codes, rather than full objects.
	:param term:
	:param section:
	:return:
	"""
	# For section corequisites (like freshman quiz, 2nd half semester MA courses, etc.), it should just be a simple search for the section title.
	#   After, these sections should be checked for requirements, too.

	# - Satisfy Activities coreqs
	# - Satisfy Section coreqs
	# - Satisfy Course coreqs
	# - Filter duplicates

	# To satisfy activity coreqs:
	#   Search for sections related to the course this section is in (MA 121 for MA 121A) that have the satisfy coreqs.
	#   Make sure that these new sections's coreqs are satisfied and that there are no conflicts

	# To satisfy section coreqs:
	#   Add section, and then ensure that that new section's coreqs are satisfied.
	#   If section's coreqs aren't satisfied, find combinations that satisfy them. (Recurse back into section_corequisite_combinations maybe?)
	pass  # TODO


def course_combinations(term, course_names):
	"""
	Returns a list of all possible ways multiple specified courses can be taken together given that all of their requirements are collectively satisfied.
	:param term:
	:param names:
	:return:
	"""
	# this is likely gonna be closest to the main function
	# possibly just make a ton of section_requisite satisfaction functions and map them onto the thing?
	pass  # TODO


def coll_to_tups(coll):
	"""
	Quick and dirty helper function to turn a python collection into organized tuples.
	:param coll:
	:return:
	"""
	if type(coll) is dict:
		result = []
		for key in list(coll.keys()):
			result += [(key, coll_to_tups(coll[key]))] if type(coll) is dict \
				else [(key, tuple(map(coll_to_tups, coll[key])))] if list \
				else [key, coll[key]]
		return tuple(result)
	elif type(coll) is list:
		return tuple(map(coll_to_tups, coll))
	else:
		return coll

def tups_to_coll(tups):
	"""
	Quick and Dirty helper function to turn an organized tuple of other tuples (as given by `coll_to_tups`) back into
	whatever data type it previously was.
	:param tups:
	:return:
	"""
	if type(tups) is tuple:
		# Very likely that it was a map
		if len(tups) == 2:
			pass # TODO: Write a check to see if it's really a map
		elif len(tups) > 2 or len(tups) < 2: # Very likely that is was a list
			pass # TODO
		pass # TODO
	else:
		return tups

def ex_relation_queries():
	"""
	A function to provide example kanren queries in the context of the stevens xml data.
	Not meant to be used in legitimate production, more just a test-bed for relational functions.
	"""
	test_course = coll_to_tups(course_sections("2019F", "MA 121"))

	# Query: Which sections in test_course have section corequisite requirements?
	section, sections, requirement, requirements, section_requirement = var(), var(), var(), var(), var()
	run(0, section, (eq, sections, tuple([var() for thing in test_course])), (eq, sections, test_course),
		(membero, section, sections),  										# There is a section in sections
		(membero, ("requirements", requirements), section),  				# that has requirements
		(membero, requirement, requirements),  								# which has a requirement
		(membero, ("code_list", ("CS", section_requirement)), requirement)) # that is a class requirement requirement

	# Query: "Which sections in test_course are lectures?"
	meeting, meetings = var(), var()
	run(0, section, (eq, sections, tuple([var() for thing in test_course])), (eq, sections, test_course),
		(membero, section, sections),  					# There is a section in sections
		(membero, ("meetings", meetings), section),  	# That has meetings
		(membero, meeting, meetings),  					# that has a meeting
		(membero, ("activity", "LEC"), meeting))  		# that is a lecture.

	# Query: "Which lectures sections in test_course are open?"
	meeting, meetings = var(), var()
	run(0, section, (eq, sections, tuple([var() for thing in test_course])), (eq, sections, test_course),
		(membero, section, sections),  					# There is a section in sections
		(membero, ("status", "open"), section), 		# That is open
		(membero, ("meetings", meetings), section), 	# That has meetings
		(membero, meeting, meetings),  					# that has a meeting
		(membero, ("activity", "LEC"), meeting))  		# that is a lecture.

	# Query: "Which sections satisfy an activity co-requisite?
	pass # TODO

def test():
	# parent = Relation()
	# facts(parent, ("Homer", "Bart"), ("Homer", "Lisa"), ("Abe", "Homer"))
	# facts(parent, ["Marcus", {"name": "God"}])
	# x = var()
	# return run(1, x, parent("Marcus", x))

	with open("data/2019F.xml", "r") as f:
		sem = {"sections": list(map(lambda d: __clean__(d), xml.parse(f.read())["Semester"]["Course"])), "code": "2019F"}
		f.close()

	# The below block of code is an attempt to sketch out what a function might look like if it were trying to
	# retrieve all sections that satisfy an activity corequisite

	# MA 121A from 2019F
	test_section = {'section': 'MA 121A', 'title': 'Differential Calculus', 'call_number': '11160', 'min_credit': 2, 'max_credit': 4, 'max_enrollment': 45, 'current_enrollment': 0, 'status': 'open', 'date_span': (datetime.date(2019, 8, 26), datetime.date(2019, 12, 20)), 'instructor_1': 'Staff A', 'term': '2019F', 'meetings': [{'day': ['monday', 'wednesday', 'friday'], 'time_span': (datetime.time(5, 0), datetime.time(5, 50)), 'site': 'Castle Point', 'building': '', 'room': '', 'activity': 'LEC'}], 'requirements': [{'description': 'Activity corequisite required: RCT', 'code_list': ['CA', 'RCT']}, {'description': 'Section corequisite required: D   110A', 'code_list': ['CS', 'D   110A']}, {'description': 'Section corequisite required: MA  122AA', 'code_list': ['CS', 'MA  122AA']}]}

	for req in test_section["requirements"]:
		if "CA" in req["code_list"]:
			# the course name from the section name ("MA 123A => MA 123")
			course_name = " ".join(re.findall("([A-Z]{2,3})\s+([0-9]{3})([A-Z]{1,2})?", test_section["section"])[0][0:2])
			# TODO: In the line below, replace sem -> test_section["term"] to automate getting the right term obj
			course = coll_to_tups(course_sections(sem, course_name))

			# Query: "Which sections in test_course are lectures?"
			section, sections, requirement, requirements, section_requirement, meeting, meetings = var(), var(), var(), var(), var(), var(), var()
			result = run(0, section, (eq, sections, tuple([var() for thing in course])), (eq, sections, course),
							(membero, section, sections),  							# There is a section in sections
							(membero, ("meetings", meetings), section),  			# That has meetings
							(membero, meeting, meetings),  							# that has a meeting
							(membero, ("activity", req["code_list"][1]), meeting))  # That is the co-required activity.

			# The commented out line below will crash until `tups_to_coll` is implemented
			# return tups_to_coll(result)
			return result
	# Splits up a Section name into Subject, Course, and Section.
	re.findall("([A-Z]{2,3})\s+([0-9]{3})([A-Z]{1,2})?", "MA 123RC")
	# => [("MA", "123", "RC")]