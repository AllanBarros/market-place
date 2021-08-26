from rest_framework import generics, permissions, viewsets, status
from rest_framework.response import Response
from .serializers import ProdutoSerializer, ProdutoCarrinhoSerializer
from .models import Produto, ProdutoCarrinho, Carrinho

class ProdutoView(generics.ListAPIView):
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

class CarrinhoView(viewsets.ModelViewSet):
    queryset           = ProdutoCarrinho.objects.all()
    serializer_class   = ProdutoCarrinhoSerializer
    permission_classes = [permissions.AllowAny]

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

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
        carrinho.save()
        resultado = ProdutoCarrinhoSerializer(carrinho)   
        return Response(data=resultado.data,status=status.HTTP_200_OK)


    def partial_update(self, request, *args, **kwargs):
        carrinho_id = request.data['id_carrinho']
        produto_id = request.data['id_produto']
        carrinho = ProdutoCarrinho.objects.get(id_carrinho=carrinho_id, id_produto = produto_id)

        carrinho.quantidade_produto = request.data['quantidade_produto']
        carrinho.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, *args, **kwargs):
        carrinho_id = request.data['id_carrinho']
        produto_id = request.data['id_produto']
        carrinho = ProdutoCarrinho.objects.get(id_carrinho=carrinho_id, id_produto = produto_id).delete()
        return Response(status=status.HTTP_200_OK)

