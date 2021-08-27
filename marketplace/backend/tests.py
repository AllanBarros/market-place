from rest_framework.test import APITestCase,APIClient
from django.urls import reverse
from .models import *
from .views import *

class MarketPlaceTestCase(APITestCase):
    
    fixtures=['produtos_testes.json']

    def test_buscar(self):
        valor_1 = 'Racao'
        url = reverse('buscar') + '?name=' + valor_1 
        print(url)
        client = APIClient()
        response = client.get(url,  format='json')

        self.assertEqual(response.status_code, 200)
    
    def test_buscar_vazio(self):
        valor_1 = ''
        url = reverse('buscar') + '?name=' + valor_1 
        client = APIClient()
        response = client.get(url,  format='json')

        self.assertEqual(response.status_code, 200)
        # self.assertEqual(len(response.data), 0)

    def test_adicionar(self):
        url = reverse('adicionar')
        client = APIClient()
        dados = {"id_produto":1,"quantidade_produto":12}
        response = client.post(url, dados ,format='json')
        self.assertEqual(response.status_code, 200)
    
    def test_adicionar_invalido(self):
        url = reverse('adicionar')
        client = APIClient()
        dados = {"id_produto":1,"quantidade_produto":1}
        response = client.post(url, dados ,format='json')

        self.assertEqual(response.status_code, 400)


    def test_quantidade(self):
        url = reverse('quantidade')
        client = APIClient()
        dados = {"id_produto":1,"id_produto_carrinho": 1,"quantidade_produto":20}
        response = client.patch(url, dados ,format='json')
        self.assertEqual(response.status_code, 204)
    
    def test_quantidade_invalido(self):
        url = reverse('quantidade')
        client = APIClient()
        dados = {"id_produto":1,"id_produto_carrinho": 1,"quantidade_produto":35}
        response = client.patch(url, dados ,format='json')

        self.assertEqual(response.status_code, 400)

    def test_quantidade_max(self):
        url = reverse('quantidade')
        client = APIClient()
        dados = {"id_produto":1,"id_produto_carrinho": 1,"quantidade_produto":50001}
        response = client.patch(url, dados ,format='json')

        self.assertEqual(response.status_code, 400)

    def test_remover(self):
        url = reverse('remover')
        client = APIClient()
        dados = {"id_produto":1,"id_carrinho": 5}
        response = client.delete(url, dados ,format='json')
        self.assertEqual(response.status_code, 200)
    
    def test_remover_invalido(self):
        url = reverse('remover')
        client = APIClient()
        dados = {"id_produto":1}
        response = client.delete(url, dados ,format='json')

        self.assertEqual(response.status_code, 400)

    def test_exibir(self):
        valor_1 = '5'
        url = reverse('exibir') + '?id_carrinho=' + valor_1
        client = APIClient()
        response = client.get(url, format='json')

        self.assertEqual(response.status_code, 200)
    
    def test_exibir_invalido(self):
        valor_1 = '475'
        url = reverse('exibir') + '?id_carrinho=' + valor_1
        client = APIClient()
        response = client.get(url, format='json')

        self.assertEqual(response.status_code, 400)

    
    def test_comprar(self):
        dados = {"id_carrinho": 5}
        url = reverse('comprar')
        client = APIClient()
        response = client.post(url, dados,format='json')

        self.assertEqual(response.status_code, 200)
    
    def test_comprar_invalido(self):
        dados = {"id_carrinho": 6}
        url = reverse('comprar')
        client = APIClient()
        response = client.post(url, dados,format='json')
        self.assertEqual(response.status_code, 400)
