from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=30)
    author = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='')
    release_date = models.DateTimeField(auto_now_add=True)
    post_datepy = models.DateTimeField(auto_now=True)

