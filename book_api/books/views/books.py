from datetime import datetime

from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.decorators import action

from book_api.books.models import Book
from book_api.books.serializers.books import BookModelSerializer
from book_api.external_apis.exchange_rates.api_caller import get_exchange_rates


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer

    @action(detail=False, methods=["get"], url_path="search")
    def search(self, request):
        category = self.request.query_params.get("category", None)
        if category:
            books = Book.objects.filter(category=category)
            serializer = self.serializer_class(books, many=True)
            return Response(serializer.data)
        return Response({"error": "Category query parameter is required."}, status=400)

    @action(detail=False, methods=["get"], url_path="low-stock")
    def low_stock(self, request):
        threshold = self.request.query_params.get("threshold", 10)
        try:
            threshold = int(threshold)
        except ValueError:
            return Response({"error": "Threshold must be an integer."}, status=400)

        low_stock_books = self.queryset.filter(
            stock_quantity__lt=threshold)  # Filter books with stock below the threshold
        serializer = self.get_serializer(low_stock_books, many=True)
        return Response(serializer.data)


    @action(detail=True, methods=["post"], url_path="calculate-price")
    def calculate_price(self, request, pk=None):
        book = self.get_object()
        exchange_rates = get_exchange_rates()
        ves_rate = exchange_rates[0]['rates']['VES'] if exchange_rates else 180.00

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
