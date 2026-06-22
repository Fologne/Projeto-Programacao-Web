from django.shortcuts import render
from usuario.models import Usuario
from categoria.models import Categoria
from tipo.models import Tipo
from .models import Pedido

def pedidos(request):
    usuario = Usuario.objects.get(id=request.session["usuario_id"])
    pedidos = Pedido.objects.filter(usuario=usuario).order_by("-data")
    return render(request, "pedidos.html", {
            "pedidos": pedidos,
            "categorias": Categoria.objects.all(),
            "tipos": Tipo.objects.all()
    })