from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def home_page(request):
    user = request.user
    context = {}

    if user.is_staff:
        pass
    else:
        patient = user.patient_info
        medical_records = patient.medical_records.all()

        context["patient"] = patient
        context["medical_records"] = medical_records

    return render(request, "app/index.html", context)


@login_required
def profile_page(request):
    return render(request, "app/profile.html")
