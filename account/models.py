from django.contrib.auth.models import User
from django.db import models


class Account(models.Model):
    image = models.ImageField(upload_to='image')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    place = models.CharField(max_length=30)

    def __str__(self):
        return self.user

