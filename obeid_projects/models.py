from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, EmailValidator
from django.contrib.auth.models import User
from django_countries.fields import CountryField


class ProjectManager(models.Manager):
    def published_project(self, project_id):
        qs = self.get_queryset().filter(id=project_id, publish=True)
        if qs.count() == 1:
            return qs.first()
        else:
            return None


class Tag(models.Model):
    title = models.CharField(max_length=32)
    slug = models.SlugField(max_length=32)

    def __str__(self):
        return self.title


class Customer(models.Model):
    name = models.CharField(max_length=64, null=True, blank=True)
    lastname = models.CharField(max_length=64, null=True, blank=True)
    email = models.EmailField(null=True, blank=True, validators=[EmailValidator])
    phone = models.CharField(max_length=32, blank=True, null=True)
    country = CountryField(null=True, blank=True)

    def __str__(self):
        return "{} {}".format(self.name, self.lastname)


class Category(models.Model):
    title = models.CharField(max_length=64, unique=True)
    slug = models.SlugField(max_length=64, unique=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Categories'


class Project(models.Model):
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=256)
    content = models.TextField(null=True, blank=True)
    progress = models.PositiveIntegerField(default=5, validators=[MinValueValidator(0), MaxValueValidator(100)])
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ManyToManyField(Category, blank=True, verbose_name='Categories')
    tag = models.ManyToManyField(Tag, blank=True)
    publish = models.BooleanField(default=True)
    objects = ProjectManager()

    def __str__(self):
        return self.title
