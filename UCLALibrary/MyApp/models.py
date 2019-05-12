from django.db import models
from django.views import generic

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=32)
    middle_name = models.CharField(max_length=32, blank=True)
    last_name = models.CharField(max_length=32)

    def __repr__(self):
        return '<Author {}: {} {} {}>'.format(self.id, self.first_name, self.middle_name, self.last_name)

    def __str__(self):
    	return self.first_name
     

      
class Publisher(models.Model):
    publisher_name = models.CharField(max_length=256)
    publisher_city = models.CharField(max_length = 64, blank=True)

    def __repr__(self):
        return '<Publisher {}: {}>'.format(self.id, self.publisher_name)
 
    def __str__(self):
    	return self.publisher_name
      
class Type(models.Model):
    """Model representing a book genre."""
    type_name = models.CharField(max_length=200, help_text='Enter a book genre (e.g. Science Fiction)')
    
    def __str__(self):
        return self.type_name

class Book(models.Model):
    title = models.CharField(max_length=64)
    volume = models.CharField(max_length=64, blank=True)
    isbn = models.CharField('ISBN',max_length=32, blank=True)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    type_of_book = models.ManyToManyField(Type, help_text='Specify a Type for this book')


    def __repr__(self):
        return '<Book {}: {}>'.format(self.id, self.title)

    def __str__(self):
    	return self.title


 
class BookListView(generic.ListView):
    model = Book
    context_object_name = 'book_list'  

class BookDetailView(generic.DetailView):
    model = Book

