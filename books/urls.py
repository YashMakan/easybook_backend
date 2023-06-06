from django.urls import path
from books import views as books_views

urlpatterns = [
    # Get the list of trending books
    path('trending-books', books_views.trending_books, name='Trending Books'),

    # search books
    path('search-books', books_views.search_books, name='Search Books'),
]