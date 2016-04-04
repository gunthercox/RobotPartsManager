from rest_framework import serializers
from parts_manager.robots.models import Robot


class RobotSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Robot
        fields = ('id', 'url', 'name')
