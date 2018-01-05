from django.contrib import admin
from .models import Content, Property, PropertyImage


class ContentAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'page',
        'content'
    ]
admin.site.register(Content, ContentAdmin)

class PropertyAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'completion_status',
        'unit_type',
        'location'
    ]
admin.site.register(Property, PropertyAdmin)

class PropertyImageAdmin(admin.ModelAdmin):
    list_display = [
        'mw_property',
        'is_primary'
    ]
admin.site.register(PropertyImage, PropertyImageAdmin)
