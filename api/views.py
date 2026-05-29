from django.http import HttpResponse
import requests


def items(request):
    response = requests.get("https://testedefensoriapr.pythonanywhere.com/precos")
    return HttpResponse(response.content, content_type="application/json")