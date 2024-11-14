from rest_framework import viewsets
from .models import Author, Publisher, Book  # Используйте фактические имена моделей
from .serializers import AuthorSerializer, PublisherSerializer, BookSerializer
from rest_framework.permissions import IsAuthenticated

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated]  # Доступ только для авторизованных

class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    permission_classes = [IsAuthenticated]  # Доступ только для авторизованных

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Доступ только для авторизованных