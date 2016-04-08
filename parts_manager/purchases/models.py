from django.db import models
from django.core.exceptions import ValidationError


class Purchase(models.Model):

    products = models.ManyToManyField(
        'products.Product',
        help_text='The parts included in this purchase.'
    )

    shipping = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        help_text='The cost of shipping for this purchase.'
    )

    discounts = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        help_text='The total sum of any discounts applied to this purchase.'
    )

    def get_price(self):
        """
        Return the sum of the prices of each product in the order.
        """
        from django.db.models import Sum
        price = self.products.aggregate(Sum('price'))
        return price['price__sum']

    def get_total_price(self):
        return self.get_price() + self.shipping - self.discounts

    def clean(self):
        super(Purchase, self).clean()

        # Check to make sure each product has the same retailer
        '''
        retailer = self.products.first().retailer
        for product in self.products:
            if product.retailer != retailer:
                raise ValidationError(_('All parts must be purchased from the same retailer.'))
        '''
