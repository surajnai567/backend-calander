from django.db import models
from user.models import User

# Create your models here.


class Event(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.URLField()
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=300)
    location = models.CharField(max_length=300)
    is_private = models.CharField(max_length=6)
    start_date = models.CharField(max_length=12)
    end_date = models.CharField(max_length=12)
    capacity = models.CharField(max_length=10)



