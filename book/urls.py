
from django.urls import path
from . import views

app_name = 'books'
urlpatterns = [
    path('books/', views.BooksListView.as_view(), name='books_all'),
    path('books/<int:id>/', views.BookDetailView.as_view(), name='books_detail'),
    path('books/<int:id>/update/', views.BookUpdateView.as_view(), name='books_update'),
    path('books/<int:id>/delete/', views.BookDeleteVies.as_view(), name='books_delete'),
    path('add-books/', views.BookCreateView.as_view(), name='add-books'),
]