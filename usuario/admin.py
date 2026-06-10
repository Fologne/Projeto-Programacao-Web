from django.contrib import admin
from usuario.models import Usuario

# Register your models here.
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nome_completo',)
admin.site.register(Usuario, UsuarioAdmin)