from . import views
from django.urls import path


app_name = "hospital"

urlpatterns = [
    path("", views.hospital_page, name="hospital"),
    path("transfer/", views.transfer_page, name="hospital-transfer"),
    path("<int:hospital_id>/", views.hospital_detail_page, name="hospital-detail"),
]

# patients url
urlpatterns += [
    path("patient/", views.manage_patient_page, name="patient"),
    path("patient/add/", views.add_patient_page, name="add-patient"),
    path(
        "patient/admission-discharge/",
        views.admission_discharge_page,
        name="admission-discharge",
    ),
    path(
        "patient/add-medical-record/",
        views.add_medical_record_page,
        name="add-medical-record",
    ),
]
