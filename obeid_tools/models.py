from django.db import models


class Youtube(models.Model):
    url = models.URLField(max_length=256)
    title = models.CharField(max_length=512)
    id = models.CharField(max_length=32, primary_key=True)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
