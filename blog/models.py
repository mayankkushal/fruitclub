from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.
class Article(models.Model):
	name = models.CharField(max_length=200)
	description = models.CharField(max_length=500)
	content = models.TextField(null=False)
	date_created = models.DateTimeField(auto_now_add=True)
	slug = models.SlugField()
	comments = models.IntegerField(default=0)

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.name)

		super(Article, self).save(*args, **kwargs)


class Images(models.Model):
	article = models.ForeignKey(Article, related_name='images')
	picture = models.ImageField(upload_to="blog_images", null=False)

	def __str__(self):
		return self.article.name

class Comment(models.Model):
	poster = models.ForeignKey(User)
	article = models.ForeignKey(Article)
	time = models.DateTimeField(auto_now_add=True)
	comment = models.CharField(max_length=124)

	def __str__(self):
		return self.poster.username
