
from django.contrib import admin
from .models import Subject, Exam, Assessment, Mark


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ("name", "code")
    search_fields = ("name", "code")


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ("name", "date")
    search_fields = ("name",)
    list_filter = ("date",)


@admin.register(Assessment)
class AssessmentAdmin(admin.ModelAdmin):
    list_display = ("exam", "subject", "total_marks")
    list_filter = ("exam", "subject")


@admin.register(Mark)
class MarkAdmin(admin.ModelAdmin):
    list_display = ("student", "assessment", "marks_obtained")
    search_fields = ("student__student_id", "student__first_name")
