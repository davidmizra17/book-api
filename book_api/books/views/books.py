from datetime import datetime

from django.http import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter

from book_api.books.models import Book
from book_api.books.serializers.books import BookModelSerializer
from book_api.external_apis.exchange_rates.api_caller import get_exchange_rates


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer
    filter_backends = (SearchFilter, DjangoFilterBackend)
    search_fields = ("category",)


    @action(detail=True, methods=["post"], url_path="calculate-price")
    def calculate_price(self, request, pk=None):
        book = self.get_object()
        exchange_rates = get_exchange_rates()
        ves_rate: float
        if exchange_rates is None:
            ves_rate = 180.00
        ves_rate = exchange_rates[0]['rates']['VES']

        cost_local = float(ves_rate) * float(book.cost_usd)

        book.selling_price_local = cost_local * 1.40
        book.save()

        calculation_timestamp = datetime.utcnow().isoformat() + 'Z'

        response_data = {
            "book_id": book.id,
            "cost_usd": str(book.cost_usd),
            "exchange_rate": str(ves_rate),
            "cost_local": cost_local,
            "margin_percentage": 40,
            "selling_price_local": book.selling_price_local,
            "currency": "VES",
            "calculation_timestamp": calculation_timestamp
        }

        return Response(response_data, status=status.HTTP_200_OK)
