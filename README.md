# edu_manager

система для управления учебным процессом с соблюдением принципов инкапсуляции.  
позволяет создавать и редактировать курсы, регистрировать студентов и преподавателей, вести оценки и расписание занятий.

---

## возможности

- **курсы**: создание, редактирование, установка требований, ограничение по количеству студентов, управление расписанием  
- **студенты**: регистрация, отчисление, запись на курсы с проверкой требований, отслеживание успеваемости, предупреждения об академических задолженностях  
- **преподаватели**: назначение на курсы, контроль нагрузки и расписания  
- **оценки**: разные типы (экзамены, проекты, домашка), история изменений, автоматический подсчёт средних и итоговых баллов

---

## структура проекта

edu_manager/
├── main.py # точка входа, пример использования
├── models/ # модели: курс, студент, преподаватель, оценка
│ ├── init.py
│ ├── course.py
│ ├── student.py
│ ├── teacher.py
│ └── grade.py
├── services/ # сервисы для записи на курсы и оценивания
│ ├── init.py
│ ├── enrollment_service.py
│ └── evaluation_service.py
└── utils/
└── scheduler.py # планировщик расписания


---

## установка и запуск

1. склонируй репозиторий:
git clone https://github.com/sgorivyasnomplameni/edu_manager.git

2. зайди в папку проекта:
cd edu_manager

3. (опционально) создай и активируй виртуальное окружение:
python3 -m venv venv
source venv/bin/activate

4. запусти пример из `main.py`:
python3 main.py


---

## пример использования (из `main.py`)

```python
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

# создаём преподавателя и назначаем курс
ivan = Teacher("Иван Иванов")
ivan.assign_course(python_course)

# регистрация студентов на курс
enroll = EnrollmentService()
enroll.enroll_student_in_course(sasha, python_course)
enroll.enroll_student_in_course(masha, python_course)

# выставляем оценки
eval_service = EvaluationService()
eval_service.add_grade(sasha, python_course, Grade(85, "экзамен"))
eval_service.add_grade(sasha, python_course, Grade(75, "домашка"))
eval_service.add_grade(masha, python_course, Grade(95, "экзамен"))

# выводим средние баллы
print(f"Средняя оценка Саши: {eval_service.calculate_final_grade(sasha, python_course)}")
print(f"Средняя оценка Маши: {eval_service.calculate_final_grade(masha, python_course)}")

# работа с расписанием
scheduler = Scheduler()
scheduler.add_lesson("Понедельник", "10:00", "12:00", python_course)
print("Расписание на понедельник:")
for start, end, name in scheduler.get_schedule_for_day("Понедельник"):
 print(f" - {start}–{end} | {name}")
```

спасибо за интерес к проекту!
