from django.shortcuts import (get_object_or_404, redirect, render)
from categoria.models import Categoria
from produto.models import Produto
from tipo.models import Tipo
from usuario.models import Usuario
from pedidos.models import Pedido, ItemPedido
from django.contrib import messages
from .models import (Carrinho, ItemCarrinho)

def adicionarCarrinho(request, produto_id):
    usuario_id = request.session.get('usuario_id')
    if not usuario_id:
        return redirect(f'/login/?next={request.path}')
    produto = get_object_or_404(Produto, id=produto_id)
    usuario = get_object_or_404(Usuario, id=usuario_id)
    quantidade = int(request.POST.get('quantidade', 1))
    carrinho, criado = (Carrinho.objects.get_or_create(usuario=usuario))
    item, criado = (ItemCarrinho.objects.get_or_create(carrinho=carrinho, produto=produto))
    if criado:
        item.quantidade = min(quantidade, produto.estoque)
    else:
        item.quantidade = min(item.quantidade + quantidade, produto.estoque)
    item.save()
    return redirect('carrinho')

def carrinho(request):
    usuario_id = request.session.get('usuario_id')
    if not usuario_id:
        return redirect('login')
    usuario = Usuario.objects.get(id=usuario_id)
    carrinho, criado = Carrinho.objects.get_or_create(usuario=usuario)
    total = sum(item.produto.preco * item.quantidade for item in carrinho.itens.all())
    return render (request, 'carrinho.html', {
        'categorias': Categoria.objects.all(),
        'tipos': Tipo.objects.all(),
        'carrinho': carrinho,
        'total': total
    })
    
def aumentarItemCarrinho(request, item_id):
    item = get_object_or_404(ItemCarrinho, id=item_id, carrinho__usuario_id=request.session.get('usuario_id'))
    if item.quantidade < item.produto.estoque:
        item.quantidade += 1
        item.save()
    return redirect('carrinho')

def diminuirItemCarrinho(request, item_id):
    item = get_object_or_404(ItemCarrinho, id=item_id, carrinho__usuario_id=request.session.get('usuario_id'))
    if item.quantidade > 1:
        item.quantidade -= 1
        item.save()
    else:
        item.delete()
    return redirect('carrinho')

def removerItemCarrinho(request, item_id):
    item = get_object_or_404(ItemCarrinho, id=item_id, carrinho__usuario_id=request.session.get('usuario_id'))
    item.delete()
    return redirect('carrinho')

def finalizarCompra(request):
    usuario = get_object_or_404(Usuario, id=request.session.get("usuario_id"))
    carrinho = get_object_or_404(Carrinho, usuario=usuario)
    if not carrinho.itens.exists():
        messages.error(request, "Carrinho vazio.")
        return redirect("carrinho")
    total = 0
    for item in carrinho.itens.all():
        if item.quantidade > item.produto.estoque:
            messages.error(request, f"Estoque insuficiente para {item.produto.nome}.")
            return redirect("carrinho")
        total += item.produto.preco * item.quantidade
    pedido = Pedido.objects.create(usuario=usuario, total=total)
    for item in carrinho.itens.all():
        ItemPedido.objects.create(pedido=pedido, produto=item.produto, quantidade=item.quantidade, preco=item.produto.preco)
        item.produto.estoque -= item.quantidade
        item.produto.save()
    carrinho.itens.all().delete()
    messages.success(request, "Compra realizada com sucesso!")
    return redirect("pedidos")