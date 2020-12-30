"""module defining views to be used by catalog app"""
from django.contrib.auth.mixins import UserPassesTestMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from .models import Book, Author


# pylint: disable=too-many-ancestors


class StaffRequiredMixin(UserPassesTestMixin):
    """overridden method testing if user is in staff group"""
    def test_func(self):
        return self.request.user.is_staff


class BooksView(ListView):
    """view for listing Book objects"""
    template_name = 'books_view.html'
    model = Book
    paginate_by = 5

    def get_paginate_by(self, queryset):
        """sets pagination for BooksView"""
        return self.request.GET.get("paginate_by", self.paginate_by)


class BookDetailView(DetailView):
    """view for showing details of a particular book"""
    template_name = 'book_detail.html'
    model = Book


class BookCreateView(PermissionRequiredMixin, CreateView):
    """view for creating Book objects"""
    template_name = 'form_author.html'
    model = Book
    fields = '__all__'
    success_url = reverse_lazy('books')
    permission_required = 'catalog.add_book'


class BookUpdateView(StaffRequiredMixin, PermissionRequiredMixin, UpdateView):
    """view for updating Book objects"""
    template_name = 'form.html'
    model = Book
    fields = '__all__'
    success_url = reverse_lazy('books')
    permission_required = 'catalog.change_book'


class BookDeleteView(StaffRequiredMixin, PermissionRequiredMixin, DeleteView):
    """view for deleting Book objects"""
    template_name = 'book_delete.html'
    model = Book
    success_url = reverse_lazy('books')
    permission_required = 'catalog.delete_book'


class AuthorCreateView(PermissionRequiredMixin, CreateView):
    """view for creating Author objects"""
    template_name = 'form.html'
    model = Author
    success_url = reverse_lazy('book-create-view')
    fields = '__all__'
    permission_required = 'catalog.add_author'
