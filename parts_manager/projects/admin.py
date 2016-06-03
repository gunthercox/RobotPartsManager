from django.contrib import admin
from parts_manager.projects.models import Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', )


admin.site.register(Project, ProjectAdmin)
