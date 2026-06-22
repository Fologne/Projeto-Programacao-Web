from django.db import models
from usuario.models import Usuario
from produto.models import Produto

class Pedido(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='pedidos')
    data = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    STATUS = (('preparando', 'Preparando'), ('enviado', 'Enviado'), ('entregue', 'Entregue'),)
    status = models.CharField(max_length=20, choices=STATUS, default='preparando')
    def __str__(self):
        return f'Pedido #{self.id}'
    
class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='itens')
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
    quantidade = models.PositiveIntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    def subtotal(self):
        return self.preco * self.quantidade