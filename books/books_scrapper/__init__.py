import os
from typing import List
import requests
from books.models import Book
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / '.env')


class BookScraper:
    def __init__(self):
        self.base_url = "https://www.googleapis.com/books/v1/"
        self.api_key = os.getenv("GOOGLE_BOOKS_API_KEY")

    # get trending books
    def get_trending_books(self):
        url = self.base_url + "volumes?q=coding&key=" + self.api_key
        response = requests.get(url)
        books = [Book.from_json(book) for book in response.json()['items']]
        return Book.list_to_json_response(books)

    # search book by name
    def search_book(self, name: str) -> List[Book]:
        url = self.base_url + "volumes?q=" + name + "&key=" + self.api_key
        response = requests.get(url)
        books = [Book.from_json(book) for book in response.json()['items']]
        return Book.list_to_json_response(books)

    # get book by isbn
    def search_book_by_isbn(self, isbn: str) -> List[Book]:
        url = self.base_url + "volumes?q=" + "" + "+isbn:" + isbn + "&key=" + self.api_key
        response = requests.get(url)
        books = [Book.from_json(book) for book in response.json()['items']]
        return Book.list_to_json_response(books)
