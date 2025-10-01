from django.urls import path, include
from rest_framework import routers

from book_api.books.views.books import BookViewSet

app_name = "books"

router = routers.SimpleRouter()
router.register(r"books", BookViewSet, basename="books")

urlpatterns = [
    path("", include(router.urls)),
]