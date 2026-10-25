
from django.urls import path
from . import views

app_name = "attendance"

urlpatterns = [
    path("", views.attendance_list, name="attendance_list"),
    path("create/", views.attendance_create, name="attendance_create"),
    path("<int:pk>/mark/", views.mark_attendance, name="mark_attendance"),
]
