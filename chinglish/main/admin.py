from django.contrib import admin

from chinglish.main.models import TypeLesson, TrialLesson, StartTime, Lesson, HomeWorkFile, Visitors

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


@admin.register(StartTime)
class StartTimeAdmin(admin.ModelAdmin):
    list_display = ['start_time']


class HomeWorkFileAdmin(admin.TabularInline):
    model = HomeWorkFile
    list_display = ['homework_file']


class StudentLessonAdmin(admin.TabularInline):
    model = Visitors
    list_display = ['student']


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    inlines = [
        HomeWorkFileAdmin,
        StudentLessonAdmin
    ]
    fieldsets = (
        ('Занятие', {"fields": ("teacher", "type_lesson", "date", "time")}),

    )
    list_display = ["type_lesson", "teacher", "date", "time"]
    search_fields = ["teacher"]
