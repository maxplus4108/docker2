# Импорт модуля admin из библиотеки Django.contrib
from django.contrib import admin

# Импорт нужных моделей из текущего каталога (".")
from .models import Author, Publisher, Book

# Регистрация моделей для административного сайта
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Book)
