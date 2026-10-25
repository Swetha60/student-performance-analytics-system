
from django.shortcuts import render
from students.models import Student
from academics.models import Mark


def performance_dashboard(request):
    students = Student.objects.all().prefetch_related(
        "marks__assessment"
    )

    performance_data = []

    for student in students:
        marks = list(student.marks.all())

        total_obtained = sum(
            mark.marks_obtained for mark in marks
        )
        total_possible = sum(
            mark.assessment.total_marks for mark in marks
            if mark.assessment.total_marks > 0
        )

        # Only include marks with a valid maximum.
        valid_marks = [
            mark for mark in marks
            if mark.assessment.total_marks > 0
        ]

        total_obtained = sum(
            mark.marks_obtained for mark in valid_marks
        )

        percentage = (
            total_obtained / total_possible * 100
            if total_possible > 0 else None
        )

        if percentage is None:
            level = "No marks"
        elif percentage >= 75:
            level = "Excellent"
        elif percentage >= 60:
            level = "Good"
        elif percentage >= 40:
            level = "Average"
        else:
            level = "Needs Improvement"

        performance_data.append({
            "student": student,
            "marks_count": len(valid_marks),
            "total_obtained": round(total_obtained, 2),
            "total_possible": total_possible,
            "percentage": (
                round(percentage, 2)
                if percentage is not None else None
            ),
            "level": level,
        })

    performance_data.sort(
        key=lambda item: (
            item["percentage"] is not None,
            item["percentage"] or 0
        ),
        reverse=True,
    )

    scored_students = [
        item for item in performance_data
        if item["percentage"] is not None
    ]

    overall_average = (
        sum(item["percentage"] for item in scored_students)
        / len(scored_students)
        if scored_students else 0
    )

    context = {
        "performance_data": performance_data,
        "total_students": students.count(),
        "students_with_marks": len(scored_students),
        "overall_average": round(overall_average, 2),
        "top_students": scored_students[:5],
        "chart_labels": [
            item["student"].student_id
            for item in scored_students
        ],
        "chart_values": [
            item["percentage"]
            for item in scored_students
        ],
    }

    return render(
        request,
        "analytics/performance_dashboard.html",
        context,
    )
