from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from parts_manager.robots.models import Robot, RobotPart
from parts_manager.products.models import Product
from parts_manager.robots.serializers import (
    RobotSerializer,
    RobotPartSerializer
)


class RobotViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows robots to be viewed or edited.
    """
    queryset = Robot.objects.all()
    serializer_class = RobotSerializer

    @detail_route(methods=['get'])
    def parts_manifest_current(self, request, pk=None):
        """
        Return a list of all parts used by this robot.
        """
        robot = self.get_object()
        parts = robot.robot_parts.all()

        serializer = RobotPartSerializer(
            parts,
            many=True,
            context={'request': request}
        )

        return Response(serializer.data)

    @detail_route(methods=['get'])
    def parts_manifest_optimal(self, request, pk=None):
        """
        Return a list of all parts used by this robot.
        """

        parts = []

        return Response(parts)


class RobotPartViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows a robot's parts to be viewed or edited.
    """
    queryset = RobotPart.objects.all()
    serializer_class = RobotPartSerializer
