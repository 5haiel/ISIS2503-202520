from ..models import Usuario

def get_usuarios():
    # Retorna los 10 usuarios más recientes
    queryset = Usuario.objects.all().order_by('-id_usuario')[:10]
    return queryset


def create_usuario(nombre, correo, telefono=None, direccion_entrega=None, ciudad=None, codigo_postal=None, pais='Colombia'):
    usuario = Usuario(
        nombre=nombre,
        correo=correo,
        telefono=telefono,
        direccion_entrega=direccion_entrega,
        ciudad=ciudad,
        codigo_postal=codigo_postal,
        pais=pais
    )
    usuario.save()
    return usuario
