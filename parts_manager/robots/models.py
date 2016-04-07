from django.db import models


class Robot(models.Model):
    """
    An entity that represents a single robot.
    """
    name = models.CharField(
        max_length=20,
        help_text='The robot\'s name.'
    )

    parts = models.ManyToManyField(
        'products.Product',
        blank=True,
        help_text='The parts used by this robot.'
    )

    def __str__(self):
        return self.name
