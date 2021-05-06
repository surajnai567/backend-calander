from django.db import models
from cloudinary.models import CloudinaryField
from django.utils.html import mark_safe

# Create your models here.
class Offer(models.Model):
    name = models.CharField(max_length=15)
    #url = models.ImageField()
    image = CloudinaryField('image')

    def image_tag(self):
        return mark_safe('<img src="%s" width="150" height="150" />' % (self.image.url))

    image_tag.short_description = 'Image'

