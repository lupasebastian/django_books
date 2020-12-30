"""module defining serializers to be used in api app"""
from rest_framework.serializers import ModelSerializer
from catalog.models import Book, Author


# pylint: disable=too-few-public-methods


class AuthorSerializer(ModelSerializer):
    """class for serializing Author objects"""

    class Meta:
        """class defining fields to be used in serializer"""
        model = Author
        fields = ('id', 'name')


class BookSerializer(ModelSerializer):
    """class for serializing Book objects"""

    author = AuthorSerializer()

    class Meta:
        """class defining fields to be used in serializer"""
        model = Book
        fields = ('id', 'title', 'genre', 'rating', 'author', 'issue_date', 'description')


class MiniBookSerializer(ModelSerializer):
    """class for serializing Book objects with limited fields"""

    author = AuthorSerializer()

    class Meta:
        """class defining fields to be used in serializer"""
        model = Book
        fields = ('id', 'title', 'author')
