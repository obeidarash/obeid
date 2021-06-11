from django.db import models
from django.contrib.auth.models import User


class Scrape(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    url = models.URLField(verbose_name="Link")
    title = models.CharField(max_length=256)
    color = models.CharField(max_length=256)
    size = models.CharField(max_length=256)
    stock = models.IntegerField(verbose_name='In Stock', default=0)
    publish = models.BooleanField(default=False)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} - {}".format(self.title, self.size)


class Contact(models.Model):
    name = models.CharField(max_length=128)
    subject = models.CharField(max_length=256)
    email = models.EmailField()
    content = models.TextField(max_length=2048)
    datetime = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return "{} - {}".format(self.name, self.subject)
