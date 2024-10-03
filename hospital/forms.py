from django import forms
from .models import Hospital, Patient, MedicalRecord, PatientTransfer


class HospitalForm(forms.ModelForm):
    class Meta:
        model = Hospital
        fields = ["name", "location", "capacity"]


class PatientForm(forms.ModelForm):
    STATUS_CHOICES = [("Inactive", "Inactive"), ("Active", "Active")]

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

        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "gender": forms.Select(attrs={"class": "form-control"}),
            "birthdate": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date",  # Use HTML5 date input
                }
            ),
            "hospital": forms.Select(attrs={"class": "form-control"}),
            "is_admitted": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "status": forms.Select(attrs={"class": "form-control"}),
        }


class MedicalRecordForm(forms.ModelForm):
    class Meta:
        model = MedicalRecord
        fields = ["patient", "diagnosis", "treatment", "medications", "date_of_visit"]


class PatientTransferForm(forms.ModelForm):
    class Meta:
        model = PatientTransfer
        fields = ["patient", "from_hospital", "to_hospital"]
