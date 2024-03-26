import time
import telebot

def fluxo_um(bot, message):
    bot.reply_to(message, "Oi gatinho")
    time.sleep(2)

    with open('.\\audios\\audio1\\audio.mp3', 'rb') as audio_file:
        bot.send_audio(message.chat.id, audio=audio_file)
    time.sleep(6)
    with open('.\\midias\\1.jpg', 'rb') as imagem_file:
        bot.send_photo(message.chat.id, photo=imagem_file)
    bot.reply_to(message, "O que você achou gatinho?")

def fluxo_dois(bot, message):
    bot.reply_to(message, "Que bom meu bem.")
    bot.reply_to(message, "Isso é só uma prévia do conteúdo que eu vendo")
    with open('.\\audios\\audio2\\audio.mp3', 'rb') as audio_file:
        bot.send_audio(message.chat.id, audio=audio_file)
    bot.reply_to(message, "São 50 fotos e 50 videos por 30 reais.")
    with open('.\\audios\\audio3\\audio.mp3', 'rb') as audio_file:
        bot.send_audio(message.chat.id, audio=audio_file)
    bot.reply_to(message, "Posso te mandar os dados de pagamento ?")

def fluxo_tres(bot, message):
    bot.reply_to(message, "que bom meu amor, vou te mandar um link de pagamento, e a entrega vai ser feita pelo seu email ta bom ??")
    bot.send_message(message.chat.id, 'você vai poder acessar aqui mesmo por um canal do telegram, ou através do google drive')
    markup = types.InlineKeyboardMarkup()
    btn_checkout = types.InlineKeyboardButton(text='Comprar Agora', url='https://www.seusite.com')
    markup.add(btn_checkout)
    bot.send_message(message.chat.id, "Clique no botão abaixo para realizar o pagamento:", reply_markup=markup)

def fluxo_duvida(bot,message):
    markup = telebot.types.InlineKeyboardMarkup()
    botao = telebot.types.InlineKeyboardButton(text="Me chame no WhatsApp",
                                               url="https://wa.me/seunumerowhatsapp")  # Substitua 'seunumerowhatsapp' pelo seu número de WhatsApp
    markup.add(botao)
    bot.send_message(message.chat.id, "Para tirar suas dúvidas, me chame no WhatsApp clicando no botão abaixo.", reply_markup=markup)
