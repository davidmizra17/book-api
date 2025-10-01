import re

from rest_framework import serializers

from book_api.books.models import Book


class BookModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        exclude = ['created', 'modified']

    def validate_cost_usd(self, value):
        if value <= 0:
            raise serializers.ValidationError("cost_usd must be greater than 0.")
        return value

    def validate_stock_quantity(self, value):
        if value < 0:
            raise serializers.ValidationError("stock_quantity cannot be negative.")
        return value

    def validate_isbn(self, value):
        if not re.match(r'^\d{3}-\d{1,5}-\d{1,7}-\d{1,7}-\d{1}$', value) and len(value) not in [10, 13]:
            raise serializers.ValidationError("ISBN must be valid (10 or 13 digits).")
        return value