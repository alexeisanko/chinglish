from chinglish.main.models import TypeLesson


def get_free_trial_lesson():
    free_trial = {}
    type_trial_lessons = TypeLesson.objects.filter(available_trial_lesson=True)
    for lesson in type_trial_lessons:
        pass

