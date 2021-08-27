from django.core.exceptions import ValidationError
from rest_framework import serializers
from .models import *

class ProdutoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Produto
        fields = '__all__'


class ProdutoCarrinhoSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProdutoCarrinho
        fields = '__all__'

class CarrinhoCompletoSerializer(serializers.ModelSerializer):

    total_price = serializers.SerializerMethodField()
    items = serializers.SerializerMethodField()

    class Meta:
        model = Carrinho
        fields = [
            'id',
            'total_price',
            'items',
        ]
    def get_total_price(self, instance):
        carrinho_id = instance.id
        lista = ProdutoCarrinho.objects.filter(id_carrinho=carrinho_id)
        total = 0
        for produto in lista:
            item = Produto.objects.get(id=produto.id_produto_id)
            preco = item.price
            resultado = produto.quantidade_produto * preco
            total = total  + resultado
        return total

    def get_items(self, instance):
        carrinho_id = instance.id
        lista = ProdutoCarrinho.objects.filter(id_carrinho=carrinho_id).values('id_produto__name', 'quantidade_produto')
        return lista

class FinalizarSerializer(CarrinhoCompletoSerializer):


    def is_valid(self, raise_exception=False):

        carrinho_id = self.data['id']
        lista = ProdutoCarrinho.objects.filter(id_carrinho=carrinho_id)
        for item in lista:
            produto = Produto.objects.get(id=item.id_produto_id)
            minimo = produto.minimun
            qtd_maxima = produto.max_availability
            
            if item.quantidade_produto > qtd_maxima:
                raise serializers.ValidationError({'detail':'O produto ' + item.id_produto.name + ' não tem a quantidade escolhida em estoque'})

            if item.quantidade_produto < minimo:
                raise serializers.ValidationError({'detail':'O produto ' + item.id_produto.name + ' só pode ser comprado na quantidade mínima de: ' + str(minimo)})
                
        return self

    def get_items(self, instance):
        carrinho_id = instance.id
    
        lista = ProdutoCarrinho.objects.filter(id_carrinho=carrinho_id).values('id_produto__name', 'quantidade_produto')
        return lista
    
            
    def get_total_price(self, instance):
        carrinho_id = instance.id
        lista = ProdutoCarrinho.objects.filter(id_carrinho=carrinho_id)
        total = 0
        for produto in lista:
            item = Produto.objects.get(id=produto.id_produto_id)
            preco = item.price
            
            resultado = produto.quantidade_produto * preco
            total = total  + resultado

        return total