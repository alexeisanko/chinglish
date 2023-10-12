import datetime

from chinglish.main.models import TypeLesson, StartTime
from chinglish.teachers.models import Teacher


def get_teacher_for_trial_lesson():
    free_trial = {}
    type_trial_lessons = TypeLesson.objects.filter(available_trial_lesson=True)
    for lesson in type_trial_lessons:
        teachers = Teacher.objects.filter(teacherlesson__type_lesson=lesson)
    return free_trial


def get_free_date_time(teacher_id):
    free_date = {}
    teacher = Teacher.objects.get(id=teacher_id)
    today = datetime.date.today()
    for i in range(14):
        record_date = today + datetime.timedelta(days=1)
        free_times = StartTime.objects.filter(actual=True).exclude(lesson__date=record_date)
        if free_times:
            free_date[record_date] = free_times

