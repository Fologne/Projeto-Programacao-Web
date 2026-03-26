from django.http import HttpResponse
from django.shortcuts import render
from produto.models import Produto

def visualizarHome(request):
    produtos = Produto.objects.all().filter(esta_disponivel=True)
    context = {
        'produtos':produtos
    }
    return render(request, 'index.html', context)