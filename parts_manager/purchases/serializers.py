from rest_framework import serializers
from parts_manager.purchases.models import Purchase


class PurchaseSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='api:purchase-detail'
    )

    price = serializers.SerializerMethodField()

    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Purchase
        fields = (
            'id', 'url',
            'price', 'shipping', 'discounts', 'total_price',
        )

    def get_price(self, obj):
        """
        The sum of the prices of each product in the order.
        """
        return obj.get_price()

    def get_total_price(self, obj):
        """
        The price plus the cost of shipping,
        minus any discounts applied to the purchase.
        """
        return obj.get_total_price()
