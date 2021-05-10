import logging
import settings
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters


logging.basicConfig( format='%(asctime)s - %(levelname)s - %(message)s',
          level=logging.INFO,
          filename='bot.log'
          )


def start_bot(update: Updater, context: CallbackContext):
	print(update)
	mytext = """Привет {}

	Я немного туповатый бот! Я создан, чтобы зеркалить! Когда тебе одиноко отправь мне сердечко =)
	(P.S Если создатель решит, что меня пора обновить или заменить, я не обижусь, я тебя очень люблю!)
	""".format(update.message.chat.first_name) 
	update.message.reply_text(mytext)


def chat(update: Updater, context: CallbackContext):
	text = update.message.text
	logging.info(text)

	update.message.reply_text(text)


def main():
	updtr = Updater(settings.TOKEN_TELEGRAMM)

	updtr.dispatcher.add_handler(CommandHandler("start", start_bot))
	updtr.dispatcher.add_handler(MessageHandler(Filters.text, chat))

	updtr.start_polling()
	updtr.idle()

if __name__ == "__main__":
	logging.info('Bot started!')
	main()



