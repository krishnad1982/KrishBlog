from django.db import models
from django.contrib.auth.models import Permission, User

# Create your models here.


class About(models.Model):
    content = models.TextField(max_length=500)

    def __str__(self):
        return self.content