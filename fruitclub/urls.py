from django.conf.urls import url
from fruitclub import views

urlpatterns = [
	url(r'^$', views.index, name="index"),
	url(r'^profile_page', views.profile_page, name='profile_page'),
	url(r'^profile', views.profile, name='profile'),
	url(r'^add_cart', views.add_cart, name='add_cart'),
	url(r'^product/(?P<product_slug>[\w\-]+)', views.single_product, name='single_product'),
	url(r'^cart', views.cart, name='cart'),
	url(r'^remove_item', views.remove_item, name='remove_item'),
	url(r'^change', views.change_qty, name="change_qty"),
	url(r'^about', views.about, name='about'),
	url(r'^category/(?P<category_slug>[\w\-]+)', views.category, name='category'),
	url(r'^checkout', views.checkout, name="checkout")
]