from django.urls import path

from accounts import views
from accounts.utils import home

urlpatterns = [

    path("", home, name="home"),
    path("register/", views.register_staff, name="register_staff"),

    path("staff/", views.staff_profile, name="staff_profile"),
    path("s-staff/", views.senior_staff_profile, name="senior_staff_profile"),
    path("manager/", views.manager_profile, name="manager_profile"),

    path("staff/list/", views.staff_management_list, name="staff_management_list"),
    path("modify/<int:profile_id>/", views.modify_staff, name="modify_staff"),
    path("delete/<int:profile_id>/", views.delete_staff, name="delete_staff"),
    path("delete-staff/<int:profile_id>/", views.confirm_delete_staff, name="confirm_delete_staff"),

    path("profile/", views.create_super_user_profile, name="profile"),
    path("logout", views.logout_user, name="logout"),

]
