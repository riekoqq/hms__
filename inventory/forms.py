from django import forms
from .models import Category, Supplier, Item
from hospital.models import Hospital


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description', 'hospital']


class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['name', 'contact_name', 'phone_number', 'email', 'hospital']


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['category', 'name', 'description', 'quantity', 'reorder_level', 'supplier', 'hospital']


