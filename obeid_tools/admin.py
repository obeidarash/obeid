from django.contrib import admin
from .models import Youtube


@admin.register(Youtube)
class YoutubeAdmin(admin.ModelAdmin):
    list_display = ('title', 'datetime')
