from django.db import models
from categoria.models import Categoria

# Create your models here.
class Produto (models.Model):
    nome = models.CharField (max_length=80, unique=True)
    descricao = models.TextField (max_length=250, blank=True)
    preco = models.DecimalField (max_digits=12, decimal_places=2)
    imagem = models.ImageField (upload_to='fotos/produtos', blank=True)
    estoque = models.IntegerField ()
    esta_disponivel = models.BooleanField(default=True)
    criado_em = models.DateTimeField (auto_now_add=True)
    modificado_em = models.DateTimeField( auto_now=True)
    slug = models.SlugField(max_length=90, unique=True)
    categoria = models.ForeignKey (Categoria, on_delete=models.CASCADE)