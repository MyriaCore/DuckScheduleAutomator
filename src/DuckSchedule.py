class DuckSchedule(object):
    def __init__(self, name, enrolled_classes, no_class_hours):
        """
        Constructor for a `DuckSchedule` object, representing the current ideal schedule.
        `name` is a string representing the "name" of the scheduler
        `enrolled_classes` is a list of `DuckClass` objects representing the classes that the schedule needs
        `no_class_hours` is (something???) representing the times that the schedule should put classes in (early in the morning for example)
        Returns a `DuckSchedule` object.
        """
        self.__name__ = name
        self.__enrolled_classes__ = enrolled_classes
        self.__no_class_hours__ = no_class_hours # TODO: rename
        self.__enrolled_sections__ = self.__resolve_sechedule__()

    @property
    def name(self):
        """A string representing the name of the schedule"""
        return self.__name__

    @property
    def enrolled_classes(self):
        """
        A list of `DuckClass` object representing the classes that
        need to be enrolled in.
        """
        return self.__enrolled_classes__

    @property
    def no_class_hours(self):
        """
        A (???) representing the times classes shouldn't be scheduled during
        (like early in the morning, late at night, or during lunch for example)
        """
        return self.__no_class_hours__

    @property
    def enrolled_sections(self):
        """
        A list of `DuckSections` representing the sections to enroll in to create
        the most ideal schedule.
        """
        return self.__enrolled_sections__

    def __resolve_sechedule__(self):
        """
        Private Helper function responsible for finding all the sections given the
        classes in `enrolled_classes`, while also avoiding the times in `no_class_hours`.
        Returns a list of `DuckSection` objects representing the best possible "class loadout"
        """
        pass # TODO: implement

class DuckClass(object):

    def __init__(self, course_code, title, subject):
        """
        Constructor for the `DuckClass` object, representing a class offered by Stevens.
        `course_code` is the shortened name of the course (PEP111 for example)
        `title` is the human readable name of the curse (Mechanics for example)
        `subject` is the subject of the course (Environmental Sciences for example)
        """
        self.__course_code__ = course_code
        self.__title__ = title
        self.__subject__ = subject

    @property
    def course_code(self):
        """A string representing the shortened name of the course (PEP111 for example)"""
        return self.__course_code__

    @property
    def title(self):
        """A string representing the human readable name of the curse (Mechanics for example)"""
        return self.__title__

    @property
    def subject(self):
        """A string representing the subject of the course (Environmental Sciences for example)"""
        return self.__subject__


class DuckSection(DuckClass):

    def __init__(self, course_code, title, subject, prereqs, coreqs, term, days_time_location, instructor, call_number, section_id):
        """
        Constructor for a `DuckSection` object, representing a section for a specific `DuckClass`.
        `course_code`
        `title`
        `subject`
        `prereqs`
        `coreqs`
        `term`
        `days_time_location`
        `instructor`
        `call_number`
        `section_id`
        """
        super().__init__(course_code, title, subject)
        self.__prereqs__ = prereqs
        self.__coreqs__ = coreqs
        self.__term__ = term
        self.__days_time_location__ = days_time_location
        self.__instructor__ = instructor
        self.__call_number__ = call_number
        self.__section_id__ = section_id

    @property
    def prereqs(self):
        return self.__prereqs__

    @property
    def coreqs(self):
        return self.__coreqs__

    @property
    def term(self):
        return self.__term__

    @property
    def days_time_location(self):
        return self.__days_time_location__

    @property
    def instructor(self):
        return self.__instructor__

    @property
    def call_number(self):
        return self.__call_number__

    @property
    def section_id(self):
        return self.__section_id__

class DuckTerm(object):
    def __init__(self, name):
        """
        Constructor for a `DuckTerm` object, representing a specific term,
        and all of the sections in it.
        `name` is the term code (2019S for example).
        """
        self.__name__ = name
        self.__sections__ = self.__get_sections__()

    def name(self):
        return self.__name__

    def sections(self):
        return self.__sections__

    def __get_sections__(self):
        """
        Helper function to get the sections for the term as a list of
        `DuckSection`'s.
        """
        pass # TODO: implement

    # TODO: functions to query the term, like get_sections_by_name, or get_sections_by_subject, etc.
