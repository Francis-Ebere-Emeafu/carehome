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

admin.site.register(EmotionalWellbeing)
# @admin.register(EmotionalWellbeing)
# class EmotionalWellbeingAdmin(admin.ModelAdmin):
#     list_display = []

admin.site.register(HealthHygiene)
# @admin.register(HealthHygiene)
# class HealthHygieneAdmin(admin.ModelAdmin):
#     list_display = []

admin.site.register(Education)
# @admin.register(Education)
# class EducationAdmin(admin.ModelAdmin):
#     list_display = []

admin.site.register(Activity)
# @admin.register(Activity)
# class ActivityAdmin(admin.ModelAdmin):
#     list_display = []

admin.site.register(Achievement)
# @admin.register(Achievement)
# class AchievementAdmin(admin.ModelAdmin):
#     list_display = []

admin.site.register(Appointment)
# @admin.register(Appointment)
# class AppointmentAdmin(admin.ModelAdmin):
#     list_display = []

admin.site.register(KeyWork)
# @admin.register(KeyWork)
# class KeyWorkAdmin(admin.ModelAdmin):
#     list_display = []

admin.site.register(Incident)
# @admin.register(Incident)
# class IncidentAdmin(admin.ModelAdmin):
#     list_display = []

admin.site.register(Food)
# @admin.register(Food)
# class FoodAdmin(admin.ModelAdmin):
#     list_display = ['meal']
#     form = FoodForm
#     search_fields = ['meal']


# @admin.register(StaffTask)
# class StaffTaskAdmin(admin.ModelAdmin):
#     list_display = []
#
# @admin.register(StaffTask)
# class StaffTaskAdmin(admin.ModelAdmin):
#     list_display = []
#
