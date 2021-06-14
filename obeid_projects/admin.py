from django.contrib import admin
from .models import Project, Customer, Category


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'customer')


@admin.register(Category)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Customer)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'lastname', 'email')
