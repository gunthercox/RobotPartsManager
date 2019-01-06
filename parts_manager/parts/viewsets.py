from rest_framework import viewsets, filters
from parts_manager.parts.models import Part
from parts_manager.parts.serializers import PartSerializer


class PartViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows parts to be viewed or edited.
    """
    queryset = Part.objects.all()
    serializer_class = PartSerializer

    filter_backends = (
        filters.SearchFilter,
    )
    search_fields = ('name', )
