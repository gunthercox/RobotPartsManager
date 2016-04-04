from rest_framework import viewsets
from parts_manager.robots.models import Robot
from parts_manager.robots.serializers import RobotSerializer


class RobotViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows robots to be viewed or edited.
    """
    queryset = Robot.objects.all()
    serializer_class = RobotSerializer
