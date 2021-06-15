from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, EmailValidator
from django.contrib.auth.models import User


class ProjectManager(models.Manager):
    pass


class Customer(models.Model):
    name = models.CharField(max_length=64, null=True, blank=True)
    lastname = models.CharField(max_length=64, null=True, blank=True)
    email = models.EmailField(null=True, blank=True, validators=[EmailValidator])
    phone = models.CharField(max_length=32, blank=True, null=True)

    def __str__(self):
        return "{} {}".format(self.name, self.lastname)


class Category(models.Model):
    title = models.CharField(max_length=64, unique=True)
    slug = models.SlugField(max_length=64, unique=True, blank=True)

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=256, unique=True, blank=True)
    progress = models.PositiveIntegerField(default=5, validators=[MinValueValidator(0), MaxValueValidator(100)])
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    objects = ProjectManager()

    def __str__(self):
        return self.title
