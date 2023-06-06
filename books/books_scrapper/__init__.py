from typing import List

import requests
import json
from books.models import Book
from django.http import JsonResponse
import dotenv


class BookScraper:
    def __init__(self):
        dotenv.load_dotenv()
        self.base_url = "https://www.googleapis.com/books/v1/"
        self.api_key = dotenv.get_key("GOOGLE_BOOKS_API_KEY")

    # get trending books
    def get_trending_books(self):
        url = self.base_url + "volumes?q=trending&key=" + self.api_key
        response = requests.get(url)
        books = [Book.from_json(book) for book in response.json()['items']]
        return Book.list_to_json_response(books)

    # search book by name
    def search_book(self, name: str) -> List[Book]:
        url = self.base_url + "volumes?q=" + name + "&key=" + self.api_key
        response = requests.get(url)
        books = [Book.from_json(book) for book in response.json()['items']]
        return Book.list_to_json_response(books)
