from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def trending_books(request):
    data = {'message': 'Hello, API!'}
    return Response(data)
