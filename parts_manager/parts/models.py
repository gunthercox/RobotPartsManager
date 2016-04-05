from django.db import models


class Part(models.Model):
    """
    A part that a robot can have.
    """
    name = models.CharField(
        max_length=200,
        help_text='The name of the part.'
    )
    retailer = models.ForeignKey(
        'parts.Retailer',
        related_name='parts',
        help_text='The retailer that sells this part.'
    )

    def __str__(self):
        return self.name


class Retailer(models.Model):
    """
    A retailer that sells parts.
    """
    name = models.CharField(
        max_length=50,
        help_text='The name of the retailer.'
    )
    website = models.URLField(
        max_length=200,
        help_text='The website for the retailer.'
    )

    def __str__(self):
        return self.name
