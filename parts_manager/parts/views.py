from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from parts_manager.parts.models import Part


class PartListView(ListView):
    template_name = 'part/list.html'
    context_object_name = 'parts'
    model = Part

    def get_queryset(self):
        parts = super(PartListView, self).get_queryset()

        return parts


class PartDetailView(DetailView):
    template_name = 'part/detail.html'
    model = Part
