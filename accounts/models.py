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
    image = models.ImageField(upload_to='profile_pics', null=True, blank=True)
    active = models.BooleanField(default=True)
    when = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse("", kwargs={"id": self.id})

    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url

    @property
    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)
