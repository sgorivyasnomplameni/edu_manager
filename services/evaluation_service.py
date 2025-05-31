class EvaluationService:
    def __init__(self):
        self.__grade_history = {}  # { (student, course): [Grade, ...] }

    def add_grade(self, student, course, grade):
        student.add_grade(course, grade)
        key = (student, course)
        if key not in self.__grade_history:
            self.__grade_history[key] = []
        self.__grade_history[key].append(grade)

    def get_average(self, student):
        return student.get_average()

    def get_grade_history(self, student, course):
        return self.__grade_history.get((student, course), [])

    def calculate_final_grade(self, student, course):
        grades = student._Student__grades.get(course, [])
        if not grades:
            return 0
        return sum(g.value for g in grades) / len(grades)

