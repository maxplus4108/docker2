from rest_framework import serializers
from .models import Author, Publisher, Book

# Сериализатор в Django Rest Framework (DRF) выполняет важную функцию преобразования данных между форматами, удобными для работы внутри программы и для передачи по сети.
# Сериализатор для модели Author
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name']  # Указываем, что хотим включить все поля

# Сериализатор для модели Publisher
class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'  # Включаем все поля модели Publisher

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    publisher = PublisherSerializer()

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'publisher', 'publication_date']

    def create(self, validated_data):
        # Извлекаем данные авторов и издателей
        author_data = validated_data.pop('author')
        publisher_data = validated_data.pop('publisher')

        # Создаем авторов и издателей
        author = Author.objects.create(**author_data)
        publisher = Publisher.objects.create(**publisher_data)

        # Создаем книгу
        book = Book.objects.create(author=author, publisher=publisher, **validated_data)

        return book