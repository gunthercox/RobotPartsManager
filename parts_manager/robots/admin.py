from django.contrib import admin
from parts_manager.robots.models import Robot, RobotPart


class RobotAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )


class RobotPartAdmin(admin.ModelAdmin):
    list_display = ('get_name', 'condition', )
    search_fields = ('product__item__name', )

    def get_name(self, obj):
        return obj.product.item.name

    get_name.short_description = 'Name'
    get_name.admin_order_field = 'product__item__name'


admin.site.register(Robot, RobotAdmin)
admin.site.register(RobotPart, RobotPartAdmin)
