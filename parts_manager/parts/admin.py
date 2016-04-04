from django.contrib import admin
from parts_manager.parts.models import Part, Retailer


class PartAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )


class RetailerAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )


admin.site.register(Part, PartAdmin)
admin.site.register(Retailer, RetailerAdmin)
