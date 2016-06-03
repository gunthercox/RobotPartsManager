from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from parts_manager.projects.models import Project


class ProjectListView(ListView):
    template_name = 'project/list.html'
    context_object_name = 'projects'
    model = Project

    def get_queryset(self):
        parts = super(ProjectListView, self).get_queryset()

        return parts


class ProjectDetailView(DetailView):
    template_name = 'project/detail.html'
    model = Project
