from django import forms
from .models import Hospital, Patient, MedicalRecord, PatientTransfer


class HospitalForm(forms.ModelForm):
    class Meta:
        model = Hospital
        fields = ["name", "location", "capacity"]


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = [
            "first_name",
            "last_name",
            "gender",
            "birthdate",
            "hospital",
            "is_admitted",
            "status",
        ]


class MedicalRecordForm(forms.ModelForm):
    class Meta:
        model = MedicalRecord
        fields = ["patient", "diagnosis", "treatment", "medications", "date_of_visit"]


class PatientTransferForm(forms.ModelForm):
    class Meta:
        model = PatientTransfer
        fields = ["patient", "from_hospital", "to_hospital"]
