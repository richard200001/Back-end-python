from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from django.contrib import admin
from django.urls import path
from authApp import views
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('usuario', views.UsuarioGeneralView.as_view()),
    path('usuario/<int:id>', views.UsuarioView.as_view()),
    path('usuario/<int:id>/', views.UsuarioGetView.as_view()),
    path('consulta', views.ConsultaView.as_view()),
    path('inventario', views.InventarioGeneralView.as_view()),
    path('inventario/<int:id>', views.InventarioView.as_view()),
    
]