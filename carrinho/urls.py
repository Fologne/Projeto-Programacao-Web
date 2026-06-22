from django.urls import path
from . import views

urlpatterns = [
    path('', views.carrinho, name='carrinho'),
    path('adicionar/<int:produto_id>/', views.adicionarCarrinho,name='adicionarCarrinho'),
    path('aumentar/<int:item_id>/', views.aumentarItemCarrinho, name='aumentarItemCarrinho'),
    path('diminuir/<int:item_id>/',views.diminuirItemCarrinho, name='diminuirItemCarrinho'),
    path('remover/<int:item_id>/', views.removerItemCarrinho, name='removerItemCarrinho'),
]