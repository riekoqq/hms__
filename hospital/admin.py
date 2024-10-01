from .models import Hospital, MedicalRecord, Patient, PatientTransfer
from django.contrib import admin

# Register your models here.
admin.site.register(Hospital)
admin.site.register(MedicalRecord)
admin.site.register(Patient)
admin.site.register(PatientTransfer)
