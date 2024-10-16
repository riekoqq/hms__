# Generated by Django 5.1.1 on 2024-10-14 09:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_remove_shiftschedule_assigned_by_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('time_in', models.TimeField(blank=True, null=True)),
                ('time_out', models.TimeField(blank=True, null=True)),
                ('is_late', models.BooleanField(default=False)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('user_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendance_records', to='account.userinfo')),
            ],
        ),
    ]
