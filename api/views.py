from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, OpenApiResponse, OpenApiExample, OpenApiParameter, OpenApiTypes
import requests

API_URL = "https://testedefensoriapr.pythonanywhere.com/precos"

# O código do endpoint foi interamente elaborado por mim. Foi se utilizado IA para auxiliar na criação da documentação do Swagger, detalhando o endpoint, parâmetros e exemplos de resposta para facilitar a compreensão e uso da API pelos consumidores.
# Um adendo para a documentação do Swagger, detalhando o endpoint, parâmetros e exemplos de resposta para facilitar a compreensão e uso da API pelos consumidores.
# Endpoint para buscar itens com documentação detalhada para o Swagger
@extend_schema(
    summary="Endpoint to fetch items.",
    description="This endpoint fetches items for a specific date from an API and returns the data in a JSON format.",
    parameters=[
        OpenApiParameter(
            name="date", 
            description="The date for which to fetch data", 
            type=OpenApiTypes.DATE,
            location=OpenApiParameter.QUERY, 
            required=True,
            examples=[
                    OpenApiExample(
                        name='Exemplo de Data',
                        value='28-05-2026'
                    )
                ],
        )
    ],
    examples=[OpenApiExample(
        name="Successful Response Example",
        summary="Example of a successful response with data.",
        description="An example of the expected response format.",
        value={
            "date": "28-05-2026",
            "data": [
                {"id": 1, "name": "Item 1"},
                {"id": 2, "name": "Item 2"}
            ]
        }
    )],  
    responses={
        200: OpenApiResponse(
            description="Successful response with data",response={
        'type': 'object',
        'properties': {
            'date': {'type': 'string', 'format': 'date'},
            'data': {'type': 'array', 'items': {'type': 'object'}}
        }
    }),
        400: OpenApiResponse(description="Response with an error message",response={
        'type': 'object',
        'properties': {
            'error': {'type': 'string'}
        },
        'example': {
            'error': 'Failed to fetch data from the API'
        }
    }),
        500: OpenApiResponse(description="Internal server error")
    }
)
@api_view(["GET"])
def items(request):
    date = request.GET.get("date")

    if not date:
        return Response(
            {"error": "The 'date' parameter is required."},
            status=400
        )

    response = requests.get(API_URL)
    if response.status_code == 200:
        data =  {
            'date': date,
            'data': response.json(),
        }
        return Response(data)
    else:
        return Response(
        {"error": "Failed to fetch data from the API"},
        status=response.status_code
    )