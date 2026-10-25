
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("students.urls")),
    path("attendance/", include("attendance.urls")),
    path("academics/", include("academics.urls")),
    path("analytics/", include("analytics.urls")),
]
