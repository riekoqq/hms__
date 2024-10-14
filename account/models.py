import datetime
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
    qualifications = models.TextField(blank=True)
    contact_number = models.CharField(max_length=15, blank=True)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=255, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} ({self.role} at {self.hospital.name})"


class WorkDay(models.Model):
    DAYS_OF_THE_WEEK = [
        ("MON", "Monday"),
        ("TUE", "Tuesday"),
        ("WED", "Wednesday"),
        ("THU", "Thursday"),
        ("FRI", "Friday"),
        ("SAT", "Saturday"),
    ]

    name = models.CharField(max_length=3, choices=DAYS_OF_THE_WEEK, unique=True)

    def __str__(self):
        return self.get_name_display()


class ShiftSchedule(models.Model):
    user_info = models.ForeignKey(
        UserInfo, on_delete=models.CASCADE, related_name="shift_schedules"
    )
    shift_start = models.TimeField()
    shift_end = models.TimeField()
    days = models.ManyToManyField(WorkDay)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        days_str = ", ".join([day.get_name_display() for day in self.days.all()])
        return f"{self.user_info.user.username} - {days_str} ({self.shift_start} to {self.shift_end})"


class Attendance(models.Model):
    user_info = models.ForeignKey(
        UserInfo, on_delete=models.CASCADE, related_name="attendance_records"
    )
    date = models.DateField(auto_now_add=True)
    time_in = models.TimeField(null=True, blank=True)
    time_out = models.TimeField(null=True, blank=True)
    is_late = models.BooleanField(default=False)
    remarks = models.TextField(blank=True, null=True)

    def calculate_late(self, standard_time_in):
        if self.time_in and self.time_in > standard_time_in:
            self.is_late = True

    def __str__(self):
        return f"Attendance for {self.user_info.user.username} on {self.date}"

    def save(self, *args, **kwargs):
        standard_time_in = datetime.time(9, 0, 0)
        self.calculate_late(standard_time_in)
        super().save(*args, **kwargs)
