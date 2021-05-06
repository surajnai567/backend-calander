from django.db import models
from category.models import CategoryModel
from cloudinary.models import CloudinaryField
from django.utils.html import mark_safe

# Create your models here.


class Product(models.Model):
	name = models.CharField(max_length=20)
	category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
	description = models.CharField(max_length=50)
	attribute = models.CharField(max_length=20)
	currency = models.CharField(max_length=5, default='Rs.')
	discount = models.IntegerField(default=0)
	price = models.IntegerField()
	#image = models.ImageField()
	image = CloudinaryField('image')
	homepage = models.BooleanField(default=False)
	is_new = models.BooleanField(default=False)

	def image_tag(self):
		return mark_safe('<img src="%s" width="150" height="150" />' % (self.image.url))
	image_tag.short_description = 'Image'

	def __str__(self):
		return self.name


