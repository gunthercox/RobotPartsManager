from rest_framework import viewsets, filters
from parts_manager.parts.models import Part
from parts_manager.parts.serializers import PartSerializer
from rest_framework import permissions
from oauth2_provider.ext.rest_framework import (
    TokenHasReadWriteScope, TokenHasScope
)


class PartViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows parts to be viewed or edited.
    """
    queryset = Part.objects.all()
    serializer_class = PartSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        TokenHasScope
    ]

    filter_backends = (
        filters.SearchFilter,
    )
    search_fields = ('name', )
