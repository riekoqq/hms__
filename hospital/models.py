from django.db import models


class Hospital(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    capacity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Patient(models.Model):
    GENDER_CHOICES = [
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Other"),
    ]
    STATUS_CHOICES = [("Inactive", "Inactive"), ("Active", "Active")]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    birthdate = models.DateField()
    hospital = models.ForeignKey(
        Hospital, on_delete=models.CASCADE, related_name="patients"
    )
    is_admitted = models.BooleanField(default=False)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class MedicalRecord(models.Model):
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name="medical_records"
    )
    diagnosis = models.CharField(max_length=255)
    treatment = models.TextField()
    medications = models.CharField(max_length=255)
    date_of_visit = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Record for {self.patient} on {self.date_of_visit}"


class PatientTransfer(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    from_hospital = models.ForeignKey(
        Hospital, related_name="transfers_out", on_delete=models.CASCADE
    )
    to_hospital = models.ForeignKey(
        Hospital, related_name="transfers_in", on_delete=models.CASCADE
    )
    transfer_date = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Transfer of {self.patient} from {self.from_hospital} to {self.to_hospital}"
