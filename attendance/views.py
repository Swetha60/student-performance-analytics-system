
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import modelformset_factory

from .models import AttendanceSession, AttendanceRecord
from .forms import AttendanceSessionForm, AttendanceRecordForm
from students.models import Student


def attendance_list(request):
    sessions = AttendanceSession.objects.select_related(
        "classroom", "subject"
    ).all()
    return render(
        request,
        "attendance/attendance_list.html",
        {"sessions": sessions},
    )


def attendance_create(request):
    if request.method == "POST":
        form = AttendanceSessionForm(request.POST)
        if form.is_valid():
            session = form.save()
            return redirect("attendance:mark_attendance", pk=session.pk)
    else:
        form = AttendanceSessionForm()

    return render(
        request,
        "attendance/attendance_form.html",
        {"form": form, "page_title": "Create Attendance Session"},
    )


def mark_attendance(request, pk):
    session = get_object_or_404(
        AttendanceSession.objects.select_related("classroom"),
        pk=pk,
    )
    students = Student.objects.filter(
        classroom=session.classroom
    ).order_by("student_id")

    RecordFormSet = modelformset_factory(
        AttendanceRecord,
        form=AttendanceRecordForm,
        extra=0,
    )

    existing_records = AttendanceRecord.objects.filter(session=session)
    existing_by_student = {
        record.student_id: record for record in existing_records
    }

    if request.method == "POST":
        formset = RecordFormSet(
            request.POST,
            queryset=existing_records,
            prefix="attendance",
        )
        if formset.is_valid():
            records = formset.save(commit=False)
            for record in records:
                record.session = session
                record.save()
            formset.save_m2m()

            # Add attendance records for students without an existing record.
            for student in students:
                AttendanceRecord.objects.get_or_create(
                    session=session,
                    student=student,
                    defaults={"status": "P"},
                )

            return redirect("attendance:attendance_list")
    else:
        # Ensure every student has a record for this session.
        for student in students:
            AttendanceRecord.objects.get_or_create(
                session=session,
                student=student,
                defaults={"status": "P"},
            )

        formset = RecordFormSet(
            queryset=AttendanceRecord.objects.filter(session=session),
            prefix="attendance",
        )

    return render(
        request,
        "attendance/mark_attendance.html",
        {"session": session, "students": students, "formset": formset},
    )
