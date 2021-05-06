from django.db import models
from cloudinary.models import CloudinaryField
from django.utils.html import mark_safe

# Create your models here.
class CategoryModel(models.Model):
	categry = models.CharField(max_length=15)
	#cateimg = models.ImageField()
	cateimg = CloudinaryField('image')

	def __str__(self):
		return self.categry

	def image_tag(self):
		return mark_safe('<img src="%s" width="150" height="150" />' % (self.cateimg.url))

	image_tag.short_description = 'Image'


