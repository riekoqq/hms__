from .forms import PatientForm
from .models import Hospital
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render


def hospital_page(request):
    hospitals = Hospital.objects.all()

    context = {}
    context["hospitals"] = hospitals
    return render(request, "hospital/hospital.html", context)


def transfer_page(request):
    return render(request, "hospital/transfer.html")


def manage_patient_page(request):
    return render(request, "hospital/manage-patient.html")


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


def admission_discharge_page(request):
    return render(request, "hospital/admission-discharge.html")
