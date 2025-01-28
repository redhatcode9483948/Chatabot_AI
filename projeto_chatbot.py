#Chatabot_AI
import os
def processar_resposta(resposta,nome):
    if resposta == '1':

        
        print(f'{os.linesep}{nome}, temos Camisetas com tamanhos P, M, G e GG{os.linesep}Calças com tamanhos 36, 38, 40 e 41{os.linesep} Tenis com tamnhos 38,39,40 e 41{os.linesep} e com valores de R$ 50,00 a R$119,90 dependendo da marca e modelo, tanto masculino quanto femino{os.linesep}')
    elif resposta == '2':
        print(f'{os.linesep}{nome}, aceitamos cartão de crédito e comnseguimos parcelar em até 12x para você, cartão de débito ou pix{os.linesep}')
    elif resposta == '3':
        print(f'{os.linesep}{nome}, O prazo de entrega é de 7 a 15 dias úteis, dependendo da sua localização{os.linesep}Atendemos nos estados de SP, MG e PR{os.linesep}')  
    elif resposta == '4':
        print(f'{os.linesep}{nome}, Você pode rastrear seu pedido pelo nosso site varejo.com/rastreamento,{os.linesep}basta inserir o código de rastreio que enviaremso ao seu e-mail após a compra.{os.linesep}')      
    else:
        print('Digite apenas 1, 2, 3 ou 4')
        #elif para poupar processamento 
def start():
    #apresentar o chatbot
    print("Olá, bem vindo ao botfriendAI")
    #pedir o nome do usário
    nome = input("Qual o seu nome ?\n")
    #pedir o email do usuário
    email = input('Qual o seu melhor e-mail?\n')
    while True:
        #oferecer o menu de opções
        resposta = input(f'o que gostaria de saber hoje?{os.linesep}[1]-Quais são os produtos disponíveis?{os.linesep}[2]-Quais as formas de pagamento?{os.linesep}[3]-Qual o prazo de entrega?{os.linesep}[4]-Como posso rastrear meu pedido?{os.linesep}')
        #processar a resposta enviada
        processar_resposta(resposta, nome)
if __name__ == '__main__':
    start()