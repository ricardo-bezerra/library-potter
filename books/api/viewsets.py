from rest_framework import viewsets
from books.api import serializers
from books import models


class BookViewset(viewsets.ModelViewSet):
    serializer_class = serializers.BookSerializer
    queryset = models.Books.objects.all()
