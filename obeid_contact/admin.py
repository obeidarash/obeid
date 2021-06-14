from django.contrib import admin

from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'email', 'is_read', 'datetime')
    search_fields = ('name', 'subject', 'email', 'content')
    list_filter = ('datetime',)
    list_editable = ('is_read',)
    list_per_page = 20
