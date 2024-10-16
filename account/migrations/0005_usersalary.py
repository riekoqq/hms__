# Generated by Django 5.1.1 on 2024-10-16 12:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_attendance'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSalary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base_salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('bonuses', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('deductions', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('total_salary', models.DecimalField(decimal_places=2, editable=False, max_digits=10)),
                ('last_payment_date', models.DateField(blank=True, null=True)),
                ('next_payment_date', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user_info', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='salary_info', to='account.userinfo')),
            ],
        ),
    ]
