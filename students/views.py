
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q

from .models import Student, Classroom
from .forms import StudentForm
from academics.models import Subject, Mark
from attendance.models import AttendanceRecord


def dashboard(request):
    context = {
        "total_students": Student.objects.count(),
        "total_classrooms": Classroom.objects.count(),
        "total_subjects": Subject.objects.count(),
        "total_marks": Mark.objects.count(),
        "total_attendance_records": AttendanceRecord.objects.count(),
    }
    return render(request, "home.html", context)


def student_list(request):
    query = request.GET.get("q", "").strip()
    students = Student.objects.select_related("classroom").all()

    if query:
        students = students.filter(
            Q(student_id__icontains=query)
            | Q(first_name__icontains=query)
            | Q(last_name__icontains=query)
            | Q(email__icontains=query)
        )

    return render(
        request,
        "students/student_list.html",
        {"students": students, "query": query},
    )


def student_create(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("students:student_list")
    else:
        form = StudentForm()

    return render(
        request,
        "students/student_form.html",
        {"form": form, "page_title": "Add Student"},
    )


def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect("students:student_list")
    else:
        form = StudentForm(instance=student)

    return render(
        request,
        "students/student_form.html",
        {"form": form, "page_title": "Edit Student"},
    )


def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == "POST":
        student.delete()
        return redirect("students:student_list")

    return render(
        request,
        "students/student_confirm_delete.html",
        {"student": student},
    )
