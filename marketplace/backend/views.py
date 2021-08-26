from rest_framework import generics, permissions
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProdutoSerializer, ProdutoCarrinhoSerializer
from .models import Produto, ProdutoCarrinho

class ProdutoView(generics.ListCreateAPIView):
    # queryset           = Produto.objects.all()
    serializer_class   = ProdutoSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        
        try:
            parametro = self.request.query_params['name']
        except:
            parametro = None

        if parametro:
            filtrado = Produto.objects.filter(name__icontains=parametro)
        else:
            filtrado = Produto.objects.all()
        return filtrado

class CarrinhoView(generics.ListCreateAPIView):
    queryset           = ProdutoCarrinho.objects.all()
    serializer_class   = ProdutoCarrinhoSerializer
    permission_classes = [permissions.AllowAny]

