from django.db import models

# Create your models here.

class Contact(models.Model):    #Contact eta database er nam
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=30)
    subject=models.TextField()
    message=models.TextField()