from django.contrib import admin
from .models import Project, Customer


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'customer')


@admin.register(Customer)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'lastname', 'email')
