from django.db import models
from accounts.models import Account
# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    active = models.BooleanField(default=True)
    when = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class StaffTask(models.Model):
    title = models.CharField(max_length=100)
    staff = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    when = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


YES = 0
NO = 1
SELECT = 2
ANSWER = enumerate(('Yes', 'No'))

AM = 0
PM = 1
DAYTIME = enumerate(('AM', 'PM'))

POSITIVE = 0
NEGATIVE = 1
MEASURE = enumerate(('Positive', 'Negative'))

LOW = 0
HIGH = 1
DEGREE = enumerate(('Low', 'High'))

BREAKFAST = 0
LUNCH = 1
DINNER = 2
SNACKS = 3
MEALTYPE = enumerate(('Breakfast', 'Lunch', 'Dinner', 'Snacks'))


class Food(models.Model):
    meal = models.CharField(max_length=100)
    meal_type = models.PositiveIntegerField(choices=MEALTYPE, null=True, blank=True)

    def __str__(self):
        return self.meal


class EmotionalWellbeing(models.Model):
    daytime = models.PositiveIntegerField(choices=DAYTIME, null=True, blank=True)
    measure = models.PositiveIntegerField(choices=MEASURE, null=True, blank=True)
    degree = models.PositiveIntegerField(choices=DEGREE, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)


class HealthHygiene(models.Model):
    daytime = models.PositiveIntegerField(choices=DAYTIME, null=True, blank=True)
    medication_taken = models.PositiveIntegerField(choices=ANSWER, null=True, blank=True)
    teeth_brushed = models.PositiveIntegerField(choices=ANSWER, null=True, blank=True)
    bath_shower = models.PositiveIntegerField(choices=ANSWER, null=True, blank=True)
    hair_washed = models.PositiveIntegerField(choices=ANSWER, null=True, blank=True)
    diet_nutrition = models.ForeignKey(Food, on_delete=models.CASCADE, null=True, blank=True)


class Education(models.Model):
    hours_attended = models.CharField(max_length=200, null=True, blank=True)
    homework_completed = models.PositiveIntegerField(choices=ANSWER, null=True, blank=True)
    educational_activity = models.CharField(max_length=200, null=True, blank=True)
    school_contact = models.CharField(max_length=200, null=True, blank=True)


class Activity(models.Model):
    planned_activities = models.CharField(max_length=200, null=True, blank=True)
    other_activities = models.CharField(max_length=200, null=True, blank=True)
    # undertaken_activities = models.CharField(max_length=20)
    undertaken_activities = models.PositiveIntegerField(choices=ANSWER, null=True, blank=True)


class Achievement(models.Model):
    first = models.CharField(max_length=200, null=True, blank=True)
    second = models.CharField(max_length=200, null=True, blank=True)
    third = models.CharField(max_length=200, null=True, blank=True)


class Appointment(models.Model):
    health_appointment = models.PositiveIntegerField(choices=ANSWER, null=True, blank=True)
    professional_appointment = models.PositiveIntegerField(choices=ANSWER, null=True, blank=True)
    contact_visit_call = models.PositiveIntegerField(choices=ANSWER, null=True, blank=True)


class KeyWork(models.Model):
    requested_planned = models.PositiveIntegerField(choices=ANSWER, null=True, blank=True)
    topic = models.TextField(blank=True, null=True)


class Incident(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    consequence = models.TextField(null=True, blank=True)
    intervention = models.TextField(null=True, blank=True)
    comments = models.TextField(null=True, blank=True)
