from django.contrib import admin
from parts_manager.parts.models import Part


class PartAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )


admin.site.register(Part, PartAdmin)
