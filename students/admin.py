
from django.contrib import admin
from .models import Classroom, Student


@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    list_display = ("name", "section", "academic_year")
    search_fields = ("name", "section", "academic_year")
    list_filter = ("academic_year",)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        "student_id",
        "first_name",
        "last_name",
        "classroom",
        "email",
    )
    search_fields = ("student_id", "first_name", "last_name", "email")
    list_filter = ("classroom", "gender")
