from . import views
from django.contrib.auth.views import LogoutView
from django.urls import path

app_name = "account"

urlpatterns = [
    path("login/", views.custom_login, name="login"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
]
