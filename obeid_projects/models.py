from django.db import models


class ProjectManager(models.Manager):
    pass


class Project(models.Model):
    title = models.CharField(max_length=256)
    objects = ProjectManager()

    def __str__(self):
        return self.title
