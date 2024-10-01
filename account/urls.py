from . import views
from django.urls import path

app_name = "account"

urlpatterns = [
    path("login/", views.custom_login, name="login"),
    path("logout/", views.custom_logout, name="logout"),
]
