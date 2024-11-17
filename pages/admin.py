from django.contrib import admin
from .models import Team
from django.utils.html import format_html


# customize admin preview

class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40"/>', object.photo.url)
    
    thumbnail.short_description = 'Avatar'
    
    list_display = ('id', 'thumbnail', 'firstname', 'lastname', 'role', 'created_date')
    list_display_links = ('id', 'firstname',)
    search_fields = ('firstname', 'lastname', 'role')
    list_filter = ('role',)


# Register your models here.
admin.site.register(Team, TeamAdmin)