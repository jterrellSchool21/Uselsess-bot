from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler

def start(bot, update):
	bot.sendMessage(chat_id=update.message.chat_id, text="Привет, Хозяин!")

def text_handle(bot, update):
	bot.sendMessage(chat_id=update.message.chat_id, text='Привет')


updater = Updater('878532279:AAG7tdIAQBYmm0axHx6wmbt3B5GtD7_EB74')

start_handler = CommandHandler('start', start) 

message_handler = MessageHandler('', text_handle)

updater.dispatcher.add_handler(start_handler)
updater.dispatcher.add_handler(message_handler)

updater.start_polling()