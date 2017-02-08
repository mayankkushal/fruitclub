from django.conf.urls import url
from fruitclub import views

urlpatterns = [
	url(r'^$', views.index, name="index"),
	url(r'^profile_page', views.profile_page, name='profile_page'),
	url(r'^profile', views.profile, name='profile')
]