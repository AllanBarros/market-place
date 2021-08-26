from django.db import models
from django.db.models.deletion import CASCADE

class Produto(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    minimun = models.IntegerField()
    amount_per_package = models.IntegerField(verbose_name="amount-per-package")
    max_availability = models.IntegerField(verbose_name="max-avaiability")

class Carrinho(models.Model):
    id = models.AutoField(primary_key=True)

class ProdutoCarrinho(models.Model):
    id_produto = models.ForeignKey('Produto', on_delete=CASCADE)
    id_carrinho = models.ForeignKey('Carrinho',on_delete=CASCADE)
    quantidade_produto = models.IntegerField()
    

