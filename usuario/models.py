from django.db import models

class Usuario(models.Model):
    TIPOS = (('cliente', 'Cliente'), ('admin', 'Administrador'), ('superadmin', 'Super Administrador'))
    tipo_usuario = models.CharField(max_length=20, choices=TIPOS, default='cliente')
    nome_completo = models.CharField(max_length=150)
    username = models.CharField(max_length=50, unique=True)
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=14, unique=True)
    foto_perfil = models.ImageField(upload_to='fotos/categoria', blank=True, null=True)
    logradouro = models.CharField(max_length=150)
    bairro = models.CharField(max_length=100)
    cep = models.CharField(max_length=9)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=255)
    ativo = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
