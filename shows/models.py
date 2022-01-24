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
    date_filmed = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class ShowComment(models.Model):
    shows = models.ForeignKey(TVShow, on_delete=models.CASCADE, related_name="show_comment")
    text = models.TextField(null=True)
    created_date = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.shows.title
