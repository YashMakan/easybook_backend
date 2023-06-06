from django.http import JsonResponse
import json


class Book:
    def __init__(self, kind, book_id, etag, self_link, volume_info, sales_info, access_info, search_info):
        self.kind = kind
        self.book_id = book_id
        self.etag = etag
        self.self_link = self_link
        self.volume_info = volume_info
        self.sales_info = sales_info
        self.access_info = access_info
        self.search_info = search_info

    def serialize(self):
        return {
            'kind': self.kind,
            'id': self.book_id,
            'etag': self.etag,
            'selfLink': self.self_link,
            'volumeInfo': self.volume_info,
            'salesInfo': self.sales_info,
            'accessInfo': self.access_info,
            'searchInfo': self.search_info
        }

    @classmethod
    def from_json(cls, data: dict):
        return cls(
            data.get('kind'),
            data.get('id'),
            data.get('etag'),
            data.get('selfLink'),
            data.get('volumeInfo'),
            data.get('saleInfo'),
            data.get('accessInfo'),
            data.get('searchInfo')
        )

    @staticmethod
    def list_to_json_response(books):
        serialized_books = [book.serialize() for book in books]
        response_data = {
            'error': False,
            'count': len(books),
            'result': serialized_books
        }
        return response_data
