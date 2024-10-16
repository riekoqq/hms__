from .forms import (
    MedicalRecordForm,
    PatientForm,
    PatientTransferForm,
    PatientStatusUpdateForm,
)
from .models import Hospital, Patient
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import render


@login_required
def hospital_page(request):

    allowed_groups = ["staff"]

    if not request.user.groups.filter(name__in=allowed_groups).exists():
        return HttpResponseForbidden("You are not authorized to view this page.")

    hospitals = Hospital.objects.all()

    context = {}
    context["hospitals"] = hospitals
    return render(request, "hospital/hospital.html", context)


@login_required
def hospital_detail_page(request, hospital_id):

    allowed_groups = ["staff"]

    if not request.user.groups.filter(name__in=allowed_groups).exists():
        return HttpResponseForbidden("You are not authorized to view this page.")

    hospital = Hospital.objects.get(pk=hospital_id)

    context = {}
    context["hospital"] = hospital
    context["patients"] = hospital.patients.all().order_by("-created_at")
    return render(request, "hospital/hospital-detail.html", context)


@login_required
def transfer_page(request):

    allowed_groups = ["staff"]

    if not request.user.groups.filter(name__in=allowed_groups).exists():
        return HttpResponseForbidden("You are not authorized to view this page.")

    if request.method == "POST":
        form = PatientTransferForm(request.POST)
        if form.is_valid():
            patient = form.cleaned_data["patient"]
            hospital = form.cleaned_data["hospital"]
            patient.hospital = hospital
            patient.save()
            messages.success(
                request,
                f"Patient {patient.first_name} {patient.last_name} transferred successfully to {hospital.name}!",
            )
        else:
            messages.error(request, "There was an error processing the transfer.")
    else:
        form = PatientTransferForm()

    context = {}
    context["form"] = form
    return render(request, "hospital/transfer.html", context)


@login_required
def manage_patient_page(request):

    allowed_groups = ["staff"]

    if not request.user.groups.filter(name__in=allowed_groups).exists():
        return HttpResponseForbidden("You are not authorized to view this page.")

    return render(request, "hospital/manage-patient.html")


@login_required
def patient_detail_page(request, patient_id):

    allowed_groups = ["staff"]

    if not request.user.groups.filter(name__in=allowed_groups).exists():
        return HttpResponseForbidden("You are not authorized to view this page.")

    patient = Patient.objects.get(pk=patient_id)
    medical_records = patient.medical_records.all()

    print("patient: ", patient)
    print("medical records: ", medical_records)

    context = {}
    context["patient"] = patient
    context["medical_records"] = medical_records
    return render(request, "hospital/patient-detail.html", context)


@login_required
def add_patient_page(request):

    allowed_groups = ["staff"]

    if not request.user.groups.filter(name__in=allowed_groups).exists():
        return HttpResponseForbidden("You are not authorized to view this page.")

    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Patient successfully created!")
        else:
            messages.error(
                request,
                "There was an error creating the patient. Please check the form.",
            )
    else:
        form = PatientForm()

    context = {}
    context["form"] = form
    return render(request, "hospital/add-patient.html", context)


@login_required
def admission_discharge_page(request):

    allowed_groups = ["staff"]

    if not request.user.groups.filter(name__in=allowed_groups).exists():
        return HttpResponseForbidden("You are not authorized to view this page.")

    if request.method == "POST":
        form = PatientStatusUpdateForm(request.POST)
        if form.is_valid():
            patient = form.cleaned_data["patient"]
            patient.status = form.cleaned_data["status"]
            patient.save()
            messages.success(
                request,
                f"Patient {patient.first_name} {patient.last_name}'s status updated to {patient.get_status_display()} successfully!",
            )
        else:
            messages.error(request, "There was an error updating the status.")
    else:
        form = PatientStatusUpdateForm()

    return render(request, "hospital/admission-discharge.html", {"form": form})


@login_required
def add_medical_record_page(request):

    allowed_groups = ["staff"]

    if not request.user.groups.filter(name__in=allowed_groups).exists():
        return HttpResponseForbidden("You are not authorized to view this page.")

    if request.method == "POST":
        form = MedicalRecordForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Medical record created successfully!")
        else:
            messages.error(
                request,
                "There was an error creating the medical record. Please try again.",
            )
    else:
        form = MedicalRecordForm()

    return render(request, "hospital/add-medical-record.html", {"form": form})
