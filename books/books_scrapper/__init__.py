from typing import List

import requests
import json

from books.models import Book

from django.http import JsonResponse


class BookScraper:
    def __init__(self):
        self.base_url = "https://www.googleapis.com/books/v1/"
        self.api_key = "AIzaSyDf82yoe-dtaxS7ZtXq3ZfYv9RuD3MX6hs"

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
