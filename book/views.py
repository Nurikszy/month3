from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from . import models, forms
from django.urls import reverse


def book_all(request):
    books = models.Book.objects.all()
    return render(request, 'book_list.html',
                  {'books': books})


def books_detail(request, id):
    book = get_object_or_404(models.Book, id=id)
    return render(request, 'books_details.html',
                  {'book': book})


def add_book(request):
    method = request.method
    if method == 'POST':
        form = forms.BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Вы успешно изменили пост!')
    else:
        form = forms.BookForm()
    return render(request, 'add_books.html', {'form': form})

def book_update(request, id):
    book_object = get_object_or_404(models.Book, id=id)
    if request.method == 'POST':
        form = forms.BookForm(instance=book_object, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("books:books_all"))
    else:
        form = forms.BookForm(instance=book_object)
    return render(request, 'book_update.html', {'form': form,'object': book_object})

def book_delete(request, id):
    book_object = get_object_or_404(models.Book, id=id)
    book_object.delete()
    return HttpResponse('Удалено.')
