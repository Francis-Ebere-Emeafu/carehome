from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#farmer database to insert the data into the table or retrive
#the data alse from the databases tables
class Farmer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    email = models.CharField(max_length = 50)
    occupation=models.CharField(max_length=30)
    phone_number = models.CharField(max_length=50)
    address = models.CharField(max_length = 50)
    state=models.CharField(max_length=20)

    def __str__(self):
        return self.user.username

#createing a sigunp data into the table for database record into them
#buyer data base
class Buyer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    email = models.CharField(max_length = 50)
    occupation=models.CharField(max_length=30)
    phone_number = models.CharField(max_length=50)
    address = models.CharField(max_length = 50)
    state=models.CharField(max_length=20)

    def __str__(self):
        return self.user.username
