import factory
from parts_manager.robots.models import Robot


class RobotFactory(factory.DjangoModelFactory):

    name = factory.Faker('name')

    class Meta:
        model = Robot
