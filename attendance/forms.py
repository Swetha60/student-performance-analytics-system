
from django import forms
from .models import AttendanceSession, AttendanceRecord


class AttendanceSessionForm(forms.ModelForm):
    class Meta:
        model = AttendanceSession
        fields = ["classroom", "subject", "date", "topic"]
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
        }


class AttendanceRecordForm(forms.ModelForm):
    class Meta:
        model = AttendanceRecord
        fields = ["status", "remarks"]
