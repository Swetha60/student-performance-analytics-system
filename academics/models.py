
from django.db import models


class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(
        max_length=20,
        unique=True,
        blank=True,
    )

    def save(self, *args, **kwargs):
        if not self.code:
            used_codes = set(
                Subject.objects.exclude(pk=self.pk)
                .values_list("code", flat=True)
            )

            number = 1
            while f"SUB{number:03d}" in used_codes:
                number += 1

            self.code = f"SUB{number:03d}"

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.code})"



class Exam(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Assessment(models.Model):
    exam = models.ForeignKey(
        Exam,
        on_delete=models.CASCADE,
        related_name="assessments",
    )
    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        related_name="assessments",
    )
    total_marks = models.PositiveIntegerField(default=100)

    def __str__(self):
        return f"{self.exam.name} - {self.subject.name}"


class Mark(models.Model):
    assessment = models.ForeignKey(
        Assessment,
        on_delete=models.CASCADE,
        related_name="marks",
    )
    student = models.ForeignKey(
        "students.Student",
        on_delete=models.CASCADE,
        related_name="marks",
    )
    marks_obtained = models.FloatField()
    remarks = models.TextField(blank=True)

    class Meta:
        unique_together = ("assessment", "student")

    def __str__(self):
        return f"{self.student} - {self.marks_obtained}"
