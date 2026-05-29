from rest_framework.test import APITestCase
from unittest.mock import patch

class ItemsEndpointTestCase(APITestCase):

    @patch('api.views.requests.get')
    def test_items_success(self, mock_get):
        # 1. Configurar o mock para simular um retorno 200 da API externa
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [
            {"id": 1, "name": "Item 1"},
            {"id": 2, "name": "Item 2"}
        ]
        
        # 2. Fazer a requisição GET no endpoint passando um parâmetro de query
        url = '/api/v1/items/'
        response = self.client.get(url, {'date': '28-05-2026'})
        
        # 3. Asserções (validações)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['date'], '28-05-2026')
        
        self.assertIsInstance(response.data['data'], list)
        self.assertEqual(len(response.data['data']), 2)
        self.assertEqual(response.data['data'][0]['name'], 'Item 1')

        mock_get.assert_called_once_with("https://testedefensoriapr.pythonanywhere.com/precos")

    @patch('api.views.requests.get')
    def test_items_external_api_failure(self, mock_get):
        # 1. Configurar o mock para simular falha na API externa
        mock_get.return_value.status_code = 500
        
        # 2. Fazer a requisição
        url = '/api/v1/items/'
        response = self.client.get(url, {'date': '28-05-2026'})
        
        # 3. Validações
        self.assertEqual(response.status_code, 500) 
        self.assertEqual(response.data['error'], 'Failed to fetch data from the API')
        
    def test_items_missing_date_parameter(self):
        url = '/api/v1/items/'
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data['error'], "The 'date' parameter is required.")
