import logging

from telegram.ext import Updater, CommandHandler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

TOKEN = '' # your token here

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me :)")
    logging.info(f'Got /start in chat_id {update.effective_chat.id}')


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()
