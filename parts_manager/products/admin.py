from django.contrib import admin
from parts_manager.products.models import Product, Retailer


class ProductAdmin(admin.ModelAdmin):
    list_display = ('item', )
    search_fields = ('item__name', )


class RetailerAdmin(admin.ModelAdmin):
    list_display = ('name', 'website', )
    search_fields = ('name', )


admin.site.register(Product, ProductAdmin)
admin.site.register(Retailer, RetailerAdmin)
