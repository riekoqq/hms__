from . import views
from django.urls import include, path

urlpatterns = [
    path("", views.home_page, name="home"),
    path("account/", include("account.urls")),
]
