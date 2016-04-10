from django.contrib import admin
from parts_manager.purchases.models import Purchase


class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('date', 'shipping', 'discounts', )


admin.site.register(Purchase, PurchaseAdmin)
