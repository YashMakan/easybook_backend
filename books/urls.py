from django.urls import path
from books import views as books_views

urlpatterns = [
    path('trending-books/', books_views.trending_books, name='Trending Books'),
]