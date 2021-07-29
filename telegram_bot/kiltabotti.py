import logging
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update, ForceReply, InlineKeyboardMarkup,\
    InlineKeyboardButton, KeyboardButton
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
        f"Hi {user.mention_markdown_v2()}, \n"
        f"Welcome to the free 30 day trial of KiltaBot \n"
        f"Use command /help to list currently available commands \n",
        reply_markup=ForceReply(selective=True),
    )


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text("List of available commands: \n"
                              "/help: Show this help message. \n"
                              "/spotify: Open spotify command keyboard \n"
                              "/play: Start playback. \n"
                              "/pause: Pause playback. \n"
                              "/skip: Skip to the the next song \n"
                              "/previous: Return to the previous song \n"
                              "/volume: Open volume control \n"
                              "/add: Add song to queue. ")


def answer(update: Update, context: CallbackContext) -> None:
    """Answer to message that wasn't a command."""
    if any(phrase in update.message.text.lower() for phrase in ["moi", "hei", "hi", "hello", "helou", "moro", "mo"]):
        answers = ["Ju moii! ", "Noni terveppä terve"]
    else:
        answers = ["Ei se mua haittaa.", "Ei paasata siitä sen enempää. ", "Erittäin hyvin sanottu! "]
    update.message.reply_text(random.choice(answers))


class Spotify:
    def __init__(self, device_id, volume=70):
        self.device_id = device_id
        self.spotify_api = self.spotify_setup()
        self.volume = volume
        self.set_volume(self.volume)

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

    def create_command_keyboard(self, update: Update, context: CallbackContext) -> None:
        """ Create telegram inline keyboard for quick command access. """
        keyboard = [[KeyboardButton("/previous"), KeyboardButton("/play"), KeyboardButton("/next")],
                    [KeyboardButton("/volume"), KeyboardButton("/pause"), KeyboardButton("/add")]]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        update.message.reply_text('Spotify controls:', reply_markup=reply_markup)

    def start(self, update: Update, context: CallbackContext) -> None:
        """ Start spotify playback. """
        self.spotify_api.start_playback(device_id=self.device_id)

    def pause(self, update: Update, context: CallbackContext) -> None:
        """ Pause spotify playback. """
        self.spotify_api.pause_playback(device_id=self.device_id)

    def next_track(self, update: Update, context: CallbackContext) -> None:
        """ Skip the spotify playback to the next track. """
        self.spotify_api.next_track(device_id=self.device_id)

    def previous_track(self, update: Update, context: CallbackContext) -> None:
        """ Skip the spotify playback to the next track. """
        self.spotify_api.previous_track(device_id=self.device_id)

    def set_volume(self, action=None) -> None:
        """ Update spotify volume. """
        if action == "-" and self.volume > 0:
            self.volume -= 10
        if action == "+" and self.volume < 100:
            self.volume += 10
        self.spotify_api.volume(self.volume, device_id=self.device_id)

    def volume_control(self, update: Update, context: CallbackContext) -> None:
        """ Increase or decrease spotify volume. """
        keyboard = [
            [InlineKeyboardButton("-", callback_data={"type": "volume", "action": "-"}),
             InlineKeyboardButton("+", callback_data={"type": "volume", "action": "+"})],
            [InlineKeyboardButton("Done", callback_data={"type": "volume", "action": "done"})]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_text('Set volume:', reply_markup=reply_markup)

    def volume_control_type_check(self, callback_data):
        if type(callback_data) == dict and callback_data["type"] == "volume":
            return True
        return False

    def volume_control_button(self, update: Update, context: CallbackContext) -> None:
        query = update.callback_query
        if query.data["action"] == '-':
            self.set_volume('-')
        if query.data["action"] == '+':
            self.set_volume('+')
        if query.data["action"] == 'done':
            query.answer()
            query.edit_message_text(text="Done")
            context.drop_callback_data(query)

    def create_search_keyboard(self, search_query, offset=0):
        results = self.spotify_api.search(search_query, type="track", limit=5,
                                          offset=offset, market="FI")
        keyboard = []
        for result in results["tracks"]["items"]:
            artist = result["artists"][0]["name"]
            song_name = result["name"]
            spotify_uri = result["uri"]
            keyboard.append([InlineKeyboardButton("{}: {}".format(artist, song_name),
                                                  callback_data={"type": "add_to_queue", "uri": spotify_uri})])
        keyboard.append([InlineKeyboardButton("Next page", callback_data={"type": "add_to_queue", "uri": "next",
                                                                          "search_query": search_query,
                                                                          "offset": offset+5}),
                         InlineKeyboardButton("Eiku", callback_data={"type": "add_to_queue", "uri": "cancel"})])
        reply_markup = InlineKeyboardMarkup(keyboard)
        return reply_markup

    def add_to_queue(self, update: Update, context: CallbackContext) -> None:
        """ Add song to spotify queue. """
        try:
            if not context.args:
                raise ValueError()
            query_input = " ".join(context.args[0:])
            if "vauhti" in query_input:
                update.message.reply_text("Vauhti kiihtyy wowowow. ")
            reply_markup = self.create_search_keyboard(query_input)
            update.message.reply_text('Results:', reply_markup=reply_markup)

        except (IndexError, ValueError):
            update.message.reply_text('Usage: /add vauhti kiihtyy')

    def add_to_queue_type_check(self, callback_data):
        """ Checks if CallbackQuery should be handled by add_to_queue handler. """
        if type(callback_data) == dict and callback_data["type"] == "add_to_queue":
            return True
        return False

    def add_to_queue_button(self, update: Update, context: CallbackContext) -> None:
        """ Handles add_to_queue inline button presses. Adds the chosen song to the spotify play queue.  """
        query = update.callback_query
        query.answer()

        if "next" in query.data["uri"]:
            reply_markup = self.create_search_keyboard(query.data["search_query"], offset=query.data["offset"])
            query.edit_message_reply_markup(reply_markup=reply_markup)
        elif "cancel" in query.data["uri"]:
            query.edit_message_text(text="Cancelled. ")
        else:
            self.spotify_api.add_to_queue(query.data["uri"])
            query.edit_message_text(text="Added song to the queue. ")
            context.drop_callback_data(query)

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

    dispatcher.add_handler(CommandHandler(["spotify"], spotify.create_command_keyboard))
    dispatcher.add_handler(CommandHandler(["queue", "add"], spotify.add_to_queue))
    dispatcher.add_handler(CommandHandler(["pause", "stop"], spotify.pause))
    dispatcher.add_handler(CommandHandler(["play", "unpause", "continue"], spotify.start))
    dispatcher.add_handler(CommandHandler(["next", "skip"], spotify.next_track))
    dispatcher.add_handler(CommandHandler(["previous"], spotify.previous_track))
    dispatcher.add_handler(CommandHandler(["search", "find"], spotify.search))
    dispatcher.add_handler(CommandHandler(["volume"], spotify.volume_control))

    updater.dispatcher.add_handler(CallbackQueryHandler(spotify.add_to_queue_button,
                                                        pattern=spotify.add_to_queue_type_check))
    updater.dispatcher.add_handler(CallbackQueryHandler(spotify.volume_control_button,
                                                        pattern=spotify.volume_control_type_check))

    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, answer))


if __name__ == '__main__':
    # Read the api token from locally saved txt file
    with open("token.txt") as token_file:
        token = token_file.read().strip()
    updater = Updater(token, arbitrary_callback_data=True)
    update_dispatcher = updater.dispatcher
    define_commands(update_dispatcher)

    # Start the Bot
    updater.start_polling()
    # Run bot in background
    updater.idle()
