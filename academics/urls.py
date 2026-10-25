
from django.urls import path
from . import views

app_name = "academics"

urlpatterns = [
    path("subjects/", views.subject_list, name="subject_list"),
    path("subjects/add/", views.subject_create, name="subject_create"),
    path("exams/", views.exam_list, name="exam_list"),
    path("exams/add/", views.exam_create, name="exam_create"),
    path("assessments/", views.assessment_list, name="assessment_list"),
    path("assessments/add/", views.assessment_create, name="assessment_create"),
    path("marks/", views.mark_list, name="mark_list"),
    path("marks/add/", views.mark_create, name="mark_create"),
    path("marks/<int:pk>/edit/", views.mark_update, name="mark_update"),
    path("marks/<int:pk>/delete/", views.mark_delete, name="mark_delete"),
]
