from .models import Hospital
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def hospital_page(request):
    hospitals = Hospital.objects.all()

    context = {}
    context["hospitals"] = hospitals
    return render(request, "hospital/hospital.html", context)


def transfer_page(request):
    return render(request, "hospital/transfer.html")
