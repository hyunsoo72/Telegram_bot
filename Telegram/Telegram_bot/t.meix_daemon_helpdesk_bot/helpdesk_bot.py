import telegram
import asyncio


bot = telegram.Bot(token='6857912701:AAFC9uuDSmKPJ_IedwYCXkPYGVChu1gTMQw')
chat_id = "6848614552"

asyncio.run(bot.send_message(chat_id=chat_id, text="Oh Baba 1 2 3 \n 화이팅이여!!"))