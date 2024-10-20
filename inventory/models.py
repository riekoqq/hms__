from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    hospital = models.ForeignKey('hospital.Hospital', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Supplier(models.Model):
    name = models.CharField(max_length=200)
    contact_name = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    hospital = models.ForeignKey('hospital.Hospital', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Item(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    quantity = models.PositiveIntegerField(default=0)
    reorder_level = models.PositiveIntegerField(default=0)
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True, blank=True)
    hospital = models.ForeignKey('hospital.Hospital', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

    def is_below_reorder_level(self):
        return self.quantity <= self.reorder_level


class Stock(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    transaction_type = models.CharField(max_length=10, choices=[('add', 'Add'), ('remove', 'Remove')])
    transaction_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    hospital = models.ForeignKey('hospital.Hospital', on_delete=models.CASCADE, null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.transaction_type == 'add':
            self.item.quantity += self.quantity
        elif self.transaction_type == 'remove':
            self.item.quantity -= self.quantity
        self.item.save()

    def __str__(self):
        return f"{self.transaction_type} {self.quantity} {self.item.name} on {self.transaction_date}"


