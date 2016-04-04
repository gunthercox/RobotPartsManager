from django.contrib import admin
from parts_manager.robots.models import Robot


class RobotAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )


admin.site.register(Robot, RobotAdmin)
