from django.contrib import admin

# Register your models here.
from .models import Offer

@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
	list_display = ['name','image_tag']



