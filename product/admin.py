from django.contrib import admin
from product.models import Category, Product, Images


# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product)
admin.site.register(Images)
