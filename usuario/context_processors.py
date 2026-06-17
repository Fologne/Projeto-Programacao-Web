from .models import Usuario

def usuario_logado(request):
    usuario = None
    usuario_id = request.session.get('usuario_id')
    if usuario_id:
        try:
            usuario = Usuario.objects.get(
                id=usuario_id
            )
        except Usuario.DoesNotExist:
            pass
    return{
        'usuario_logado': usuario
    }