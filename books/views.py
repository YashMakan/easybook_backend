from rest_framework.decorators import api_view
from books.books_scrapper import BookScraper
from django.http import JsonResponse


@api_view(['GET'])
def trending_books(_):
    scraper = BookScraper()
    data = scraper.get_trending_books()
    return JsonResponse(data)


@api_view(['POST'])
def search_books(request):
    book_name = request.data.get('search')
    scraper = BookScraper()
    data = scraper.search_book(book_name)
    return JsonResponse(data)
