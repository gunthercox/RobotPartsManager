from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from parts_manager.robots.models import Robot, RobotPart
from parts_manager.parts.models import Part
from parts_manager.products.models import Product
from parts_manager.products.serializers import ProductSerializer
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
        Return a list of all parts currently used by this robot.
        """
        robot = self.get_object()
        parts = robot.robot_parts.all().order_by('product__item__name')

        serializer = RobotPartSerializer(
            parts,
            many=True,
            context={'request': request}
        )

        return Response(serializer.data)

    @detail_route(methods=['get'])
    def parts_manifest_optimal(self, request, pk=None):
        """
        Return a list of all products used by this robot,
        optimized such that each product shown is the lowest price.
        """
        robot = self.get_object()
        robot_parts = robot.robot_parts.all()
        part_ids = robot_parts.values_list('product__id', flat=True)

        product_results = []

        # For each part, get the product with the lowest price
        for part_id in part_ids:
            part = Part.objects.get(id=part_id)

            # TODO: Account for shipping
            product = Product.objects.filter(item=part).order_by('price')

            product_results.append(product.first())

        serializer = ProductSerializer(
            product_results,
            many=True,
            context={'request': request}
        )

        return Response(serializer.data)


class RobotPartViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows a robot's parts to be viewed or edited.
    """
    queryset = RobotPart.objects.all()
    serializer_class = RobotPartSerializer
