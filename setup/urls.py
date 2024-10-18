from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('meu_aplicativo.urls')),  # Inclui as URLs do aplicativo na raiz
]
