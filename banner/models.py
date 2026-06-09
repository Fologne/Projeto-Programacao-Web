from django.db import models
from django.utils.text import slugify

class Banner(models.Model):
    titulo = models.CharField(max_length=100)
    slug = models.SlugField(unique=True,blank=True)
    imagem = models.ImageField(upload_to='fotos/banners')
    link = models.CharField(max_length=400,help_text='Ex: /categoria/yugioh/ ou /tipo/sleeves/')
    ativo = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = 'Banner'
        verbose_name_plural = 'Banners'
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)
    def __str__(self):
        return self.titulo