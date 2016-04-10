import factory
import faker
from parts_manager.robots.models import Robot


fake = faker.Faker()


class RobotFactory(factory.DjangoModelFactory):

    name = factory.LazyAttribute(lambda n: fake.name())

    class Meta:
        model = Robot
