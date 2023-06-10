from django.urls import path
from books import views as books_views

urlpatterns = [
    # Get the list of trending books
    path('trending-books', books_views.trending_books, name='Trending Books'),

    # search books
    path('search-books', books_views.search_books, name='Search Books'),

    # weekly trending books
    path('weekly-trending-books', books_views.weekly_trending_book, name='Weekly Trending Books'),

    # you might like books
    path('you-might-like-books', books_views.you_might_like_books, name='You Might Like Books'),
]