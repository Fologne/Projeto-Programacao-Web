import random
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.hashers import make_password
from usuario.models import Usuario
from banner.models import Banner
from categoria.models import Categoria
from produto.models import Produto
from tipo.models import Tipo
from django.contrib import messages
from django.utils.text import slugify

def visualizarHome(request):
    banners = Banner.objects.filter(ativo=True).order_by('ordem')
    novidades = Produto.objects.filter(esta_disponivel=True).order_by('-modificado_em')[:5]
    mais_vendidos = Produto.objects.filter(esta_disponivel=True).order_by('-qtd_vendida')[:5]
    tipos_lista = Tipo.objects.all()
    categorias = Categoria.objects.all()
    produtos_por_tipo = {}
    for tipo in tipos_lista:
        produtos = list(Produto.objects.filter(tipo=tipo, esta_disponivel=True))
        random.shuffle(produtos)
        produtos_por_tipo[tipo.nome] = produtos[:5]
    return render(request, 'index.html', {
        'novidades': novidades,
        'mais_vendidos': mais_vendidos,
        'produtos_por_tipo': produtos_por_tipo,
        'categorias': categorias,
        'tipos': tipos_lista,
        'banners': banners
    })

def cadastroProdutos(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        slug = slugify(nome)
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
    
def visualizarProduto(request, slug):
    produto = Produto.objects.get(slug=slug)
    lista = list(
        Produto.objects.filter(tipo=produto.tipo)
        .exclude(id=produto.id)
    )
    relacionados = random.sample(lista, min(len(lista), 10))
    return render(request, 'produto.html', {
        'produto': produto,
        'relacionados': relacionados,
        'categorias': Categoria.objects.all(),
        'tipos': Tipo.objects.all()
    })
    
def produtosPorCategoria(request, slug):
    categoria = get_object_or_404(Categoria, slug=slug)
    produtos = Produto.objects.filter(categoria=categoria, esta_disponivel=True)
    return render(request, 'categoria.html', {
        'categoria': categoria,
        'produtos': produtos,
        'categorias': Categoria.objects.all(),
        'tipos': Tipo.objects.all()
    })

def produtosPorTipo(request, slug):
    tipo = get_object_or_404(Tipo, slug=slug)
    produtos = Produto.objects.filter(tipo=tipo, esta_disponivel=True)
    return render(request, 'tipo.html', {
        'tipo': tipo,
        'produtos': produtos,
        'categorias': Categoria.objects.all(),
        'tipos': Tipo.objects.all()
    })

def listaProduto(request):
    produtos = Produto.objects.all()
    categorias = Categoria.objects.all()
    tipos = Tipo.objects.all()
    return render(request, 'listaProduto.html', {
        'produtos': produtos,
        'categorias': categorias,
        'tipos': tipos
    })

def alteraProduto(request, slug):
    produto = get_object_or_404(Produto, slug=slug)
    if request.method == 'POST':
        produto.nome = request.POST.get('nome')
        produto.descricao = request.POST.get('descricao')
        produto.preco = request.POST.get('preco')
        produto.estoque = request.POST.get('estoque')
        produto.esta_disponivel = True if request.POST.get('esta_disponivel') else False
        categoria_id = request.POST.get('categoria')
        tipo_id = request.POST.get('tipo')
        produto.categoria = Categoria.objects.get(id=categoria_id)
        produto.tipo = Tipo.objects.get(id=tipo_id)
        if request.FILES.get('imagem'):
            produto.imagem = request.FILES.get('imagem')
        produto.save()
        return redirect('listaProduto')
    return render(request, 'alteraProduto.html', {
        'produto': produto,
        'categorias': Categoria.objects.all(),
        'tipos': Tipo.objects.all()
    })
    
def cadastroBanner(request):
    if request.method == 'POST':
        Banner.objects.create(
            titulo=request.POST.get('titulo'),
            imagem=request.FILES.get('imagem'),
            link=request.POST.get('link'),
            ordem=request.POST.get('ordem') or 0,
            ativo=request.POST.get('ativo') == 'true'
        )
        messages.success(
            request,
            'Banner cadastrado com sucesso!'
        )
        return redirect('cadastroBanner')
    return render(request,'cadastroBanner.html',{
        'categorias': Categoria.objects.all(),
        'tipos': Tipo.objects.all()
    })
    
def listaBanner(request):
    banners = Banner.objects.all().order_by('criado_em')
    return render(request,'listaBanner.html', {
        'banners': banners,
        'categorias': Categoria.objects.all(),
        'tipos': Tipo.objects.all()
    })

def alteraBanner(request, slug):
    banner = get_object_or_404(Banner, slug=slug)
    if request.method == 'POST':
        banner.titulo = request.POST.get('titulo')
        banner.link = request.POST.get('link')
        banner.ordem = request.POST.get('ordem')
        banner.ativo = (
            True
            if request.POST.get('ativo') == 'on'
            else False
        )
        if request.FILES.get('imagem'):
            banner.imagem = request.FILES.get('imagem')
        banner.save()
        return redirect('listaBanner')
    return render(request,'alteraBanner.html', {
        'banner': banner,
        'categorias': Categoria.objects.all(),
        'tipos': Tipo.objects.all()
    })
    
def signup (request):
    if request.session.get('usuario_id'):
        return redirect('/')
    if request.method == 'POST':
        senha = request.POST.get('senha')
        confirmar = request.POST.get('confirmar_senha')
        if senha != confirmar:
            messages.error(request, 'As senhas não coincidem.')
            return redirect('signup')
        usuario = Usuario.objects.create(
            nome_completo=request.POST.get('nome_completo'),
            username=request.POST.get('username'),
            data_nascimento=request.POST.get('data_nascimento'),
            cpf=request.POST.get('cpf'),
            foto_perfil=request.FILES.get('foto_perfil'),
            logradouro=request.POST.get('logradouro'),
            bairro=request.POST.get('bairro'),
            cep=request.POST.get('cep'),
            cidade=request.POST.get('cidade'),
            estado=request.POST.get('estado'),
            email=request.POST.get('email'),
            senha=make_password(senha),
            tipo_usuario='cliente'
        )
        request.session['usuario_id'] = usuario.id
        request.session['username'] = usuario.username
        request.session['tipo_usuario'] = usuario.tipo_usuario
        destino = request.GET.get(
            'next',
            '/'
        )
        return redirect(destino)
    return render(request,'signup.html', {
        'categorias': Categoria.objects.all(),
        'tipos': Tipo.objects.all()
    })