import requests
from copy import deepcopy
import xmltodict as xml
from src.date_util import convert_time, convert_date
import re
from functools import reduce
import datetime
from kanren import run, eq, membero, var, conde, Relation, facts, fact, Var
from collections import OrderedDict


def __clean_key__(key):
	"""
	Private helper function used in clean
	:param key: String, representing a key in a dictionary
	:return: String, representing a cleaned key in a dictionary
	"""
	return str(re.sub("([a-z])([A-Z1-9])", lambda m: m.group(1) + "_" + str(m.group(2)).lower(),
		str(key).replace("@", ""))).lower()


def __clean_requirements__(requirement):
	"""
	Private helper function used in __clean__, handles `@Requirement` key.
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


def __coll_to_tups__(coll):
	"""
	Quick and dirty helper function to turn a python collection into organized tuples. Used in kanren, because lists
	and dictionaries aren't hashable.
	:param coll: A standard python collection (lists, dicts, etc.). Assumes everything other than lists and dicts are
		simply values, and leaves them be.
	:return: The same coll, but made up of completely tuples. If given a dictionary, will return a tuple of the form:
		((key1, val1), (key2, val2), ..., (keyn, valn))
	"""
	return tuple([(k, __coll_to_tups__(v)) for (k, v) in list(coll.items())]) if type(coll) is dict \
		else tuple(map(__coll_to_tups__, coll)) if type(coll) is list \
		else coll


def __tups_to_coll__(tups):
	"""
	Quick and Dirty helper function to turn an organized tuple of other tuples (as given by `__coll_to_tups__`) back into
	whatever data type it previously was. Used to revert data structures used in kanren back to their original form.
	:param tups: a collection comprised of only tuples, meant to emulate possibly nested dictionaries and lists
	:return: the original python collection, whether it was a list, a dictionary, etc. Recursively performs this operation
		on all of the tups's children until it is made up of completely lists and dictionaries.
	"""
	if type(tups) is tuple:
		# to keep track of control codes, a possible edge case for checking maps
		# TODO: make sure control codes arent being fucked
		control_codes = ['(BLANK)', 'CC', 'CS', 'CA', 'RQ', 'R&', 'RQM', 'RM&', 'RQT', 'RT&', 'NQ', 'N&', 'NQM', 'NM&',
						 'MB', 'MP', 'MC', 'ML', 'MA', 'MI', 'MH', 'MN', 'MS', 'MW', 'PAU', 'PCG', 'PDP', 'PIN', 'PUN',
						 'PUA']
		# tups only has other tuples in it
		only_tups = reduce(lambda a, b: a and b, list(map(lambda thing: type(thing) is tuple, tups)))
		# tups only has tuples of length two in it
		all_have_two = reduce(lambda a, b: a and b, list(map(lambda tup: len(tup) == 2, tups))) if only_tups else False
		# all tuples inside of tups have strings as the first element (i.e. they are keys)
		all_have_keys = reduce(lambda a, b: a and b, list(map(lambda tup: type(tup[0]) is str, tups))) if only_tups else False

		# tups was a map
		if only_tups and all_have_two and all_have_keys:
			return {k: __tups_to_coll__(v) for (k, v) in tups}
		# tups was a list
		else:
			return list(map(__tups_to_coll__, tups))
	else:
		return tups


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
	Retrieves all sections related to a specific course from a term.
	:param course_name: String representing the name of the course (i.e. "CS 115")
	:param term: Either a semester object (list of maps representing sections in a semester) or a string representing a term-code.
	:return: All sections in the semester relating to the course.
	"""
	if type(term) is list:
		return list(filter(lambda section: course_name in section["section"], term))
	if type(term) is dict:
		return list(filter(lambda section: course_name in section["section"], term["sections"]))
	if type(term) is str:
		return list(filter(lambda section: course_name in section["section"], semester(term)["sections"]))

def ex_relation_queries():
	"""
	A function to provide example kanren queries in the context of the stevens xml data.
	Not meant to be used in legitimate production, more just a test-bed for relational functions.
	"""
	test_course = __coll_to_tups__(course_sections("2019F", "MA 121"))

	# Query: Which sections in test_course have section co-requisite requirements?
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


def coreq_options(section, term=None):
	"""
	Returns a dictionary representing the options you have to satisfy a single section's co-requisites. See the
	docs in /docs/home.md for specific information about the spec of these dictionaries.
	:param section: The section to query for co-requisites
	:param term: (optional) the term/semester object to use. Defaults to creating a term object from the term code provided
		by `section["term"]`.
	:return: Python dictionary used to describe the options that can satisfy the section's co-requisites.
	"""
	# Set term if not provided
	if not term: term = semester(section["term"])
	elif type(term) is str: term = semester(term)
	result = {}

	for req in section["requirements"]:
		# Activity Co-Requisite
		if "CA" in req["code_list"]:
			# gets the course name from the section name ("MA 123A => MA 123")
			course_name = " ".join(re.findall("([A-Z]{1,3})\s+([0-9]{3})([A-Z]{1,2})?", section["section"])[0][0:2])
			course = __coll_to_tups__(course_sections(term, course_name))
			activity_type = req["code_list"][1]
			# Query: "Which sections satisfy a `section`'s co-requisite?"
			v_section, v_course, v_requirement, v_requirements, v_section_requirement, v_meeting, v_meetings, v_call_number \
				= var(), var(), var(), var(), var(), var(), var(), var()
			kanren_result = run(0, v_section, (eq, v_course, tuple([var() for thing in course])), (eq, v_course, course),
						(membero, v_section, v_course),  							# There is a section `vsection` in `v_course`
						(membero, ("call_number", v_call_number), v_section),		# That has a call number `v_call_number`
						(membero, ("meetings", v_meetings), v_section),  			# and has a list of meetings `v_meetings`
						(membero, v_meeting, v_meetings),  							# which has some meeting `v_meeting`
						(membero, ("activity", activity_type), v_meeting))  		# That is the co-required activity.
			if "activity" not in result.keys():
				result["activity"] = [{
					"type": activity_type,
					"sections": __tups_to_coll__(kanren_result)
				}]
			else:
				result["activity"] += [{
					"type": activity_type,
					"sections": __tups_to_coll__(kanren_result)
				}]
		# Section Co-Requisite
		if "CS" in req["code_list"]:
			# Clean up section coreq name to make it searchable
			parsed_section_coreq_name = re.findall("([A-Z]{1,3})\s+([0-9]{3})([A-Z]{1,2})?", req["code_list"][1])[0]
			section_coreq_name = " ".join(parsed_section_coreq_name[0:2]) + parsed_section_coreq_name[2]

			section_coreq = [s for s in term["sections"] if s["section"] == section_coreq_name][0]
			if "section" not in result.keys():
				result["section"] = [section_coreq]
			else:
				result["section"] += [section_coreq]
		# Course Co-Requisite
		if "CC" in req["code_list"]:
			# [s for s in term["sections"] if "requirements" in s.keys() and ["MC" in r["code_list"] for r in s["requirements"]]]
			pass  # TODO (Probably)
	return result


def are_requirements_satisfied(sections):
	"""
	Returns true of the sections dictionaries described in `sections` satisfy each other's co-requisite requirements
	:param sections: A list of section dictionaries.
	:return: Boolean that represents whether or not the sections in `sections` satisfy each other's requirements.
	"""
	pass # TODO

def generate_schedules(term, courses, num_schedules=0, minimum_free_time=None, maximum_free_time=None, time_spans_when_free=None, time_spans_when_busy=None, maximum_class_duration=None):
	"""
	Generates a list of lists with section dictionaries in them. Each sublist describes a unique schedule given the courses
	that the user wants to take.
	:param term: Either a semester/term dictionary, or a valid term code.
	:param courses: A list of course names that the user wants to sign up for / schedule.
	:param num_schedules: (Optional) The number of schedules to generate. A value of 0 will return all possible schedules.
		Defaults to 0.
	:param minimum_free_time: The smallest amount of time per day that the user wants to leave unscheduled, measured
		in hours. Does not count time inside of time spans set by `time_spans_when_free` and `time_spans_when_busy`.
		Defaults to 0.
	:param maximum_free_time: The largest amount of time per day that the user wants to leave unscheduled, measured
		in hours. Does not count time inside of time spans set by `time_spans_when_free` and `time_spans_when_busy`.
		Defaults to infinity.
	:param time_spans_when_free: A python dictionary describing blocks of time that the user wants to leave unscheduled.
		Acceptable keys include `"monday"`, `"tuesday"`, `"wednesday"`, `"thursday"`, `"friday"`, `"saturday"`, `"weekdays"`,
		and `"all"`. Acceptable values for such dictionaries are lists of tuples with two datetime.time objects in them,
		denoting ranges of time to be left free on specific days. Defaults to {"all": [(dt.time(21, 0), dt.time(8, 0))]}.
	:param time_spans_when_busy: A python dictionary describing blocks of time that the user wants to be scheduled.
		Acceptable keys include `"monday"`, `"tuesday"`, `"wednesday"`, `"thursday"`, `"friday"`, `"saturday"`, `"weekdays"`,
		and `"all"`. Acceptable values for such dictionaries are lists of tuples with two datetime.time objects in them,
		denoting ranges of time to be booked on specific days. Defaults to {"all": [(dt.time(21, 0), dt.time(8, 0))]}.
	:param maximum_class_duration: The maximum acceptable duration for any single class, measured in hours. Defaults to infinity.
	:return: A list of lists with sections in them. Each sublist describes a unique schedule.
	"""
	pass  # TODO


def test():
	"""
	Quick function used to test things
	"""
	# parent = Relation()
	# facts(parent, ("Homer", "Bart"), ("Homer", "Lisa"), ("Abe", "Homer"))
	# facts(parent, ["Marcus", {"name": "God"}])
	# x = var()
	# return run(1, x, parent("Marcus", x))

	with open("data/2019F.xml", "r") as f:
		sem = {"sections": list(map(lambda d: __clean__(d), xml.parse(f.read())["Semester"]["Course"])), "code": "2019F"}
		f.close()
	section = {'section': 'MA 121A', 'title': 'Differential Calculus', 'call_number': '11160', 'min_credit': 2, 'max_credit': 4, 'max_enrollment': 45, 'current_enrollment': 0, 'status': 'open', 'date_span': (datetime.date(2019, 8, 26), datetime.date(2019, 12, 20)), 'instructor_1': 'Staff A', 'term': '2019F', 'meetings': [{'day': ['monday', 'wednesday', 'friday'], 'time_span': (datetime.time(5, 0), datetime.time(5, 50)), 'site': 'Castle Point', 'building': '', 'room': '', 'activity': 'LEC'}], 'requirements': [{'description': 'Activity corequisite required: RCT', 'code_list': ['CA', 'RCT']}, {'description': 'Section corequisite required: D   110A', 'code_list': ['CS', 'D   110A']}, {'description': 'Section corequisite required: MA  122AA', 'code_list': ['CS', 'MA  122AA']}]}

	# Gets a list of tuples containing the term and the call number of courses that satisfy section's coreq requirements
	list(map(lambda s: (s["term"], s["call_number"]), coreq_options(section)))

	# Splits up a Section name into Subject, Course, and Section.
	re.findall("([A-Z]{1,3})\s+([0-9]{3})([A-Z]{1,2})?", "MA 123RC")
	# => [("MA", "123", "RC")]