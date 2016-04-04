from rest_framework import serializers
from parts_manager.parts.models import Part


class PartSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Part
        fields = ('id', 'url', 'name')
