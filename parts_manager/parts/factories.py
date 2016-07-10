import factory
from parts_manager.parts.models import Part


class PartFactory(factory.DjangoModelFactory):

    name = factory.Faker('sentence', nb_words=5, variable_nb_words=True)

    class Meta:
        model = Part
