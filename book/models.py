from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=30)
    author = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='')
    release_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

class BookComment(models.Model):
    books = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="book_comment")
    text = models.TextField()
    created_date = models.DateField(auto_now_add=True)

def __str__(self):
    return f'{self.name}'

class Expert(models.Model):
    EXPERT_CHOICE = (
        ('EXEMINATION OF EDUCATIONAL PROJECTS', 'EXEMINATION OF EDUCATIONAL PROJECTS'),
        ('experemential work', 'experemential work'),
        ('adout education development programs', 'adout education development programs'),
        ('legal documents', 'legal documents'),
    )
    education = models.CharField(max_length=35)
    projects = models.IntegerField()
    nameEX = models.TextField()
    expert = models.CharField(choices=EXPERT_CHOICE, max_length=150)

def __str__(self):
    return f'{self.nameEX}'