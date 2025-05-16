from django.contrib import admin
from django.urls import path
from Proyecto_Web import views  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pagina_principal/', views.home, name="pag_principal"),
    path('', views.home, name='inicio'),
    path('login/', views.login, name="login"),
    path('registro/', views.registro, name='registro'),
    path('datos_victima/', views.datos_victima, name='datos_victima'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('base/', views.base, name='base'),
    path('mapas/', views.mapas, name='mapas'),  
    path('solicitud/', views.solicitud, name='solicitud'),  
    path('mis_solicitudes/', views.mis_solicitudes, name='mis_solicitudes'),  
    path('administrador/', views.administrador, name='administrador'),  
    path('logout/', views.cerrar_sesion, name='logout'),
]