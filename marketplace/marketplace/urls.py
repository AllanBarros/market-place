"""marketplace URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from backend.views import ProdutoView, CarrinhoView

urlpatterns = [
    path('buscar/', ProdutoView.as_view(), name="buscar"),
    path('adicionar/', CarrinhoView.as_view(({'post': 'create'})), name="adicionar"),
    path('quantidade/', CarrinhoView.as_view(({'patch': 'partial_update'})), name="quantidade"),
    path('remover/', CarrinhoView.as_view({'delete':'destroy'}), name="remover"),
    path('exibir/', CarrinhoView.as_view({'get':'retrieve'}), name="exibir"),
    # path('comprar/', CarrinhoView.as_view(), name="comprar"),

]
