class Course:
    def __init__(self, title, requirements=None, max_students=30):
        self.__title = title
        self.__requirements = requirements or []
        self.__max_students = max_students
        self.__students = []
        self.__schedule = []

    def get_title(self):
        return self.__title

    def add_requirement(self, requirement):
        self.__requirements.append(requirement)

    def enroll_student(self, student):
        if len(self.__students) >= self.__max_students:
            raise Exception("превышен лимит студентов")
        self.__students.append(student)

    def set_schedule(self, schedule):
        self.__schedule = schedule

    def get_schedule(self):
        return self.__schedule

    def get_students(self):
        return self.__students