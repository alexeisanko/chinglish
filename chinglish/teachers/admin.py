from django.contrib import admin

from chinglish.teachers.models import Teacher, TeacherLesson


class TeacherLessonAdmin(admin.TabularInline):
    model = TeacherLesson
    list_display = ['type_lesson']


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    inlines = [
        TeacherLessonAdmin
    ]
    fieldsets = (
        ('Учитель', {"fields": ("last_name", "first_name", "second_name")}),
        ("Личная информация", {"fields": (
            "phone",
            "birthday",
            'photo',
            ),
        },
         ),
    )
    list_display = [Teacher.get_full_name, "phone", "birthday"]



