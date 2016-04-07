from rest_framework import serializers
from parts_manager.products.models import Product, Retailer
from parts_manager.parts.serializers import PartSerializer


class RetailerSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='api:retailer-detail'
    )

    class Meta:
        model = Retailer
        fields = ('id', 'url', 'name', )


class ProductSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='api:product-detail'
    )
    item = PartSerializer()
    retailer = RetailerSerializer()

    class Meta:
        model = Product
        fields = (
            'id', 'url',
            'item', 'retailer',
        )
