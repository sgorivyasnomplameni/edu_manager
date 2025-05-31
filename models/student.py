class Student:
    def __init__(self, name):
        self.__name = name
        self.__courses = []
        self.__grades = {}
        self.__warnings = 0

    def enroll(self, course):
        self.__courses.append(course)

    def add_grade(self, course, grade):
        if course not in self.__grades:
            self.__grades[course] = []
        self.__grades[course].append(grade)

    def get_average(self):
        total, count = 0, 0
        for grades in self.__grades.values():
            total += sum(grades)
            count += len(grades)
        return total / count if count > 0 else 0

    def add_warning(self):
        self.__warnings += 1

    def get_warnings(self):
        return self.__warnings
