from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User, related_name="profile")
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	picture = models.ImageField(default='empty-user-photo.png')

	def __str__(self):
		return self.first_name

class ImageGroup(models.Model):
	name = models.CharField(max_length=30, default="slideshow")

	def __str__(self):
		return self.name

class SlideShowImage(models.Model):
	slideshow = models.ForeignKey(ImageGroup, related_name="images", default="slideshow")
	picture = models.ImageField(null=False, upload_to='slideshow')
	caption = models.CharField(max_length=256, null=True)
	url = models.URLField()

	def __str__(self):
		return self.url

