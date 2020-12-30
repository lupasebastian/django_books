"""views to be used in api app"""
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from catalog.models import Book, Author

from .serializers import BookSerializer, AuthorSerializer, MiniBookSerializer


# pylint: disable=too-many-ancestors, no-member, unused-argument


class BookViewSet(ModelViewSet):
    """view for a serialized rest representation of a Book object"""
    queryset = Book.objects.all()
    serializer_class = MiniBookSerializer

    def list(self, request, *args, **kwargs):
        """
        method returning a list of Book object
        representations with limited fields
        """
        serializer = MiniBookSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        """method returning Book object representation with all the fields"""
        book = self.get_object()
        serializer = BookSerializer(book)
        return Response(serializer.data)


class AuthorViewSet(ModelViewSet):
    """view for a serialized rest representation of an Author object"""
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def list(self, request, *args, **kwargs):
        """
        method returning a list of Author object
        representation with all the fields
        """
        serializer = AuthorSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        """method returning Author object representation with all the fields"""
        author = self.get_object()
        serializer = AuthorSerializer(author)
        return Response(serializer.data)
