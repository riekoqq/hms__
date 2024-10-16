from hospital.models import Hospital, Patient
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.core.paginator import Paginator
from django.http import HttpResponseForbidden
from django.shortcuts import render


@login_required
def home_page(request):
    user = request.user
    context = {}

    allowed_groups = ["staff", "patient"]

    if not request.user.groups.filter(name__in=allowed_groups).exists():
        return HttpResponseForbidden("You are not authorized to view this page.")

    if user.is_staff:
        hospitals = Hospital.objects.all().order_by("-created_at")
        patients = Patient.objects.all().order_by("-created_at")

        hospital_paginator = Paginator(hospitals, 10)
        patient_paginator = Paginator(patients, 10)

        hospital_page_number = request.GET.get("hospital_page", 1)
        patient_page_number = request.GET.get("patient_page", 1)

        hospital_page = hospital_paginator.get_page(hospital_page_number)
        patient_page = patient_paginator.get_page(patient_page_number)

        number_of_hospitals = hospitals.count()
        number_of_staffs = User.objects.filter(is_staff=True).count()
        number_of_patients = patients.count()

        context["hospital_page"] = hospital_page
        context["patient_page"] = patient_page
        context["number_of_hospitals"] = number_of_hospitals
        context["number_of_staffs"] = number_of_staffs
        context["number_of_patients"] = number_of_patients
    else:
        patient = user.patient_info
        medical_records = patient.medical_records.all()

        context["patient"] = patient
        context["medical_records"] = medical_records

    return render(request, "app/index.html", context)


@login_required
def profile_page(request):
    user = request.user
    context = {}

    allowed_groups = ["staff", "patient"]

    if not request.user.groups.filter(name__in=allowed_groups).exists():
        return HttpResponseForbidden("You are not authorized to view this page.")

    if user.is_staff:
        user_info = user.user_info
        attendance_records = user_info.attendance_records.all().order_by("-date")
        shift_schedules = user_info.shift_schedules.all()[0].get_shift_schedule_array()

        context["records"] = attendance_records
        context["shift"] = shift_schedules
    else:
        patient = user.patient_info
        medical_records = patient.medical_records.all()

        context["patient"] = patient
        context["medical_records"] = medical_records

    return render(request, "app/profile.html", context)
