from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler


# 토큰을 bot_token 변수에 저장
bot_token = '7163354721:AAHaWwtfjTAmSPVYGenoa6ONu9kQ2-7_-NM'


# start 명령어 처리 함수
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    send_msg = "[채팅방]\n캄보디아 최고의 텔레그램 마케팅 채팅방에 오신 것을 환영합니다.\n/help : 채팅방 사용법"

    await context.bot.send_message(chat_id=update.effective_chat.id, text=send_msg)


if __name__ == '__main__':

    # 챗봇 application 인스턴스 생성
    application = ApplicationBuilder().token(bot_token).build()

    # start 핸들러 생성
    start_handler = CommandHandler('start', start)

    # 핸들러 추가
    application.add_handler(start_handler)

    # 폴링 방식으로 실행
    application.run_polling()