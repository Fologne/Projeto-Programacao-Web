from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=50, unique=True)#nome da categoria que é unico de 50 caracteres no máximo
    descricao = models.TextField(max_length=150, blank=True)
    image = models.ImageField(upload_to='fotos/categoria', blank=True)
    slug = models.SlugField(max_length=80, unique=True)