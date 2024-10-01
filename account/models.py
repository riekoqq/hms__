from django.contrib.auth.models import User
from django.db import models
from hospital.models import Hospital


class UserInfo(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="user_info"
    )
    hospital = models.ForeignKey(
        Hospital, on_delete=models.CASCADE, related_name="staff"
    )
    role = models.CharField(max_length=100)
    date_of_joining = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username} ({self.role} at {self.hospital.name})"
