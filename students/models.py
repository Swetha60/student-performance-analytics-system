
from django.db import models


class Classroom(models.Model):
    name = models.CharField(max_length=50)
    section = models.CharField(max_length=10, blank=True)
    academic_year = models.CharField(max_length=20)

    class Meta:
        ordering = ["name", "section"]
        constraints = [
            models.UniqueConstraint(
                fields=["name", "section", "academic_year"],
                name="unique_class_section_year",
            )
        ]

    def __str__(self):
        return f"{self.name} {self.section} ({self.academic_year})".strip()


class Student(models.Model):
    GENDER_CHOICES = [
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Other"),
    ]

    student_id = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True)
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        blank=True,
    )
    date_of_birth = models.DateField(null=True, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    classroom = models.ForeignKey(
        Classroom,
        on_delete=models.PROTECT,
        related_name="students",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["student_id"]

    def __str__(self):
        return f"{self.student_id} - {self.first_name} {self.last_name}".strip()

