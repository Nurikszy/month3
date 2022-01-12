from django.db import models

# Create your models here.
class TVShow(models.Model):
    GANRE_CHOICE = (
        ('Detective', 'Detective'),
        ('Comedy', 'Comedy'),
        ('Drama', 'Drama'),
        ('Horror', 'Horror'),
        ('Romantic', 'Romantic'),
        ('Anime', 'Anime')
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='')
    quantity = models.IntegerField()
    ganre = models.CharField(choices=GANRE_CHOICE, max_length=100)
    date_filmed = models.DateField()
