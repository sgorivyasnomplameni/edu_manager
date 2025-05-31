class Teacher:
    def __init__(self, name):
        self.__name = name
        self.__courses = []

    def assign_course(self, course):
        self.__courses.append(course)

    def get_courses(self):
        return self.__courses
