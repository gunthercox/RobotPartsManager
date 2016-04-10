from django.db import models


class Product(models.Model):
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    item = models.ForeignKey(
        'parts.Part',
        help_text='The part that this product is for.'
    )

    retailer = models.ForeignKey(
        'products.Retailer',
        help_text='The retailer that sells this product.'
    )

    def __str__(self):
        return self.item.name


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
