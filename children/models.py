from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from datetime import datetime

from accounts.models import Account
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
    )


class Child(models.Model):
    MALE = 0
    FEMALE = 1
    SELECT = 2
    GENDER = enumerate(('Male', 'Female', 'Select'))

    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.PositiveIntegerField(choices=GENDER, default=SELECT)
    legal_status = models.CharField(max_length=50)
    birth_date = models.DateField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    image = models.ImageField(upload_to='profile_pics', null=True, blank=True)
    assigned = models.BooleanField(default=False)
    when = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Child"
        verbose_name_plural = "Children"

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url

    @property
    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)


class ChildRecord(models.Model):
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    notes = models.TextField(null=True, blank=True)
    emotional_wellbeing = models.ForeignKey(EmotionalWellbeing,  on_delete=models.CASCADE, null=True, blank=True)
    health_hygiene = models.ForeignKey(HealthHygiene,  on_delete=models.CASCADE, null=True, blank=True)
    education = models.ForeignKey(Education,  on_delete=models.CASCADE, null=True, blank=True)
    activities = models.ForeignKey(Activity,  on_delete=models.CASCADE, null=True, blank=True)
    achievements = models.ForeignKey(Achievement,  on_delete=models.CASCADE, null=True, blank=True)
    appointments_contact = models.ForeignKey(Appointment,  on_delete=models.CASCADE, null=True, blank=True)
    key_work = models.ForeignKey(KeyWork,  on_delete=models.CASCADE, null=True, blank=True)
    incidents = models.ForeignKey(Incident,  on_delete=models.CASCADE, null=True, blank=True)
    addtional_info = models.TextField(null=True, blank=True)
    record_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=False, auto_now=False)

    def __str__(self):
        return "{} {}".format(self.child, self.date_created)

    class Meta:
        ordering = ["-date_created", "-id"]


class StaffChildManager(models.Model):
    child = models.ForeignKey(Child, null=True, blank=True, on_delete=models.CASCADE)
    staff = models.ForeignKey(Account, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return "{} {}".format(self.child.first_name, self.staff.first_name)
