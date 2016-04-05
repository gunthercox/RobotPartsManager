from rest_framework import serializers
from parts_manager.robots.models import Robot
from parts_manager.parts.models import Part
from parts_manager.parts.serializers import PartSerializer


class RobotSerializer(serializers.ModelSerializer):

    url = serializers.HyperlinkedIdentityField(view_name='api:robot-detail')

    parts = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='api:part-detail',
        required=False,
        queryset=Part.objects.all()
    )

    class Meta:
        model = Robot
        fields = ('id', 'url', 'name', 'parts')
