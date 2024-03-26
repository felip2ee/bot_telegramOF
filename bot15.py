import telebot
import csv
from datetime import datetime
from decouple import config
from fluxos import *
import time

token = config('TOKEN_BOT')
bot = telebot.TeleBot(token)

usuarios_em_fluxo = set()  

def verificar_interacao(usuario_id):
    ultima_interacao = None
    with open('interacoes.csv', 'r', newline='') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv)
        for linha in leitor_csv:
            if linha and linha[0] == str(usuario_id):
                ultima_interacao = (linha[1], linha[2])
    if ultima_interacao:
        return ultima_interacao
    else:
        return None, None

def gravar_interacao(usuario_id, data_interacao, estado_fluxo, texto):
    interacoes = []
    with open('interacoes.csv', 'r', newline='') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv)
        for linha in leitor_csv:
            interacoes.append(linha)

    nova_interacao = [usuario_id, data_interacao, estado_fluxo, texto]
    interacoes.append(nova_interacao)

    with open('interacoes.csv', 'w', newline='') as arquivo_csv:
        escritor_csv = csv.writer(arquivo_csv)
        escritor_csv.writerows(interacoes)



@bot.message_handler(func=lambda message: True)
def handle_message(message):
    usuario_id = message.from_user.id

    if usuario_id in usuarios_em_fluxo: 
        return

    _, estado_fluxo = verificar_interacao(usuario_id)


    usuarios_em_fluxo.add(usuario_id)
    
    try:
        if estado_fluxo == "fluxo_um":
            step_two(message)
        elif estado_fluxo == "fluxo_dois":
            step_three(message)
        elif estado_fluxo == "fluxo_tres":
            enviar_mensagem_whatsapp(message)
        else:
            fluxo_um(bot, message)
            gravar_interacao(usuario_id, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "fluxo_um", message.text)
    finally:

        usuarios_em_fluxo.remove(usuario_id)

def step_two(message):
    fluxo_dois(bot, message)
    usuario_id = message.from_user.id
    gravar_interacao(usuario_id, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "fluxo_dois", message.text)

def step_three(message):
    fluxo_tres(bot, message)
    usuario_id = message.from_user.id
    gravar_interacao(usuario_id, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "fluxo_tres", message.text)

def enviar_mensagem_whatsapp(message):
    fluxo_duvida(bot, message)
    usuario_id = message.from_user.id
    gravar_interacao(usuario_id, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "fluxo_duvida", message.text)

bot.polling()
