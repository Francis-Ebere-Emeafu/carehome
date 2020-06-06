from django.contrib import admin

# Register your models here.
from workbook.forms import (
    FoodForm,
)
from workbook.models import (
    Task, StaffTask,
    EmotionalWellbeing,
    HealthHygiene,
    Education,
    Activity,
    Achievement,
    Appointment,
    KeyWork,
    Incident,
    Food,
    )

# Record


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_lisplay = ['title']


@admin.register(StaffTask)
class StaffTaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'staff', 'completed', 'when']


@admin.register(EmotionalWellbeing)
class EmotionalWellbeingAdmin(admin.ModelAdmin):
    list_display = []

@admin.register(HealthHygiene)
class HealthHygieneAdmin(admin.ModelAdmin):
    list_display = []

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = []

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = []

@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = []

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = []

@admin.register(KeyWork)
class KeyWorkAdmin(admin.ModelAdmin):
    list_display = []

@admin.register(Incident)
class IncidentAdmin(admin.ModelAdmin):
    list_display = []

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ['meal']
    form = FoodForm
    search_fields = ['meal']


# @admin.register(StaffTask)
# class StaffTaskAdmin(admin.ModelAdmin):
#     list_display = []
#
# @admin.register(StaffTask)
# class StaffTaskAdmin(admin.ModelAdmin):
#     list_display = []
#
