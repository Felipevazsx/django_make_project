from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import json

def home(request):
    return render(request, 'index.html')

@csrf_exempt
def receber_webhook(request):
    if request.method == "POST":
        try:
            dados = json.loads(request.body)  # Recebe os dados JSON
            print(dados)  # Processa os dados conforme necessário
            return HttpResponse("Webhook recebido com sucesso.")
        except json.JSONDecodeError:
            return HttpResponse("Erro ao decodificar JSON.", status=400)
    return HttpResponse("Método não permitido.", status=405)

@csrf_exempt
def enviar_dados_webhook(request):
    # Lógica para enviar dados ao webhook Make.com
    dados = {
        'mensagem': 'Dados enviados ao Webhook com sucesso!'
    }
    return HttpResponse(json.dumps(dados), content_type='application/json')
