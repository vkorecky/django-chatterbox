from django.contrib import admin
from django.contrib.admin import ModelAdmin

from base.models import Room, Message


class RoomAdmin(ModelAdmin):
    # ListView
    ordering = ['id']
    list_display = ['id', 'name', 'description']
    list_display_links = ['id', 'name']
    list_per_page = 20
    search_fields = ['name', 'description']

    # FormView
    fieldsets = [
        (
            None,
            {
                'fields': ['id', 'name', 'description'],
            }
        ),
        (
            'Detail',
            {
                'fields': ['participants', 'created', 'updated'],
                'description': 'Detailed information about room.'
            }
        ),
    ]
    readonly_fields = ['id', 'created', 'updated']


class MessageAdmin(ModelAdmin):
    # ListView
    @staticmethod
    def cleanup_body(modeladmin, request, queryset):
        queryset.update(body="--- Deleted ---")

    ordering = ['id']
    list_display = ['id', 'room', 'body_short']
    list_display_links = ['id', 'body_short']
    list_per_page = 20
    list_filter = ['room']
    search_fields = ['body', 'id']
    actions = ['cleanup_body']

    # FormView
    fieldsets = [
        (
            None,
            {
                'fields': ['id', 'body']
            }
        ),
        (
            'Detail',
            {
                'fields': ['room', 'created', 'updated'],
                'description': 'Detailed information about room.'
            }
        ),
        (
            'User Information',
            {
                'fields': ['user']
            }
        ),
    ]
    readonly_fields = ['id', 'created', 'updated']


# Register your models here.
admin.site.register(Room, RoomAdmin)
admin.site.register(Message, MessageAdmin)
