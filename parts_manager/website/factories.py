import factory
from django.contrib.auth.models import User


class UserFactory(factory.Factory):

    username = factory.Sequence(lambda n: 'user%d' % n)
    email = factory.LazyAttribute(lambda obj: '%s@example.com' % obj.username)
    password = factory.PostGenerationMethodCall('set_password', 'test')

    class Meta:
        model = User
