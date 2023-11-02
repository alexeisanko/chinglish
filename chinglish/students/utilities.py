import datetime

from chinglish.main.models import Lesson, HomeWorkFile


def get_all_lesson_student(student):
    colors = ['blue', 'green', 'read', 'brown', 'purple', 'yellow', 'black', ]
    lessons = Lesson.objects.filter(visitors__student=student)
    lessons_for_calendar = [
        {'title': lesson.type_lesson.name,
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
         'color': colors[lesson.type_lesson_id],
         'id_event': lesson.id} for
        lesson in lessons]
    return lessons_for_calendar


def get_info_lesson_to_calendar(lesson):
    info_lesson = {'title': lesson.type_lesson.name,
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
                       lesson.time.start_time.minute) + datetime.timedelta(
                       minutes=lesson.type_lesson.duration)).isoformat(),
                   'id_time': lesson.time.id,
                   'teacher': lesson.teacher.get_full_name(),
                   'homework_text': lesson.homework_text}

    homework = [{'file': homework.homework_file.url, 'id': homework.id} for homework in
                HomeWorkFile.objects.filter(lesson=lesson)]

    return {'info_lesson': info_lesson, 'homework': homework}
