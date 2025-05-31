from models.course import Course
from models.student import Student
from models.teacher import Teacher
from models.grade import Grade
from services.enrollment_service import EnrollmentService
from services.evaluation_service import EvaluationService
from utils.scheduler import Scheduler

# создаём курс
python_course = Course("Python для начинающих", requirements=[], max_students=2)

# создаём студентов
sasha = Student("Саша")
masha = Student("Маша")
petya = Student("Петя")  # для проверки ограничения по количеству

# создаём преподавателя и назначаем его на курс
ivan = Teacher("Иван Иванов")
ivan.assign_course(python_course)

# регистрируем студентов
enroll = EnrollmentService()
enroll.enroll_student_in_course(sasha, python_course)
enroll.enroll_student_in_course(masha, python_course)

try:
    enroll.enroll_student_in_course(petya, python_course)
except Exception as e:
    print(f"[!] не удалось записать Петю: {e}")

# выставляем оценки
eval_service = EvaluationService()
eval_service.add_grade(sasha, python_course, Grade(85, "экзамен"))
eval_service.add_grade(sasha, python_course, Grade(75, "домашка"))
eval_service.add_grade(masha, python_course, Grade(95, "экзамен"))

# финальные баллы
print(f"\n📊 средняя оценка Саши: {eval_service.calculate_final_grade(sasha, python_course)}")
print(f"📊 средняя оценка Маши: {eval_service.calculate_final_grade(masha, python_course)}")

# история оценок
print(f"\n📜 история оценок Саши: {eval_service.get_grade_history(sasha, python_course)}")
print(f"📜 история оценок Маши: {eval_service.get_grade_history(masha, python_course)}")

# создаём расписание
scheduler = Scheduler()
scheduler.add_lesson("Понедельник", "10:00", "12:00", python_course)

print("\n📅 расписание на понедельник:")
for start, end, name in scheduler.get_schedule_for_day("Понедельник"):
    print(f" - {start}–{end} | {name}")

# проверим конфликт времени
try:
    scheduler.add_lesson("Понедельник", "11:00", "13:00", python_course)
except Exception as e:
    print(f"[!] не добавлено занятие: {e}")
