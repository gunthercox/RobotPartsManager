from rest_framework import viewsets
from parts_manager.purchases.models import Purchase
from parts_manager.purchases.serializers import PurchaseSerializer


class PurchaseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows purchases to be viewed or edited.
    """
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
