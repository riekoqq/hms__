from .forms import PatientForm, PatientTransferForm, PatientStatusUpdateForm
from .models import Hospital
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def hospital_page(request):
    hospitals = Hospital.objects.all()

    context = {}
    context["hospitals"] = hospitals
    return render(request, "hospital/hospital.html", context)


@login_required
def transfer_page(request):
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
    return render(request, "hospital/manage-patient.html")


@login_required
def add_patient_page(request):
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
