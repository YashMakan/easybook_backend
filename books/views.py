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
    isbn = request.data.get('isbn')
    start_index = request.data.get('startIndex')
    scraper = BookScraper()
    if book_name:
        data = scraper.search_book(book_name,  start_index)
        return JsonResponse(data)
    elif isbn:
        data = scraper.search_book_by_isbn(isbn)
        return JsonResponse(data)


@api_view(['GET'])
def weekly_trending_book(_):
    isbn = "0984782850"
    scraper = BookScraper()
    data = scraper.search_book_by_isbn(isbn)
    return JsonResponse(data)


# you might like books endpoint
def you_might_like_books(_):
    scraper = BookScraper()
    data = scraper.you_might_like_books()
    return JsonResponse(data)