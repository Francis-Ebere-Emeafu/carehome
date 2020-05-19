from django.urls import path

from children import views

urlpatterns = [
    path("register/", views.register_child, name="register_child"),
    path("list/", views.children_list, name="children_list"),
    path("modify/<int:child_id>/", views.modify_child_details, name="modify_child_details"),

    # path("s-staff/", views.senior_staff_profile, name="senior_staff_profile"),
    # path("manager/", views.manager_profile, name="manager_profile"),
    #
    # path("staff/list/", views.staff_management_list, name="staff_management_list"),
    # path("delete/<int:profile_id>/", views.delete_staff, name="delete_staff"),
    # path("delete-staff/<int:profile_id>/", views.confirm_delete_staff, name="confirm_delete_staff"),
    #
    # path("profile/", views.create_super_user_profile, name="profile"),
    # path("logout", views.logout_user, name="logout"),
]
