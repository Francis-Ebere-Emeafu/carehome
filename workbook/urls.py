from django.urls import path

from workbook import views
# from accounts.utils import home

urlpatterns = [
    # path("", home, name="home"),
    path("create/", views.create_task, name="create_task"),
    #
    #
    # path("staff/", views.staff_profile, name="staff_profile"),
    # path("s-staff/", views.senior_staff_profile, name="senior_staff_profile"),
    # path("manager/", views.manager_profile, name="manager_profile"),
    #
    # path("staff/list/", views.staff_management_list, name="staff_management_list"),
    # path("modify/<int:profile_id>/", views.modify_staff, name="modify_staff"),
    #
    # path("profile/", views.profile, name="profile"),
    # path("logout", views.logout_user, name="logout"),

]
