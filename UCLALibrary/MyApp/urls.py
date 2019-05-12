from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home_page'),
    #path('books/', views.BookListView.as_view(), name='books'),
    path('books/', views.BookListView, name='books'),

    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
]
