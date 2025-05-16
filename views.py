from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseForbidden
from .models import Rol, TpDocident, UsuSist, UsuLog
from django.contrib.auth.decorators import login_required
from seguridad import encriptar_contraseña, verificar_contraseña
import re
from django.contrib.auth import logout

# Pagina de inico"
def home(request):
    return render(request, 'pagina_principal/pag_principal.html')

# Página de inicio de sesión
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()

        if not username or not password:
            return render(request, 'login/login.html', {
                'error': 'Todos los campos son obligatorios.'
            })

        try:
            usuario = UsuSist.objects.get(corr=username)
            if verificar_contraseña(password, usuario.contra):
                request.session['usuario_id'] = usuario.id_usu_sist
                request.session['rol'] = usuario.id_rol.nom_rol

                # Redirigir si es víctima
                if usuario.id_rol.nom_rol.lower() == 'víctima':
                    return redirect('solicitud')  # nombre de la URL de solicitudes.html

                # Si no es víctima, redirigir a otra vista genérica
                return redirect('pag_principal')  # o a un dashboard general
            else:
                return render(request, 'login/login.html', {
                    'error': 'Contraseña incorrecta.'
                })
        except UsuSist.DoesNotExist:
            return render(request, 'login/login.html', {
                'error': 'Usuario no encontrado.'
            })

    return render(request, 'login/login.html')

    
# Vista para la página de registro
def registro(request):
    if request.method == 'POST':
        password = request.POST['contra']
        password = encriptar_contraseña(password)

        UsuSist.objects.create(
            p_nom=request.POST['p_nom'],
            s_nom=request.POST.get('s_nom'),
            p_apell=request.POST['p_apell'],
            s_apell=request.POST.get('s_apell'),
            num_ident=request.POST['num_ident'],
            direc=request.POST['direc'],
            num_tel1=request.POST['num_tel1'],
            num_tel2=request.POST.get('num_tel2'),
            corr=request.POST['corr'],
            contra=password,
            id_rol_id=request.POST['id_rol'],
            id_tpdoc_ident_id=request.POST['id_tpdoc_ident'],
        )

        if request.POST['id_rol'] == '2':
            return redirect('datos_victima') 
        else:
            return redirect('login') 

    roles = Rol.objects.all()
    tipos_documento = TpDocident.objects.all()
    return render(request, 'registro/registro.html', {
        'roles': roles,
        'tipos_documento': tipos_documento
    })

@login_required
def registrar_victima(request):
        return render(request, 'datos_victima/datos_victima.html')

#vista para el formulaario ersonal de las victimas 
def datos_victima(request):
    return render(request, 'datos_victima/datos_victima.html')

# Vista para la sección "nosotros"
def nosotros(request):
    return render(request, 'nosotros/nosotros.html')

# Vista que carga la base si quieres probarla sola
def base(request):
    return render(request, 'base/base.html')

# Vista para la página de mapas
def mapas(request):
    return render(request, 'mapas/mapas.html')  

# Vista para la página de mapas
def nosotros(request):
    return render(request, 'nosotros/nosotros.html')  

#Vista para la página de solicitud
def solicitud(request):
    return render(request, 'solicitud/solicitud.html')

#Vista para la página de mis solicitudes
def mis_solicitudes(request):
    return render(request, 'mis_solicitudes/mis_solicitudes.html')

def administrador(request):
    if 'usuario_id' not in request.session or request.session.get('rol') != 'Admin':
        return HttpResponseForbidden("Acceso no autorizado")
    
    if request.method == 'POST':
        id_usuario = request.POST.get('id_usu_sist')
        # Expresiones regulares 
        regex = {
            'p_nom': r'^[A-Za-zÁÉÍÓÚáéíóúÑñ ]{1,30}$',
            's_nom': r'^[A-Za-zÁÉÍÓÚáéíóúÑñ ]{0,30}$',
            'p_apell': r'^[A-Za-zÁÉÍÓÚáéíóúÑñ ]{1,30}$',
            's_apell': r'^[A-Za-zÁÉÍÓÚáéíóúÑñ ]{0,30}$',
            'num_ident': r'^\d{1,10}$',
            'direc': r'^[A-Za-z0-9#\-\.\, ]{1,100}$',
            'num_tel1': r'^\d{7,10}$',
            'num_tel2': r'^\d{0,10}$',
            'corr': r'^[^@\s]+@[^@\s]+\.[^@\s]+$',
            'contra': r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d!@#$%^&*()_+\-=]{8,32}$',
        }
        # Limpieza y validación
        data = {}
        for field in ['p_nom','s_nom','p_apell','s_apell','num_ident','direc','num_tel1','num_tel2','corr']:
            value = request.POST.get(field, '').strip()
            if field in regex and value:
                if not re.fullmatch(regex[field], value):
                    return render(request, 'admin/admin.html', {
                        'usuarios': UsuSist.objects.all(),
                        'roles': Rol.objects.all(),
                        'tipos_documento': TpDocident.objects.all(),
                        'error': f"Valor inválido en {field.replace('_',' ').title()}"
                    })
            # Limpieza básica para XSS
            value = re.sub(r'<.*?>', '', value)
            data[field] = value
        data['id_rol_id'] = request.POST['id_rol']
        data['id_tpdoc_ident_id'] = request.POST['id_tpdoc_ident']
        if id_usuario:
            usuario = get_object_or_404(UsuSist, id_usu_sist=id_usuario)
            for key, value in data.items():
                setattr(usuario, key, value)
            usuario.save()
        else:
            password = request.POST['contra']
            if not re.fullmatch(regex['contra'], password):
                return render(request, 'admin/admin.html', {
                    'usuarios': UsuSist.objects.all(),
                    'roles': Rol.objects.all(),
                    'tipos_documento': TpDocident.objects.all(),
                    'error': "Contraseña insegura o inválida"
                })
            password = re.sub(r'<.*?>', '', password)
            password = encriptar_contraseña(password)
            data['contra'] = password
            UsuSist.objects.create(**data)
        return redirect('administrador')
    
    eliminar_id = request.GET.get('eliminar')
    if eliminar_id:
        UsuSist.objects.filter(id_usu_sist=eliminar_id).delete()
        return redirect('administrador')
     
    usuarios = UsuSist.objects.all()
    roles = Rol.objects.all()
    tipos_documento = TpDocident.objects.all()
    return render(request, 'admin/admin.html', {
        'usuarios': usuarios,
        'roles': roles,
        'tipos_documento': tipos_documento
    })

def cerrar_sesion(request):
    logout(request)
    return redirect('pag_principal')

