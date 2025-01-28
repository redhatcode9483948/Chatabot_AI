from django.shortcuts import render
from logic import processar_resposta

def chatbot_view(request):
    if request.method =='POST':
        nome = request.POST.get('nome')
        resposta = request.POST.get('resposta')
        resposta_processada = processar_resposta(resposta, nome)
        return render(request, 'chatbot.html', {'resposta': resposta_processada})
    return render(request, 'chatbot.html')

# Create your views here.
