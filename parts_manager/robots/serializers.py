from rest_framework import serializers
from parts_manager.robots.models import Robot, RobotPart
from parts_manager.products.serializers import ProductSerializer


class RobotSerializer(serializers.ModelSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='api:robot-detail'
    )

    parts_manifest_current = serializers.HyperlinkedIdentityField(
        view_name='api:robot-parts-manifest-current'
    )

    parts_manifest_optimal = serializers.HyperlinkedIdentityField(
        view_name='api:robot-parts-manifest-optimal'
    )

    class Meta:
        model = Robot
        fields = (
            'id', 'url', 'name',
            'parts_manifest_current', 'parts_manifest_optimal',
        )


class RobotPartSerializer(serializers.ModelSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='api:robotpart-detail'
    )

    condition = serializers.ChoiceField(RobotPart.PART_CONDITION_CHOICES)

    robot = RobotSerializer()
    product = ProductSerializer()

    class Meta:
        model = Robot
        fields = ('id', 'url', 'condition', 'robot', 'product', )
