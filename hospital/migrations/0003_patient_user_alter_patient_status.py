# Generated by Django 5.1.1 on 2024-10-10 00:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0002_alter_patient_status'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='patient_info', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='patient',
            name='status',
            field=models.CharField(choices=[('Inactive', 'Inactive'), ('Active', 'Active'), ('Admission', 'Admission'), ('Discharge', 'Discharge')], max_length=10),
        ),
    ]
