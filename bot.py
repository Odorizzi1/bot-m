import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from mensagem import mensagens
from datetime import datetime, timedelta
import pytz

TOKEN = '6355104723:AAFx5vuJ5SxoEpQG82uZ8d7KcpBcfzLqmIo'
chat_id = '-1001938186563'

# Inicialização do bot e do dispatcher
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

async def send_messages():
    while True:
        for mensagem_template in mensagens:
        
            
            # Formatar a mensagem com o URL
            url_mines = "https://afiliados.greenbets.io/visit/?bta=47748&brand=greenbetsio"
            mensagem_formatada = mensagem_template.format(url_mines=url_mines)
         
            await bot.send_message(chat_id, mensagem_formatada, parse_mode=ParseMode.MARKDOWN_V2, disable_web_page_preview=True)
            await asyncio.sleep(450)  # Pausa assíncrona após enviar a mensagem
            
            # Enviar mensagem de aviso
            aviso = "O último padrão mines passou da validade\. Aguarde o próximo padrão\!"
            await bot.send_message(chat_id, aviso, parse_mode=ParseMode.MARKDOWN_V2, disable_web_page_preview=True)
            await asyncio.sleep(180)  # Pausa assíncrona após enviar a mensagem de aviso
        

            
            # Enviar mensagem formatada

        print("sem parar")
        
asyncio.run(send_messages())



