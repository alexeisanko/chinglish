import datetime

from chinglish.main.models import Lesson, TrialLesson, TypeLesson, StartTime, HomeWorkFile
from chinglish.students.models import Student
from chinglish.teachers.models import Teacher


def get_all_lesson_teacher(teacher):
    colors = ['blue', 'green', 'read', 'brown', 'purple', 'yellow', 'black', ]
    collors_trial = ['pink']
    lessons = Lesson.objects.filter(teacher=teacher)
    trial_lessons = TrialLesson.objects.filter(teacher=teacher)
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

    lessons_for_calendar += [
        {'title': 'Пробное занятие',
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


def get_available_type_lesson(teacher):
    type_lessons = [{
        'id': type_lessons.id,
        'type': type_lessons.name,
    } for type_lessons in TypeLesson.objects.filter(teacherlesson__teacher=teacher)]
    return type_lessons


def free_time_to_date(date: str, teacher):
    date = datetime.datetime.strptime(date, '%Y-%m-%d')
    free_time = StartTime.objects \
        .exclude(lesson__teacher=teacher, lesson__date=date) \
        .exclude(triallesson__teacher=teacher, triallesson__date=date)
    return [{'time': x.start_time, 'id': x.id} for x in free_time]


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
                   'id_event': lesson.id,
                   'id_time': lesson.time.id,
                   'homework_text': lesson.homework_text}
    students = [{'name': student.get_full_name(), 'id': student.id} for student in
                Student.objects.filter(visitors__lesson=lesson)]
    homework = [{'file': homework.homework_file.url, 'id': homework.id} for homework in
                HomeWorkFile.objects.filter(lesson=lesson)]

    return {'info_lesson': info_lesson, 'students': students, 'homework': homework}
