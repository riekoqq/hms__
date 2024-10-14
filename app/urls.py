from . import views
from django.urls import include, path

urlpatterns = [
    path("", views.home_page, name="home"),
    path("account/", include("account.urls")),
    path("hospital/", include("hospital.urls")),
    path("profile/", views.profile_page, name="profile"),
    path("staff/", include("staff.urls")),
]
