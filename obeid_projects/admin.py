import csv
from django.contrib import messages
from django.utils.translation import ngettext
from django.contrib import admin
from django.http import HttpResponse

from .models import Project, Customer, Category, Tag


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    ordering = ('-update',)
    list_display = ('title', 'customer', 'progress', 'primary', 'publish')
    autocomplete_fields = ('tag', 'category', 'customer')
    search_fields = ('title',)
    list_editable = ('progress',)
    list_filter = ('publish', 'create', 'update')
    prepopulated_fields = {'slug': ('title',)}
    actions = ['publish_projects', 'unpublish_projects', 'export_as_csv']
    actions_on_bottom = True

    def publish_projects(self, request, queryset):
        queryset.update(publish=True)
        # todo: add message to this

    def unpublish_projects(self, request, queryset):
        queryset.update(publish=False)
        # todo: add message to this

    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    publish_projects.short_description = 'Publish selected projects'
    unpublish_projects.short_description = 'Draft selected projects'
    export_as_csv.short_description = "Export Selected projects"

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
