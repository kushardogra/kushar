from django.db import models
from datetime import datetime
# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=200, null=True)
    username= models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.username if self.username else ''

class diary(models.Model):
    diary_id= models.CharField(auto_created=5, null=True, max_length=5)
    diary_name = models.CharField(max_length=500, null=True)
    content= models.CharField(max_length=10000, null=True)
    photo = models.FileField(max_length=10000, null=True)
    Date = models.DateTimeField(default=datetime.now, null=True)
    def __str__(self):
        return self.diary_id if self.diary_id else ''

