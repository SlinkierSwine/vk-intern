from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    friends = models.ManyToManyField("self", null=True, blank=True)

    def __str__(self):
        return f"Profile {self.pk}"
