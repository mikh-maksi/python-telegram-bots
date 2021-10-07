import logging
import random

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)


logger = logging.getLogger(__name__)

places = ["https://innovations.kh.ua/ucan","https://innovations.kh.ua/ucan1","https://innovations.kh.ua/ucan2"]

def start(update: Update, context: CallbackContext) -> None:
    """Sends a message with three inline buttons attached."""
    keyboard = [
        [InlineKeyboardButton("Развлечения", callback_data='11'),InlineKeyboardButton("Отдых", callback_data='22'),InlineKeyboardButton("Еда", callback_data='33'),],
        [InlineKeyboardButton("Остальное", callback_data='44')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Выберите сферу:', reply_markup=reply_markup)


def button(update: Update, context: CallbackContext) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query

    accept = [[InlineKeyboardButton("Принять", callback_data='1'),InlineKeyboardButton("Отказаться", callback_data='2'),InlineKeyboardButton("Еще", callback_data='3')],]
    reply_markup_accept = InlineKeyboardMarkup(accept)



    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    query.answer()
    print(query.data)

    if query.data == '11':
        string = random.choice(places)
        query.edit_message_text(text=string, reply_markup=reply_markup_accept)
    elif query.data == '22':
        string = random.choice(places)
        query.edit_message_text(text=string, reply_markup=reply_markup_accept)
    elif query.data == '33':
        string = random.choice(places)
        query.edit_message_text(text=string, reply_markup=reply_markup_accept)
    else:
        query.edit_message_text(text=f"Ссылка на оплату")

def help_command(update: Update, context: CallbackContext) -> None:
    """Displays info on how to use the bot."""
    update.message.reply_text("Use /start to test this bot.")


def main() -> None:
    """Run the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater("")

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.dispatcher.add_handler(CommandHandler('help', help_command))

    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()


if __name__ == '__main__':
    main()
