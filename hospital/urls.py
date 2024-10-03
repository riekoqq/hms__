from . import views
from django.urls import path


app_name = "hospital"

urlpatterns = [
    path("", views.hospital_page, name="hospital"),
    path("transfer/", views.transfer_page, name="hospital-transfer"),
]
