from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, EmailValidator
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from tinymce import models as tinymce_models


# from django.db.models.signals import pre_save


class ProjectManager(models.Manager):
    def published_project(self, project_slug):
        qs = self.get_queryset().filter(slug=project_slug, publish=True)
        if qs.count() == 1:
            return qs.first()
        else:
            return None

    def all_published_projects(self):
        return self.get_queryset().filter(publish=True)

    def projects_by_category(self, category):
        return self.get_queryset().filter(category__project__category=category, publish=True).distinct()

    def projects_by_tag(self, tag):
        return self.get_queryset().filter(tag__project__tag=tag, publish=True).distinct()


class Tag(models.Model):
    title = models.CharField(max_length=32)
    slug = models.SlugField(max_length=32, unique=True)
    update = models.DateTimeField(auto_now=True)
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Customer(models.Model):
    name = models.CharField(max_length=64, null=True, blank=True)
    slug = models.SlugField(max_length=128, unique=True, help_text='Name + Lastname')
    lastname = models.CharField(max_length=64, null=True, blank=True)
    email = models.EmailField(null=True, blank=True, validators=[EmailValidator])
    phone = models.CharField(max_length=32, blank=True, null=True)
    country = CountryField(null=True, blank=True)
    update = models.DateTimeField(auto_now=True)
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} {}".format(self.name, self.lastname)


class Category(models.Model):
    title = models.CharField(max_length=64, unique=True)
    slug = models.SlugField(max_length=64, unique=True)
    update = models.DateTimeField(auto_now=True)
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Categories'


class Project(models.Model):
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=256, unique=True)
    content = tinymce_models.HTMLField(null=True, blank=True)
    progress = models.PositiveIntegerField(default=5,
                                           validators=[MinValueValidator(0), MaxValueValidator(100)],
                                           help_text='Pick a number between 0 to 100')
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ManyToManyField(Category, blank=True, verbose_name='Categories')
    tag = models.ManyToManyField(Tag, blank=True)
    update = models.DateTimeField(auto_now=True)
    create = models.DateTimeField(auto_now_add=True)
    publish = models.BooleanField(default=True)
    objects = ProjectManager()

    def __str__(self):
        return self.title
