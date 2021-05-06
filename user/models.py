from django.db import models
import secrets

# Create your models here.


class User(models.Model):
	fname = models.CharField(max_length=15)
	lname = models.CharField(max_length=15)
	area = models.CharField(max_length=10, blank=True, null=True)
	address = models.CharField(max_length=25, blank=True, null=True)
	state = models.CharField(max_length=10, blank=True, null=True)
	city = models.CharField(max_length=15, blank=True, null=True)
	zip = models.CharField(max_length=10, blank=True, null=True)
	mobile = models.CharField(max_length=12)
	email = models.EmailField(blank=True, null=True)
	password = models.CharField(max_length=33)
	reset_code = models.IntegerField(blank=True, null=True)
	token = models.CharField(max_length=20, editable=False, default=secrets.token_hex(10))
	dob = models.CharField(max_length=13, blank=True, null=True)

	def __str__(self):
		return self.email








