from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from datetime import datetime


class Account(models.Model):
    STAFF = 0
    SENIOR_STAFF = 1
    MANAGER = 2
    USER_TYPE = enumerate(('Staff', 'Senior Staff', 'Manager'))

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_type = models.PositiveIntegerField(choices=USER_TYPE, default=STAFF)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    active = models.BooleanField(default=True)
    when = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name
