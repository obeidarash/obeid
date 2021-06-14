from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):
    name = models.CharField(max_length=128)
    subject = models.CharField(max_length=256)
    email = models.EmailField()
    content = models.TextField(max_length=2048)
    datetime = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return "{} - {}".format(self.name, self.subject)
