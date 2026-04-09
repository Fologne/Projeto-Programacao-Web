from django.http import HttpResponse
from django.shortcuts import redirect, render
from categoria.models import Categoria
from produto.models import Produto
from tipo.models import Tipo
from django.contrib import messages
from django.utils.text import slugify

def visualizarHome(request):
    produtos = Produto.objects.all().filter(esta_disponivel=True)
    context = {
        'produtos':produtos
    }
    return render(request, 'index.html', context)

def cadastroProdutos(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        slug = slugify(nome)

        # evitar slug duplicado
        contador = 1
        slug_original = slug
        while Produto.objects.filter(slug=slug).exists():
            slug = f"{slug_original}-{contador}"
            contador += 1

        Produto.objects.create(
            nome=nome,
            descricao=request.POST.get('descricao'),
            preco=request.POST.get('preco'),
            imagem=request.FILES.get('imagem'),
            estoque=request.POST.get('estoque'),
            esta_disponivel=request.POST.get('esta_disponivel') == 'true',
            slug=slug,
            categoria_id=request.POST.get('categoria'),
            tipo_id=request.POST.get('tipo') or None
        )

        messages.success(request, "Produto cadastrado com sucesso!")
        return redirect('cadastroProdutos')

    categorias = Categoria.objects.all()
    tipos = Tipo.objects.all()

    return render(request, 'cadastroProduto.html', {
        'categorias': categorias,
        'tipos': tipos
    })