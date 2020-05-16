from django.urls import path

from accounts import views
from accounts.utils import home

urlpatterns = [
    path("register/", views.register, name="register"),
    path("", home, name="home"),

    path("staff/", views.staff_profile, name="staff_profile"),
    path("s-staff/", views.senior_staff_profile, name="senior_staff_profile"),
    path("manager/", views.manager_profile, name="manager_profile"),
    path("profile/", views.profile, name="profile"),
    path("logout", views.logout_user, name="logout"),

]
