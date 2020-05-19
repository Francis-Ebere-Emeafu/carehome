from django.contrib import admin
from children.models import Child, ChildRecord, StaffChildManager
# Register your models here.

@admin.register(Child)
class ChildAdmin(admin.ModelAdmin):
    list_display = [
        "email",
        "first_name",
        "last_name",
        "phone",
        "when"
    ]
    search_fields = ["first_name", "last_name", "email"]


@admin.register(ChildRecord)
class ChildRecordAdmin(admin.ModelAdmin):
    list_display = [
        "child",
    ]
    search_fields = ["child" ]


@admin.register(StaffChildManager)
class StaffChildManagerAdmin(admin.ModelAdmin):
    list_display = [
        "child", "staff"
    ]
    search_fields = ["child" ]
