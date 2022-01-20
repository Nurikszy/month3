
from django.urls import path
from . import views

app_name = 'books'
urlpatterns = [
    path('books/', views.book_all, name='books_all'),
    path('books/<int:id>/', views.books_detail, name='books_detail'),
    path('books/<int:id>/update/', views.book_update, name='books_update'),
    path('books/<int:id>/delete/', views.book_delete, name='books_delete'),
    path('add-books/', views.add_book, name='add-books'),
]