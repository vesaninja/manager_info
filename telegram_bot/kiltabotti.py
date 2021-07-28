import logging
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update, ForceReply, InlineKeyboardMarkup,\
    InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackContext,\
    CallbackQueryHandler
import sys
import time
from pprint import pprint
import json
import os
import random
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from urllib import parse

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

######################################################################################################################
#  Start of bot commands.
######################################################################################################################


def start_chat(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    update.message.reply_markdown_v2(
        f"Hi {user.mention_markdown_v2()},"
        f"Welcome to the free 30 day trial of KiltaBot \n"
        f"Use command /help to list currently available commands \n",
        reply_markup=ForceReply(selective=True),
    )


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text("List of available commands: \n"
                              "/help: Show this help message.")


def answer(update: Update, context: CallbackContext) -> None:
    """Answer to message that wasn't a command."""
    answers = ["Ei se mua haittaa.", "Ei paasata siitä sen enempää. ", "Erittäin hyvin sanottu! "]
    update.message.reply_text(random.choice(answers))


def button_callback(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer("Nice! ")
    action, data = query.data.split('?')
    if action == "add_to_queue":
        query.edit_message_text(text=f"Adding song: {data}")


class Spotify:
    def __init__(self, device_id):
        self.device_id = device_id
        self.spotify_api = self.spotify_setup()

    def spotify_setup(self):
        """ Create spotify auth object. """
        # Read the api token from locally saved txt file. First line client id, second line secret token
        scope = "user-modify-playback-state"
        with open("spotify.txt") as spotify_file:
            lines = spotify_file.readlines()
            client_id = lines[0].strip()
            client_secret = lines[1].strip()
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret,
                                                       redirect_uri="http://localhost:8888/callback/", scope=scope))
        return sp

    def start(self, update: Update, context: CallbackContext) -> None:
        """ Start spotify playback. """
        self.spotify_api.start_playback(device_id=self.device_id)

    def pause(self, update: Update, context: CallbackContext) -> None:
        """ Pause spotify playback. """
        self.spotify_api.pause_playback(device_id=self.device_id)

    def add_to_queue(self, update: Update, context: CallbackContext) -> None:
        """ Add song to spotify queue. """
        try:
            if not context.args:
                raise ValueError()
            query = " ".join(context.args[0:])
            results = self.spotify_api.search(q=parse.quote(query), type="track")
            keyboard = []
            i = 1
            for result in results["tracks"]["items"]:
                artist = result["artists"][0]["name"]
                song_name = result["name"]
                spotify_uri = result["uri"]
                keyboard.append([InlineKeyboardButton("{}: {}".format(artist, song_name),
                                                      callback_data="add_to_queue?"+spotify_uri)])
                i += 1
            reply_markup = InlineKeyboardMarkup(keyboard)
            update.message.reply_text('Results:', reply_markup=reply_markup)

        except (IndexError, ValueError):
            update.message.reply_text('Usage: /search <query>')

    def select_song(self, update: Update, context: CallbackContext) -> None:
        """ Add selected song to queue """
        pass

    def search(self, update: Update, context: CallbackContext) -> None:
        """ Query spotify for songs. """
        try:
            if not context.args:
                raise ValueError()
            query = " ".join(context.args[0:])
            results = self.spotify_api.search(q=parse.quote(query), type="track")
            keyboard = []
            i = 1
            for result in results["tracks"]["items"]:
                artist = result["artists"][0]["name"]
                song_name = result["name"]
                spotify_uri = result["uri"]
                keyboard.append([InlineKeyboardButton("{}: {}".format(artist, song_name), callback_data=str(i))])
                i += 1
            reply_markup = InlineKeyboardMarkup(keyboard)
            update.message.reply_text('Results:', reply_markup=reply_markup)

        except (IndexError, ValueError):
            update.message.reply_text('Usage: /search <query>')


######################################################################################################################
#  End of bot commands.
######################################################################################################################


def define_commands(dispatcher):
    """ Define bot commands! """
    spotify = Spotify("393afc97e7cbc2502711db80685dbed507d63be0")
    dispatcher.add_handler(CommandHandler("start", start_chat))
    dispatcher.add_handler(CommandHandler("help", help_command))

    dispatcher.add_handler(CommandHandler(["next", "queue", "add"], spotify.add_to_queue))
    dispatcher.add_handler(CommandHandler(["pause", "stop"], spotify.pause))
    dispatcher.add_handler(CommandHandler(["play", "unpause", "continue"], spotify.start))
    dispatcher.add_handler(CommandHandler(["search", "find"], spotify.search))

    updater.dispatcher.add_handler(CallbackQueryHandler(button_callback))

    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, answer))


if __name__ == '__main__':
    # Read the api token from locally saved txt file
    with open("token.txt") as token_file:
        token = token_file.read().strip()
    updater = Updater(token)
    dispatcher = updater.dispatcher
    define_commands(dispatcher)

    # Start the Bot
    updater.start_polling()
    # Run bot in background
    updater.idle()
