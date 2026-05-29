from django.http import HttpResponse
import requests

API_URL = "https://testedefensoriapr.pythonanywhere.com/precos"

def items(request):
    response = requests.get(API_URL)
    return HttpResponse(response.content, content_type="application/json")