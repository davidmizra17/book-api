from rest_framework import viewsets

from book_api.books.models import Book
from book_api.books.serializers.books import BookModelSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer