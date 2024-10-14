from .models import UserInfo, WorkDay, ShiftSchedule, Attendance
from django.contrib import admin

# Register your models here.
admin.site.register(UserInfo)
admin.site.register(WorkDay)
admin.site.register(ShiftSchedule)
admin.site.register(Attendance)
