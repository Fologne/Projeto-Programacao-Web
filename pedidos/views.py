from django.shortcuts import redirect, render
from usuario.models import Usuario
from django.contrib import messages
from django.shortcuts import get_object_or_404
from categoria.models import Categoria
from tipo.models import Tipo
from .models import Pedido

def pedidos(request):
    usuario = Usuario.objects.get(id=request.session["usuario_id"])
    if usuario.tipo_usuario == "superadmin":
        messages.error(request, "Superadministradores não possuem pedidos.")
        return redirect("/")
    pedidos = Pedido.objects.filter(usuario=usuario).order_by("-data")
    return render(request, "pedidos.html", {
            "pedidos": pedidos,
            "categorias": Categoria.objects.all(),
            "tipos": Tipo.objects.all()
    })