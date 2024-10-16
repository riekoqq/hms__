from . import views
from django.urls import path

app_name = "staff"

urlpatterns = [
    path(
        "attendance-history/", views.attendance_history_page, name="attendance-history"
    ),
    path("shift-schedule/", views.shift_schedule_page, name="shift-schedule"),
    path("time-in/", views.time_in_page, name="time-in"),
    path("time-out/", views.time_out_page, name="time-out"),
    path("payroll-history/", views.payroll_page, name="payroll-history"),
]
