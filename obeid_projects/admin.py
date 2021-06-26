from django.contrib import admin
from .models import Project, Customer, Category, Tag


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    ordering = ('-update',)
    list_display = ('title', 'customer', 'update', 'publish')
    autocomplete_fields = ('tag', 'category', 'customer')
    search_fields = ('title',)
    # list_editable = ('publish',)
    list_filter = ('publish', 'create', 'update')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Category)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'update')
    search_fields = ('title',)
    ordering = ('-update',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Tag)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'update')
    search_fields = ('title',)
    ordering = ('-update',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Customer)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'lastname', 'email', 'update')
    search_fields = ('name', 'lastname')
    prepopulated_fields = {'slug': ('name', 'lastname')}
    ordering = ('-update',)
