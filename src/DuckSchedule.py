
class DuckClass(object):

    def __init__(self, course_code, title, subject):
        self.__course_code__ = course_code
        self.__title__ = title
        self.__subject__ = subject

    @property
    def course_code(self):
        return self.__course_code__

    @property
    def title(self):
        return self.__title__

    @property
    def subject(self):
        return self.__subject__


class DuckSection(DuckClass):

    def __init__(self, course_code, title, subject, prereqs, coreqs, time, instructor, call_number, section_id):
        super().__init__(course_code, title, subject)
        self.__prereqs__ = prereqs
        self.__coreqs__ = coreqs
        self.__time__ = time
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
    def time(self):
        return self.__time__

    @property
    def instructor(self):
        return self.__instructor__

    @property
    def call_number(self):
        return self.__call_number__

    @property
    def section_id(self):
        return self.__section_id__


class DuckSchedule(object):
    def __init__(self, name, enrolled_classes, no_class_hours):
        self.__name__ = name
        self.__enrolled_classes__ = enrolled_classes
        self.__no_class_hours__ = no_class_hours # TODO: rename
        self.__enrolled_sections__ = self.__resolve_sechedule__()

    @property
    def name(self):
        return self.__name__

    @property
    def enrolled_classes(self):
        return self.__enrolled_classes__

    @property
    def no_class_hours(self):
        return self.__no_class_hours__

    @property
    def enrolled_sections(self):
        return self.__enrolled_sections__

    def __resolve_sechedule__(self):
        """
        Private Helper function responsible for finding all the sections given the
        classes in `enrolled_classes`, while also avoiding the times in `no_class_hours`.
        Returns a list of `DuckSection` objects representing the best possible "class loadout"
        """
        pass # TODO: implement


d = DuckClass("PEP111", "Mechanics", "Physics")
s = DuckSection("PEP111", "Mechanics", "Physics", "PEP000", "PEP110", "5-8PM", "Ting Lu", "10000", "D")

print(s.section_id)
