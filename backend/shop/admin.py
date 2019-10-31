from django.contrib import admin

from .models import Shop  # add this


class ShopAdmin(admin.ModelAdmin):  # add this
    list_display = ('name', 'address', 'category')  # add this


# Register your models here.
admin.site.register(Shop, ShopAdmin)  # add this
