from django.conf.urls import url
from blog import views

app_name = 'blog'
urlpatterns = [
	url(r'^index', views.index, name='index' ),
	url(r'^article/(?P<article_slug>[\w\-]+)', views.article, name="article"),
	url(r'^add_comment', views.add_comment, name="add_comment")
]