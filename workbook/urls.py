from django.urls import path

from workbook import views
# from accounts.utils import home

urlpatterns = [
    # path("", home, name="home"),
    path("create/", views.create_task, name="create_task"),

    path("list/", views.manage_all_task, name="manage_all_task"),
    path("completed/", views.completed_task, name="completed_task"),
    path("incompleted/", views.incompleted_task, name="incompleted_task"),
    path("assign/list", views.assign_task_list, name="assign_task_list"),
    path("assign/<int:task_id>/<int:staff_id>/", views.assign_task, name="assign_task"),

    path("edit/<int:task_id>/", views.edit_task, name="edit_task"),

    path("delete/<int:task_id>/", views.delete_task, name="delete_task"),
    path("delete/confirm/<int:task_id>/", views.confirm_delete_task, name="confirm_delete_task"),
    # path("modify/<int:profile_id>/", views.modify_staff, name="modify_staff"),
    #
    # path("profile/", views.profile, name="profile"),
    # path("logout", views.logout_user, name="logout"),

]
