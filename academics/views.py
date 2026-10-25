
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import Subject, Exam, Assessment, Mark
from .forms import SubjectForm, ExamForm, AssessmentForm, MarkForm


# ---------------- SUBJECTS ----------------

def subject_list(request):
    subjects = Subject.objects.all()
    return render(
        request,
        "academics/subject_list.html",
        {"subjects": subjects},
    )


def subject_create(request):
    form = SubjectForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Subject created successfully.")
        return redirect("academics:subject_list")

    return render(
        request,
        "academics/form.html",
        {"form": form, "page_title": "Add Subject"},
    )


# ---------------- EXAMS ----------------

def exam_list(request):
    exams = Exam.objects.all()
    return render(
        request,
        "academics/exam_list.html",
        {"exams": exams},
    )


def exam_create(request):
    form = ExamForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Exam created successfully.")
        return redirect("academics:exam_list")

    return render(
        request,
        "academics/form.html",
        {"form": form, "page_title": "Create Exam"},
    )


# ---------------- ASSESSMENTS ----------------

def assessment_list(request):
    assessments = Assessment.objects.select_related(
        "exam", "subject"
    ).all()

    return render(
        request,
        "academics/assessment_list.html",
        {"assessments": assessments},
    )


def assessment_create(request):
    form = AssessmentForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(
            request,
            "Assessment created successfully.",
        )
        return redirect("academics:assessment_list")

    return render(
        request,
        "academics/form.html",
        {"form": form, "page_title": "Create Assessment"},
    )


# ---------------- MARKS ----------------

def mark_list(request):
    marks = Mark.objects.select_related(
        "student",
        "assessment",
        "assessment__exam",
        "assessment__subject",
    ).all()

    return render(
        request,
        "academics/mark_list.html",
        {"marks": marks},
    )


def mark_create(request):
    form = MarkForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(
            request,
            "Student marks saved successfully.",
        )
        return redirect("academics:mark_list")

    return render(
        request,
        "academics/form.html",
        {"form": form, "page_title": "Enter Student Marks"},
    )


def mark_update(request, pk):
    mark = get_object_or_404(Mark, pk=pk)
    form = MarkForm(request.POST or None, instance=mark)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(
            request,
            "Student marks updated successfully.",
        )
        return redirect("academics:mark_list")

    return render(
        request,
        "academics/form.html",
        {"form": form, "page_title": "Edit Student Marks"},
    )


def mark_delete(request, pk):
    mark = get_object_or_404(Mark, pk=pk)

    if request.method == "POST":
        mark.delete()
        messages.success(
            request,
            "Student marks deleted successfully.",
        )
        return redirect("academics:mark_list")

    return render(
        request,
        "academics/mark_confirm_delete.html",
        {"mark": mark},
    )
