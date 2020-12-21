from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy

from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from .models import Book


class BooksView(ListView):
    template_name = 'books_view.html'
    model = Book
    paginate_by = 5

    def get_paginate_by(self, queryset):
        return self.request.GET.get("paginate_by", self.paginate_by)


class BookDetailView(DetailView):
    template_name = 'book_detail.html'
    model = Book


class BookCreateView(CreateView):
    template_name = 'form.html'
    model = Book
    fields = '__all__'
    success_url = reverse_lazy('books')


class BookUpdateView(UpdateView):
    template_name = 'form.html'
    model = Book
    fields = '__all__'
    success_url = reverse_lazy('books')


class BookDeleteView(DeleteView):
    template_name = 'book_delete.html'
    model = Book
    success_url = reverse_lazy('books')


