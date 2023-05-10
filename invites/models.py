from django.db import models
from user.models import Profile


class Invite(models.Model):
    from_profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="invites_from")
    to_profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="invites_to")

    def __str__(self):
        return f"Invite from {self.from_profile} to {self.to_profile}"
