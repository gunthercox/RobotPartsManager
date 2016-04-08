import factory
import faker
from parts_manager.parts.models import Part

fake = faker.Faker()


class PartFactory(factory.DjangoModelFactory):

    name = factory.LazyAttribute(lambda n: fake.sentence(
        nb_words=5,
        variable_nb_words=True
    ))

    class Meta:
        model = Part
