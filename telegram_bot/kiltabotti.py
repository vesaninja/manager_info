import logging
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters,ConversationHandler, CallbackContext
import sys
import time
from pprint import pprint
import json
import os

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)


######################################################################################################################
#  Start of bot commands.
######################################################################################################################


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    update.message.reply_text('Ei se mua haittaa. ')


######################################################################################################################
#  End of bot commands.
######################################################################################################################

def define_commands(dispatcher):
    """
    Define bot commands!
    """
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))


if __name__ == '__main__':
    # Read the api token from locally saved txt file
    with open("token.txt") as token_file:
        token = token_file.read()
    updater = Updater(token)
    dispatcher = updater.dispatcher
    define_commands(dispatcher)

    # Start the Bot
    updater.start_polling()
    # Run bot in background
    updater.idle()
