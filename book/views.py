
from django.shortcuts import render, get_object_or_404
from . import models
def book_all(requests):
    book = models.Book.objects.all()
    return render(requests, 'book_list.html', {'book': book})

def books_detail(request, id):
    book = get_object_or_404(models.Book, id=id)
    return render(request, 'books_details.html', {'book': book})