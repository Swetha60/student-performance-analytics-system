
from django.db import models


class AttendanceSession(models.Model):
    classroom = models.ForeignKey(
        "students.Classroom",
        on_delete=models.CASCADE,
        related_name="attendance_sessions",
    )
    subject = models.ForeignKey(
        "academics.Subject",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="attendance_sessions",
    )
    date = models.DateField()
    topic = models.CharField(max_length=200, blank=True)

    class Meta:
        ordering = ["-date"]
        constraints = [
            models.UniqueConstraint(
                fields=["classroom", "subject", "date"],
                name="unique_attendance_session",
            )
        ]

    def __str__(self):
        return f"{self.classroom} - {self.date}"


class AttendanceRecord(models.Model):
    STATUS_CHOICES = [
        ("P", "Present"),
        ("A", "Absent"),
        ("L", "Late"),
        ("E", "Excused"),
    ]

    session = models.ForeignKey(
        AttendanceSession,
        on_delete=models.CASCADE,
        related_name="records",
    )
    student = models.ForeignKey(
        "students.Student",
        on_delete=models.CASCADE,
        related_name="attendance_records",
    )
    status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        default="P",
    )
    remarks = models.CharField(max_length=200, blank=True)

    class Meta:
        ordering = ["student__student_id"]
        constraints = [
            models.UniqueConstraint(
                fields=["session", "student"],
                name="unique_student_attendance_per_session",
            )
        ]

    def __str__(self):
        return f"{self.student} - {self.get_status_display()}"
