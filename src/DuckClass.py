
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


d = DuckClass("PEP111", "Mechanics", "Physics")
s = DuckSection("PEP111", "Mechanics", "Physics", "PEP000", "PEP110", "5-8PM", "Ting Lu", "10000", "D")

print(s.section_id)