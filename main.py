from datetime import datetime
import telebot
import time
import random
from config import api_key, chat_id

<<<<<<< HEAD

# Chave de API do seu bot Telegram

=======
# Caminho da imagem
image = 'C:/Users/devid/Desktop/Fortunetiger_Bot/Fotos/1.jpg'
>>>>>>> ece51afe6e2c518de18a861f13551686ba19916a

# Link do seu site, se aplicável
LINK_SITE = 'https://www.instagram.com/davi_b.rezende/'

# Inicialização do bot
bot = telebot.TeleBot(api_key)

def ALERT_GAME1():
    # Obter hora atual no fuso horário da América/São_Paulo
    now = datetime.now()
    hora = now.strftime('%H:%M:%S')

    # Enviar mensagem de alerta
    message_id = bot.send_message(chat_id=chat_id, text=f'nova oportunidade de entrada às {hora}').message_id
    # Atualizar o ID da mensagem no banco de dados (substitua com sua própria lógica)
    # bd.message_ids1 = message_id
    # Aguardar 15 segundos
    time.sleep(15)
    # Marcar que a mensagem foi deletada (substitua com sua própria lógica)
    # bd.message_delete1 = True

while True:
    # Obter hora atual no fuso horário da América/São_Paulo
    now = datetime.now()
    hora = now.strftime('%H:%M:%S')

    print(hora)

    # Gerar números aleatórios
    numero_aleatorio1 = random.randint(1, 10)
    numero_aleatorio2 = random.randint(1, 10)

    # Enviar mensagem com sinal de negociação
    mensagem = f'''
✅ BRECHA IDENTIFICADA ✅

🎁 [CADASTRE-SE AQUI]({LINK_SITE}) 🎁

🦝 Jugle Delight 🦝

🔥 {numero_aleatorio1} X NORMAL
⚡️ {numero_aleatorio2} X TURBO

⏰ VÁLIDO POR 5 MINUTOS ⏰

💸 Banca Recomendada R$25,00 💸'''

    bot.send_photo(chat_id=chat_id, photo=open(image, 'rb'), caption=mensagem, parse_mode='Markdown')

    # Aguardar 240 segundos (4 minutos)
    time.sleep(240)

    # Enviar mensagem informando que a carta foi liberada
    mensagem_carta = '''
    🚨🚨CARTA LIBERADA🚨🚨
    
    ✅✅✅ GREEEN ✅✅✅
    '''
    bot.send_message(chat_id=chat_id, text=mensagem_carta, parse_mode='Markdown', disable_web_page_preview=True)
    
    # Aguardar 60 segundos
    time.sleep(60)

    mensagem_aten =  '''
            🆘🆘 ATENÇÃO 🆘🆘

🚨Dica: Alterne os giros entre normal e turbo, se tiver um GRANDE ganho, PARE, e esoere uma nova oportunidade de entrada!.

⚠️ Os Sinais Fucionam apenas na plataforma Airbety ⚠️
            🎁CADASTRE-SE AQUI🎁
CADASTRE-SE ACIMA E COMECE A PEGAR OS GREEEENS ✅✅✅
'''
    bot.send_message(chat_id=chat_id, text=mensagem_aten, parse_mode='markdown')
