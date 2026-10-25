
from django import forms
from .models import Subject, Exam, Assessment, Mark



class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ["name"]



class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = ["name", "date", "description"]
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
        }


class AssessmentForm(forms.ModelForm):
    class Meta:
        model = Assessment
        fields = ["exam", "subject", "total_marks"]


class MarkForm(forms.ModelForm):
    class Meta:
        model = Mark
        fields = ["assessment", "student", "marks_obtained", "remarks"]
        widgets = {
            "marks_obtained": forms.NumberInput(
                attrs={"min": "0", "step": "0.01"}
            ),
        }

    def clean_marks_obtained(self):
        marks = self.cleaned_data["marks_obtained"]
        assessment = self.cleaned_data.get("assessment")

        if marks < 0:
            raise forms.ValidationError("Marks cannot be negative.")

        if assessment and marks > assessment.total_marks:
            raise forms.ValidationError(
                f"Marks cannot exceed {assessment.total_marks}."
            )

        return marks
