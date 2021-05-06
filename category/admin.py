from django.contrib import admin
from.models import CategoryModel

# Register your models here.


@admin.register(CategoryModel)
class CatAdmin(admin.ModelAdmin):
	list_display = ['categry', 'image_tag']


