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