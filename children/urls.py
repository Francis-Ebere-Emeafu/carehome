from django.urls import path

from children import views

urlpatterns = [
    path("register/", views.register_child, name="register_child"),
    path("list/", views.children_list, name="children_list"),
    path("modify/<int:child_id>/", views.modify_child_details, name="modify_child_details"),

    path("assignment/list/", views.child_assignment_list, name="child_assignment_list"),
    path("assignments/list/", views.child_assignment_list2, name="child_assignment_list2"),
    path("select/<int:child_id>/", views.select_child, name="select_child"),
    path("selects/<int:child_id>/", views.mandatory_select_child, name="mandatory_select_child"),

    path("record/list/", views.child_record_list, name="child_record_list"),
    path("selection/list/", views.my_child_selections, name="my_child_selections"),
    path("record/<int:child_id>/update/", views.create_edit_child_record, name="create_edit_child_record"),

    #
    path("create/record", views.create_record, name="create_record"),
    # path("logout", views.logout_user, name="logout"),
]
