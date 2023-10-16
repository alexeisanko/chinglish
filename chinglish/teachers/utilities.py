import datetime

from chinglish.main.models import Lesson, TrialLesson


def get_all_lesson_teacher(teacher):
    colors = ['blue', 'green', 'read', 'brown', 'purple', 'yellow', 'black', ]
    collors_trial = ['pink']
    lessons = Lesson.objects.filter(teacher=teacher)
    trial_lessons = TrialLesson.objects.filter(teacher=teacher)
    lessons_for_calendar = [
        {'title': lesson.name,
         'start': datetime.datetime(
             lesson.date.year,
             lesson.date.month,
             lesson.date.day,
             lesson.time.start_time.hour,
             lesson.time.start_time.minute
         ).isoformat(),
         'end': (datetime.datetime(
             lesson.date.year,
             lesson.date.month,
             lesson.date.day,
             lesson.time.hour,
             lesson.time.minute) + datetime.timedelta(minutes=lesson.type_lesson.duration)).isoformat(),
         'color': colors[lesson.type_lesson_id],
         'id_event': lesson.id} for
        lesson in lessons]

    lessons_for_calendar += [
        {'title': lesson.name,
         'start': datetime.datetime(
             lesson.date.year,
             lesson.date.month,
             lesson.date.day,
             lesson.time.start_time.hour,
             lesson.time.start_time.minute
         ).isoformat(),
         'end': (datetime.datetime(
             lesson.date.year,
             lesson.date.month,
             lesson.date.day,
             lesson.time.start_time.hour,
             lesson.time.start_time.minute) + datetime.timedelta(minutes=lesson.type_lesson.duration)).isoformat(),
         'color': collors_trial,
         'id_event': lesson.id} for
        lesson in trial_lessons]

    return lessons_for_calendar
