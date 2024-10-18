from django.http import HttpResponse

def home(request):
    return HttpResponse("Bem-vindo ao Projeto Django com Make!")
