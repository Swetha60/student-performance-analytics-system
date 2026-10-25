
from django.contrib import admin
from .models import AttendanceSession, AttendanceRecord


@admin.register(AttendanceSession)
class AttendanceSessionAdmin(admin.ModelAdmin):
    list_display = ("date", "classroom", "subject")
    list_filter = ("date", "classroom")


@admin.register(AttendanceRecord)
class AttendanceRecordAdmin(admin.ModelAdmin):
    list_display = ("session", "student", "status")
    list_filter = ("status",)
    search_fields = ("student__student_id", "student__first_name")
