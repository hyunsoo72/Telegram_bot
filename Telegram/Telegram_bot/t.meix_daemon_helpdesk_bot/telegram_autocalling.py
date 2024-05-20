import telegram
import asyncio
from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters

token = '6857912701:AAFC9uuDSmKPJ_IedwYCXkPYGVChu1gTMQw'
id = '6848614552'

bot = telegram.Bot(token)
asyncio.run(bot.sendMessage(chat_id=id, text = '자동으로 응답해줍니다. "안녕" 또는 "뭐해"를 입력해 보세요.'))

# 업데이트 된 정보 가져오기(새로운 채팅)
updater = Updater(token=token, use_context= True)
dispatcher = updater.dispatcher
# 계속해서 업데이트 됐는지 확인하는 듯.
updater.start_polling()

# 업데이트 내용 중 텍스트를 확인함
def handler(update, context):
    user_text = update.message.text
    if user_text == "안녕":
        bot.send_message(chat_id = id, text = '어~ 안녕~ ㅎㅎㅎ')
    elif user_text == "뭐해":
        bot.send_message(chat_id = id, text = '파이썬 공부중이야~')
    else:
        bot.send_message(chat_id = id, text = '무슨 말인지 모르겠어~')
        
# 업데이트 됐을 때 자동응답하는 함수로 연결(핸들러 설정)        
echo_handler = MessageHandler(Filters.text, handler)
dispatcher.add_handler(echo_handler)