from django.db import models
from usuario.models import Usuario
from produto.models import Produto

class Carrinho(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='carrinho')
    criado_em = models.DateTimeField(auto_now=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    def total(self):
        return sum(item.subtotal() for item in self.itens.all())
    def __str__(self):
        return f'Carrinho de {self.usuario.username}'

class ItemCarrinho(models.Model):
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE, related_name='itens')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)
    def subtotal(self):
        return(self.produto.preco * self.quantidade)
    def __str__(self):
        return (f'{self.quantidade}x ' f'{self.produto.nome}')
    class Meta:
        unique_together = ('carrinho', 'produto')