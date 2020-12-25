from django.shortcuts import render
from .serializers import BookSerializer, AuthorSerializer, MiniBookSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from catalog.models import Book, Author


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = MiniBookSerializer

    def list(self, request, *args, **kwargs):
        serializer = MiniBookSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        book = self.get_object()
        serializer = BookSerializer(book)
        return Response(serializer.data)


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def list(self, request, *args, **kwargs):
        serializer = AuthorSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        author = self.get_object()
        serializer = AuthorSerializer(author)
        return Response(serializer.data)