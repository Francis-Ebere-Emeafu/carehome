from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from datetime import datetime


class Child(models.Model):
    MALE = 0
    FEMALE = 1
    SELECT = 2
    GENDER = enumerate(('Male', 'Female', 'Select'))

    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.PositiveIntegerField(choices=GENDER, default=SELECT)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    assigned = models.BooleanField(default=False)
    when = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name
        
    @property
    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)


class ChildRecord(models.Model):
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    feeding = models.TextField()
    medication = models.TextField()
    behaviour = models.TextField()
    notes = models.TextField()
    visit = models.TextField()
