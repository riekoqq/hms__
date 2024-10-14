from .forms import TimeInForm, TimeOutForm
from account.models import Attendance
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render
from django.utils import timezone


# Create your views here.
@login_required
def time_in_page(request):

    if request.method == "POST":
        form = TimeInForm(request.POST)
        user_id = None

        if form.is_valid():
            user_id = form.cleaned_data["user_id"]

            user = User.objects.get(pk=user_id)

            attendance = Attendance()
            attendance.user_info = user.user_info
            attendance.date = timezone.now().date()
            attendance.time_in = timezone.now().time()

            attendance.save()

            messages.success(request, "Time in successfully!")
        else:
            messages.error(request, "Time in Error!")
    else:
        form = TimeInForm()

    context = {}
    context["form"] = form

    return render(request, "staff/time-in.html", context)


@login_required
def time_out_page(request):

    if request.method == "POST":
        form = TimeOutForm(request.POST)
        user_id = None

        if form.is_valid():
            user_id = form.cleaned_data["user_id"]
            date = timezone.now().date()

            user = User.objects.get(pk=user_id)

            attendance = Attendance.objects.get(user_info=user.user_info, date=date)
            attendance.time_out = timezone.now().time()

            attendance.save()

            messages.success(request, "Time out successfully!")
        else:
            messages.error(request, "Time out Error!")
    else:
        form = TimeOutForm()

    context = {}
    context["form"] = form

    return render(request, "staff/time-out.html", context)


@login_required
def attendance_history_page(request):
    user = request.user
    user_info = user.user_info
    attendance_records = user_info.attendance_records.all().order_by("-date")

    return render(
        request, "staff/attendance-history.html", {"records": attendance_records}
    )


@login_required
def shift_schedule_page(request):
    user = request.user
    user_info = user.user_info
    shift_schedules = user_info.shift_schedules.all()[0].get_shift_schedule_array()

    return render(request, "staff/shift-schedule.html", {"shift": shift_schedules})
