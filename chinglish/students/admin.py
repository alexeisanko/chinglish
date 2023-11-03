from django.contrib import admin

from chinglish.students.models import Student


@admin.register(Student)
class TeacherAdmin(admin.ModelAdmin):

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
    list_display = [Student.get_full_name, "phone", "birthday"]
