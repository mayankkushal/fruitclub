from django.contrib import admin
from fruitclub.models import Profile, SlideShowImage, ImageGroup, Category, Product, Company, ProductImage, Cart
# Register your models here.

admin.site.register(Profile)
admin.site.register(SlideShowImage)
admin.site.register(ImageGroup)
admin.site.register(Company)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Cart)