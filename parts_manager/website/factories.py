import factory
from django.contrib.auth.models import User


class UserFactory(factory.DjangoModelFactory):

    username = factory.Sequence(lambda n: 'user%d' % n)
    email = factory.LazyAttribute(lambda obj: '%s@example.com' % obj.username)
    password = factory.PostGenerationMethodCall('set_password', 'test')

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')

    class Meta:
        model = User
