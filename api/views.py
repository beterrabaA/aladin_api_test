from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema, OpenApiResponse, OpenApiExample
import requests

API_URL = "https://testedefensoriapr.pythonanywhere.com/precos"

@extend_schema(
    summary="Example endpoint",
    description="This endpoint does something specific.",
    examples=[OpenApiExample(
        summary="Example response",
        description="An example of the expected response format.",
        value={
            "date": "2024-01-01",
            "data": [
                {"id": 1, "name": "Item 1"},
                {"id": 2, "name": "Item 2"}
            ]
        }
    )],  
    responses={200: OpenApiResponse(description="Successful response with data",response={
        'type': 'object',
        'properties': {
            'date': {'type': 'string', 'format': 'date'},
            'data': {'type': 'array', 'items': {'type': 'object'}}
        }
    })}
)
def items(request):
    response = requests.get(API_URL)
    date = request.GET.get("date")
    if response.status_code == 200:
        data =  {
            'date': date,
            'data': response.json(),
        }
        return JsonResponse(data)
    else:
        return JsonResponse({'error': 'Failed to fetch data from the API'}, status=response.status_code)