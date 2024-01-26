from django.urls import path
from . import views

urlpatterns = [
    path('', views.cargarIndex),
    path('AgregarProducto/',views.AgregarProducto,name='AgregarProducto'),
    path('SubirAgregarProducto',views.SubirAgregarProducto,name='SubirAgregarProducto')
]