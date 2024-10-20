from django.contrib import admin
from .models import Category, Supplier, Item, Stock

admin.site.register(Category)
admin.site.register(Supplier)
admin.site.register(Item)
admin.site.register(Stock)