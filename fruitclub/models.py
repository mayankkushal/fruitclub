from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User, related_name="profile")
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	picture = models.ImageField(default='empty-user-photo.png', upload_to='profile_pictures')
	mobile = models.IntegerField(null=True)

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

class Category(models.Model):
	name = models.CharField(max_length=300)
	description = models.CharField(max_length=500)
	slug = models.SlugField()

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'Categories'

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.name)

		super(Category, self).save(*args, **kwargs)
	
class Company(models.Model):
    name = models.CharField(max_length=300)
    slug = models.SlugField()

    def __str__(self):
    	return self.name

    class Meta:
    	verbose_name_plural = 'Companies'

    def save(self, *args, **kwargs):
    	if not self.id:
    		self.slug = slugify(self.name)
    	super(Company, self).save(*args, **kwargs)


class Product(models.Model):
	category = models.ForeignKey(Category, related_name='category')
	name = models.CharField(max_length=300)
	company = models.ForeignKey(Company, related_name="company")
	description = models.CharField(max_length=500)
	date = models.DateTimeField(auto_now_add=True)
	price = models.DecimalField(default=0, max_digits=7, decimal_places=2)
	slug = models.SlugField()

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.name)
		super(Product, self).save(*args, **kwargs)

    
class ProductImage(models.Model):
	product = models.ForeignKey(Product, related_name='images')
	image = models.ImageField(null=True, upload_to='product_images')
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.product.name

class Cart(models.Model):
	user = models.ForeignKey(User)
	product = models.ForeignKey(Product)
	quantity = models.IntegerField(default=0)

	def __str__(self):
		return self.product.name



