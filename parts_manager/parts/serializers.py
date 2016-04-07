from rest_framework import serializers
from parts_manager.parts.models import Part


class PartSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api:part-detail')

    class Meta:
        model = Part
        fields = ('id', 'url', 'name', )
