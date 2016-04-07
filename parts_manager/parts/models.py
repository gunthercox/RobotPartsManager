from django.db import models


class Part(models.Model):
    """
    A part that a robot can have.
    """
    name = models.CharField(
        max_length=200,
        help_text='The name of the part.'
    )

    def __str__(self):
        return self.name
