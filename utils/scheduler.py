from datetime import datetime

class Scheduler:
    def __init__(self):
        self.__schedule = {}  # {day: [(start, end, course)]}

    def add_lesson(self, day, start_time, end_time, course):
        if day not in self.__schedule:
            self.__schedule[day] = []

        new_start = self.__str_to_time(start_time)
        new_end = self.__str_to_time(end_time)

        for start, end, existing_course in self.__schedule[day]:
            if self.__overlaps(new_start, new_end, start, end):
                raise Exception(f"конфликт с курсом: {existing_course.get_title()} в {start_time}–{end_time}")

        self.__schedule[day].append((new_start, new_end, course))

    def get_schedule_for_day(self, day):
        if day not in self.__schedule:
            return []
        return [(s.strftime('%H:%M'), e.strftime('%H:%M'), c.get_title()) for s, e, c in self.__schedule[day]]

    def __str_to_time(self, t):
        return datetime.strptime(t, "%H:%M").time()

    def __overlaps(self, start1, end1, start2, end2):
        return max(start1, start2) < min(end1, end2)
