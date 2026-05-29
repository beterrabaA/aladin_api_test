from django.http import JsonResponse
import requests

API_URL = "https://testedefensoriapr.pythonanywhere.com/precos"

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