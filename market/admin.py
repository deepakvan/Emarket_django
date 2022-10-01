from django.contrib import admin
from .models import User,Product,Wish_products,Ordered_products,Product_pictures
# Register your models here.

admin.site.register(User)
admin.site.register(Product)
admin.site.register(Wish_products)
admin.site.register(Ordered_products)
admin.site.register(Product_pictures)
