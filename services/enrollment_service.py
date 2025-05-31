class EnrollmentService:
    def __init__(self):
        pass

    def enroll_student_in_course(self, student, course):
        # проверяем требования курса
        for req in course._Course__requirements:
            if req not in student._Student__courses:
                raise Exception("студент не соответствует требованиям")

        # записываем на курс
        course.enroll_student(student)
        student.enroll(course)
