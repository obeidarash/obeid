from django.contrib import admin
from .models import Youtube


@admin.register(Youtube)
class YoutubeAdmin(admin.ModelAdmin):
    list_display = ('title', 'datetime')
    search_fields = ('title', 'id')

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False
