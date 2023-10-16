import datetime

from chinglish.main.models import TypeLesson, StartTime
from chinglish.teachers.models import Teacher


def get_free_teacher_for_trial_lesson():
    free_teachers, available_type_lesson = set(), {}
    type_trial_lessons = TypeLesson.objects.filter(available_trial_lesson=True)
    for lesson in type_trial_lessons:
        available_teachers = Teacher.objects.filter(teacherlesson__type_lesson=lesson)
        available_type_lesson[lesson.id] = {'name': lesson.name,
                                            'teachers': [(teacher.id, teacher.get_full_name()) for teacher in
                                                         available_teachers]}
        free_teachers.add(*available_teachers)
    free_time_teachers = get_free_date_time(free_teachers)
    return available_type_lesson, free_time_teachers


def get_free_date_time(teachers):
    free_date = {}
    today = datetime.date.today()
    for teacher in teachers:
        free_date[teacher.id] = {'name': teacher.get_full_name(), 'free_time_record': {}}
        for i in range(14):
            record_date = today + datetime.timedelta(days=i)
            free_times = StartTime.objects\
                .filter(actual=True)\
                .exclude(lesson__date=record_date, lesson__teacher=teacher)\
                .exclude(triallesson__date=record_date, triallesson__teacher=teacher)
            if free_times:
                free_date[teacher.id]['free_time_record'][record_date.strftime('%d.%m.%Y')] = [
                    (time.id, time.start_time.strftime('%H:%M')) for time in free_times]
    return free_date
