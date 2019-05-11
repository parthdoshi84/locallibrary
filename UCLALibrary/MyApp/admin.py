from django.contrib import admin

# Register your models here.
from MyApp.models import Author, Type, Book, Publisher

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Type)
admin.site.register(Publisher)