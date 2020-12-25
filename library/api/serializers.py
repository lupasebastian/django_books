from rest_framework.serializers import ModelSerializer
from catalog.models import Book, Author


class AuthorSerializer(ModelSerializer):

    class Meta:
        model = Author
        fields = ('id', 'name')


class BookSerializer(ModelSerializer):

    author = AuthorSerializer()

    class Meta:
        model = Book
        fields = ('id', 'title', 'genre', 'rating', 'author', 'issue_date', 'description')


class MiniBookSerializer(ModelSerializer):

    author = AuthorSerializer()

    class Meta:
        model = Book
        fields = ('id', 'title', 'author')
