from django.db import models


class Part(models.Model):
    name = models.CharField(max_length=200)
    retailer = models.ForeignKey(
        'parts.Retailer',
        related_name='parts'
    )


class Retailer(models.Model):
    name = models.CharField(max_length=50)
    website = models.URLField(max_length=200)
