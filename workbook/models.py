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
