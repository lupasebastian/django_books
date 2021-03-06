"""urls dispatcher for catalog app"""
from django.urls import path

from .views import BooksView, BookCreateView, BookDetailView, BookUpdateView, \
    BookDeleteView, AuthorCreateView

urlpatterns = [
    path('ksiazki/', BooksView.as_view(),
         name='books'),
    path('nowa/', BookCreateView.as_view(),
         name='book-create-view'),
    path('ksiazki/<int:pk>/', BookDetailView.as_view(),
         name='book-detail-view'),
    path('ksiazki/edytuj/<int:pk>/', BookUpdateView.as_view(),
         name='book-update-view'),
    path('ksiazki/usun/<int:pk>/', BookDeleteView.as_view(),
         name='book-delete-view'),
    path('autor/nowy', AuthorCreateView.as_view(),
         name='author-create-view'),
]
