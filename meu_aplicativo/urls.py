from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Página inicial do aplicativo
    path('webhook/', views.receber_webhook, name='webhook'),
    path('enviar/', views.enviar_dados_webhook, name='enviar_dados_webhook')  # Nova rota para enviar dados
]
