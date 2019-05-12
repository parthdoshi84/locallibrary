from django.shortcuts import render

# Create your views here.
from MyApp.models import Book, Author, Publisher, Type, BookListView, BookDetailView
from django.contrib.auth.decorators import login_required


def home(request):
    
    book_count = Book.objects.all().count()
    
       
    author_count = Author.objects.count()
    
    publisher_count = Publisher.objects.count()


    context = {
        'book_count': book_count,
        'author_count': author_count,
        'publisher_count': publisher_count,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'home.html', context=context)

@login_required
def BookListView(request):

    book_list = Book.objects.all() 
    context = {
        'book_list': book_list,
    }
    return render(request, 'book_list.html', context=context)