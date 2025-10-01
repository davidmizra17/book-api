from rest_framework import serializers

from book_api.books.models import Book


class BookModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        exclude = ['created', 'modified']