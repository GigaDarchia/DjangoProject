from django.db import models
from django.db.models import Model
from django.conf import settings

class UserCart(Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.user.username
