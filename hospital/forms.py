from django import forms
from django.contrib.auth.models import User
from .models import Hospital, Patient, MedicalRecord, PatientTransfer


class HospitalForm(forms.ModelForm):
    class Meta:
        model = Hospital
        fields = ["name", "location", "capacity"]


class PatientForm(forms.ModelForm):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )

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

    def save(self, commit=True):
        username = self.cleaned_data["username"]
        password = self.cleaned_data["password"]
        user = User.objects.create_user(username=username, password=password)

        patient = super().save(commit=False)
        patient.user = user

        if commit:
            patient.save()

        return patient


class MedicalRecordForm(forms.ModelForm):
    class Meta:
        model = MedicalRecord
        fields = ["patient", "diagnosis", "treatment", "medications", "date_of_visit"]

        widgets = {
            "patient": forms.Select(attrs={"class": "form-control"}),
            "diagnosis": forms.TextInput(attrs={"class": "form-control"}),
            "treatment": forms.Textarea(attrs={"class": "form-control"}),
            "medications": forms.Textarea(attrs={"class": "form-control"}),
            "date_of_visit": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date",
                }
            ),
        }


class PatientTransferForm(forms.Form):
    patient = forms.ModelChoiceField(
        queryset=Patient.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        label="Select Patient",
    )
    hospital = forms.ModelChoiceField(
        queryset=Hospital.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        label="Select Hospital",
    )


class PatientStatusUpdateForm(forms.Form):
    patient = forms.ModelChoiceField(
        queryset=Patient.objects.all(),  # QuerySet to display all patients
        widget=forms.Select(attrs={"class": "form-control"}),
        label="Select Patient",
    )
    status = forms.ChoiceField(
        choices=Patient.STATUS_CHOICES,  # Choices for status
        widget=forms.Select(attrs={"class": "form-control"}),
        label="Select Status",
    )
