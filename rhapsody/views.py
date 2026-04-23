import random
from django.http import HttpResponse
from django.shortcuts import redirect, render
from categoria.models import Categoria
from produto.models import Produto
from tipo.models import Tipo
from django.contrib import messages
from django.utils.text import slugify

def visualizarHome(request):
    novidades = Produto.objects.order_by('-criado_em')[:5]
    mais_vendidos = Produto.objects.order_by('-qtd_vendida')[:5]
    tipos_lista = Tipo.objects.all()
    categorias = Categoria.objects.all()
    produtos_por_tipo = {}
    for tipo in tipos_lista:
        produtos = list(Produto.objects.filter(tipo=tipo))
        random.shuffle(produtos)
        produtos_por_tipo[tipo.nome] = produtos[:5]
    return render(request, 'index.html', {
        'novidades': novidades,
        'mais_vendidos': mais_vendidos,
        'produtos_por_tipo': produtos_por_tipo,
        'categorias': categorias,   # 🔥 importante
        'tipos': tipos_lista        # 🔥 importante
    })

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