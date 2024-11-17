from django.contrib import admin
from .models import Flat


# Register your models here.
class FlatAdmin(admin.ModelAdmin):
    list_display = ('id', 'flat_title', 'type', 'state', 'rent_sale', 'created_date', 'is_featured')
    list_display_links = ('id', 'flat_title',)
    list_editable = ('is_featured',)
    search_fields = ('id', 'flat_title', 'type', 'state', 'rent_sale')
    list_filter = ('type', 'rent_sale')

    
admin.site.register(Flat, FlatAdmin)
