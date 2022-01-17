
from django.urls import path
from . import views
urlpatterns = [
    path('books/', views.book_all, name='books_all'),
    path('books/<int:id>/', views.books_detail, name='books_detail'),
    path('add-books/', views.add_book, name='add-books'),
]