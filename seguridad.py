import bcrypt
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin

#Definimos una función llamada "encriptar_contraseña" que toma un único parámetro: contrasena, 
#que será la contraseña en texto plano que el usuario quiere encriptar.
def encriptar_contraseña(contrasena):
    #Genera un "salt", este es  un valor aleatorio que se utiliza para hacer más seguro el proceso de encriptación. 
    #El "salt" es necesario para evitar que contraseñas iguales generen hashes iguales, este genera salt de 16 bytes
    salt = bcrypt.gensalt()

    #-bcrypt.hashpw(): Esta función toma dos parámetros:
    #La contraseña codificada en bytes.
    #El salt generado previamente.

    #-contrasena.encode('utf-8'): La contraseña se convierte en una secuencia de bytes, 
    #ya que la librería bcrypt requiere que la contraseña esté en formato de bytes, no en formato de texto plano.

    #La función genera el hash de la contraseña utilizando el algoritmo bcrypt junto con el salt. 
    #El resultado es una contraseña encriptada (o "hasheada").
    hashed_password = bcrypt.hashpw(contrasena.encode('utf-8'), salt)

    #Finalmente, la función devuelve la contraseña encriptada (hasheada).
    #Esta contraseña se almacenará en la base de datos en lugar de la contraseña en texto plano.
    return hashed_password

    
   
#Definimos una funcion llamada "verificar_contraseña", Esta función compara una contraseña ingresada por un usuario con la contraseña 
#encriptada almacenada en la base de datos. El objetivo es verificar que la contraseña ingresada sea correcta sin almacenar nunca la contraseña en texto plano.

#-verificar_contraseña, que recibe dos parámetros:
#contrasena_ingresada: La contraseña que el usuario ingresa para verificar si es correcta.
#hashed_contrasena: La contraseña que ya ha sido encriptada (hasheada) y almacenada en la base de datos.
def verificar_contraseña(contrasena_ingresada, hashed_contrasena):

    #-bcrypt.checkpw() es una función que compara la contraseña ingresada con la contraseña encriptada 
    #almacenada en la base de datos, Si ambos hashes coinciden, la contraseña es correcta
    #y la función devuelve True. Si no coinciden, devuelve False.

    #-contrasena_ingresada.encode('utf-8'):Como bcrypt.checkpw() requiere que las contraseñas estén en formato de bytes, 
    #la contraseña ingresada por el usuario se convierte a bytes utilizando encode('utf-8').

    #-hashed_contrasena.encode('utf-8'):Similar a lo anterior, el hash de la contraseña almacenado en la base de datos 
    #también debe estar en formato de bytes, por lo que se convierte a bytes si no lo está.

    return bcrypt.checkpw(contrasena_ingresada.encode('utf-8'), hashed_contrasena.encode('utf-8'))


class LoginRequiredMiddleware(MiddlewareMixin):
    def process_request(self, request):
        allowed_urls = [
            reverse('pag_principal'),
            reverse('login'),
            reverse('registro'),
            '/admin/',  # Django admin
        ]
        # Permitir archivos estáticos
        if request.path.startswith('/static/'):
            return None
        # Permitir solo si está autenticado o en las urls permitidas
        if not request.session.get('usuario_id') and request.path not in allowed_urls:
            return redirect('pag_principal')
        return None
