from django.contrib import admin

# Register your models here.
from workbook.models import Task, StaffTask
# Record


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_lisplay = ['title']


@admin.register(StaffTask)
class StaffTaskAmin(admin.ModelAdmin):
    list_display = ['staff']
