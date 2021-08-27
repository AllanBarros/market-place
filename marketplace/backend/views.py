from rest_framework import generics, permissions, viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from .serializers import CarrinhoCompletoSerializer, ProdutoSerializer, ProdutoCarrinhoSerializer, FinalizarSerializer
from .models import Produto, ProdutoCarrinho, Carrinho

class ProdutoView(generics.ListAPIView):
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

class CarrinhoView(viewsets.ModelViewSet):
    queryset           = ProdutoCarrinho.objects.all()
    serializer_class   = ProdutoCarrinhoSerializer
    permission_classes = [permissions.AllowAny]

    def retrieve(self, request, *args, **kwargs):
        carrinho_id = request.query_params['id_carrinho']
        try:
            resultado = CarrinhoCompletoSerializer(Carrinho.objects.get(id=carrinho_id))
        except:
            return Response(data={'detail':'Carrinho não encontrado'}, status=status.HTTP_400_BAD_REQUEST)    
        return Response(data=resultado.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):

        carrinho_id = request.data.get('id_carrinho', None)

        if not carrinho_id:
            carrinho_id = Carrinho()
            carrinho_id.save()
        else:
            carrinho_id = Carrinho.objects.get(id=carrinho_id)

        carrinho = ProdutoCarrinho()
        carrinho.id_carrinho = carrinho_id
        carrinho.id_produto = Produto.objects.get(id=request.data['id_produto'])
        carrinho.quantidade_produto = request.data['quantidade_produto']

        if not (carrinho.quantidade_produto % carrinho.id_produto.amount_per_package == 0):
            return Response(data={'detail':'Quantidade selecionada não está de acordo com quantidade por pacote'},status=status.HTTP_400_BAD_REQUEST)
        if carrinho.quantidade_produto > carrinho.id_produto.max_availability:
            return Response(data={'detail':'Quantidade acima da encontrada em estoque.'},status=status.HTTP_400_BAD_REQUEST)
        
        carrinho.save()
        resultado = ProdutoCarrinhoSerializer(carrinho)   
        return Response(data=resultado.data,status=status.HTTP_200_OK)

    def partial_update(self, request, *args, **kwargs):
        carrinho_id = request.data['id_produto_carrinho']
        produto_id = request.data['id_produto']
        carrinho = ProdutoCarrinho.objects.get(id=carrinho_id, id_produto=produto_id)
        carrinho.quantidade_produto = request.data['quantidade_produto']

        if carrinho.quantidade_produto % carrinho.id_produto.amount_per_package != 0:
            return Response(data={'detail':'Quantidade selecionada não está de acordo com quantidade por pacote'},status=status.HTTP_400_BAD_REQUEST)
        if carrinho.quantidade_produto > carrinho.id_produto.max_availability:
            return Response(data={'detail':'Quantidade acima da encontrada em estoque.'},status=status.HTTP_400_BAD_REQUEST)
        
        carrinho.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, *args, **kwargs):
        try:
            carrinho_id = request.data['id_carrinho']
            produto_id = request.data['id_produto']
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)    

        ProdutoCarrinho.objects.get(id_carrinho=carrinho_id, id_produto = produto_id).delete()
        return Response(status=status.HTTP_200_OK)


class FinalizarCarrinhoView(APIView):
    permission_classes = [permissions.AllowAny]
    renderer_classes = [JSONRenderer]

    def post(self, request):
        id_carrinho = request.data.get('id_carrinho', None)
        carrinho = Carrinho.objects.get(id=id_carrinho)
        resultado = FinalizarSerializer(carrinho)

        if resultado.is_valid():
            return Response(data=resultado.data, status=status.HTTP_200_OK)
        
        return Response(data=resultado.errors)
            
        
