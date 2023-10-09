from django.contrib import admin

from chinglish.main.models import TypeLesson, TrialLesson


@admin.register(TypeLesson)
class TypeLessonAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Основная информация', {"fields": ("name", "duration", "cost")}),
        ("Свойства", {"fields": (
            "is_group_lesson",
            "available_trial_lesson",
            ),
        },
         ),
        ("Прочее", {"fields": ("description",)}),
    )
    list_display = ["name", "is_group_lesson", "duration", "cost", "available_trial_lesson", "description"]
    search_fields = ["name"]


@admin.register(TrialLesson)
class TrialLessonAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Занятие', {"fields": ("teacher", "type_lesson", "date", "time")}),
        ("Ученик", {"fields": (
            "name",
            "age",
            "classroom",
            "phone"
            ),
        },
         ),
    )
    list_display = ["type_lesson", "teacher", "name", "date", "time", "age", "phone", "classroom"]
    search_fields = ["name"]
