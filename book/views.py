from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from . import models, forms
from django.urls import reverse
from django.views import generic




class BooksListView(generic.ListView):
    template_name = "book_list.html"
    queryset = models.Book.objects.all()

    def get_queryset(self):
        return models.Book.objects.filter().order_by("-id")
# def book_all(request):
#     books = models.Book.objects.all()
#     return render(request, 'book_list.html',
#                   {'books': books})



class BookDetailView(generic.DetailView):
    template_name = "books_details.html"

    def get_object(self, **kwargs):
        books_idc = self.kwargs.get("id")
        return get_object_or_404(models.Book, id=books_id)
# def books_detail(request, id):
#     book = get_object_or_404(models.Book, id=id)
#     return render(request, 'books_details.html',
#                   {'book': book})


# def add_book(request):
#     method = request.method
#     if method == 'POST':
#         form = forms.BookForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Вы успешно изменили пост!')
#     else:
#         form = forms.BookForm()
#     return render(request, 'add_books.html', {'form': form})



class BookUpdateView(generic.UpdateView):
    template_name = "show_update.html"
    form_class = forms.BookForm
    success_url = "/books/"


    def get_object(self, *kwargs):
        books_id = self.kwargs.get("id")
        return get_object_or_404(models.Book, id=books_id)

    def form_valid(self, form):
        return super(BookUpdateView, self).form_valid(form=form)

class BookCreateView(generic.CreateView):
    template_name = "add_books.html"
    form_class = forms.BookForm
    queryset = models.Book.objects.all()
    success = "/books/"

    def form_valid(self, form):
        return super(BookCreateView, self).form_valid(form=form)
# def book_update(request, id):
#     book_object = get_object_or_404(models.Book, id=id)
#     if request.method == 'POST':
#         form = forms.BookForm(instance=book_object, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse("books:books_all"))
#     else:
#         form = forms.BookForm(instance=book_object)
#     return render(request, 'book_update.html', {'form': form,'object': book_object})


class BookDeleteVies(generic.DeleteView):
    template_name = "confirm_delete.html"
    success_url = '/books/'


    def get_object(self, **kwargs):
        books_id = self.kwargs.get("id")
        return get_object_or_404(models.Book, id=books_id)
#
# def book_delete(request, id):
#     book_object = get_object_or_404(models.Book, id=id)
#     book_object.delete()
#     return HttpResponse('Удалено.')


