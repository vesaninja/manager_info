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
import argparse

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

# Define system path to image from guildroom.
PHOTO_PATH = "kiltahuone.jpg"
# TG-bot admins. These users have full access to every bot function!
ADMINS = ["Vesaliina"]

######################################################################################################################
#  Start of bot commands.
######################################################################################################################


def add_to_queue_type_check(callback_data):
    """ Checks if CallbackQuery should be handled by add_to_queue handler. """
    if type(callback_data) == dict and callback_data["type"] == "add_to_queue":
        return True
    return False


def authenticate_type_check(callback_data):
    """ Checks if CallbackQuery should be handled by add_to_queue handler. """
    if type(callback_data) == dict and callback_data["type"] == "auth":
        return True
    return False


def volume_control_type_check(callback_data):
    if type(callback_data) == dict and callback_data["type"] == "volume":
        return True
    return False


def start_chat(update: Update, context: CallbackContext):
    user = update.effective_user
    update.message.reply_markdown_v2(
        f"Hi {user.mention_markdown_v2()}, \n"
        f"Welcome to the free 30 day trial of KiltaBot \n"
        f"Use command /help to list currently available commands \n",
        reply_markup=ForceReply(selective=True),
    )


def help_command(update: Update, context: CallbackContext):
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


def answer(update: Update, context: CallbackContext):
    """Answer to message that wasn't a command."""
    if any(phrase in update.message.text.lower() for phrase in ["moi", "hei", "hi", "hello", "helou", "moro", "mo"]):
        answers = ["Ju moii! ", "Noni terveppä terve"]
    else:
        answers = ["Ei se mua haittaa.", "Ei paasata siitä sen enempää. ", "Erittäin hyvin sanottu! "]
    update.message.reply_text(random.choice(answers))


def cam(update: Update, context: CallbackContext):
    """ Send a picture from guild room. """
    try:
        with open(PHOTO_PATH, 'rb') as photo:
            update.message.reply_photo(photo)
    except FileNotFoundError:
        update.message.reply_text("There seems to be something wrong with the camera :/")

"""
def create_command_keyboard(keyboard):
    keyboard = [[KeyboardButton("/previous"), KeyboardButton("/play"), KeyboardButton("/next")],
                [KeyboardButton("/volume"), KeyboardButton("/pause"), KeyboardButton("/add")]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    update.message.reply_text('Spotify controls:', reply_markup=reply_markup)
"""

class Spotify:
    def __init__(self, device_id, volume=70):
        """ This class handles all spotify api related actions. """
        self.device_id = device_id
        self.spotify_api = self.spotify_setup()
        self.volume = volume
        self.set_volume(self.volume)
        self.auth_token = "1234"

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

    def handle_replies(self, update: Update, context: CallbackContext):
        """ Get reply commands."""
        text = update.message.text.strip()
        reply_to = update.message.reply_to_message.text.strip()
        if reply_to == "Insert code:":
            self.compare_tokens(text, update, context)
        if reply_to == "Search:":
            reply_markup = self.create_search_keyboard(text)
            update.message.reply_text('Results:', reply_markup=reply_markup)

    def update_auth_token(self):
        """ Generate new auth string consisting of 4 numbers. """
        self.auth_token = str(random.randint(0, 9999)).zfill(4)
        logger.info(self.auth_token)

    def new_token(self, update: Update, context: CallbackContext):
        """ Generate new auth token. """
        self.update_auth_token()

    def compare_tokens(self, input_token, update, context):
        """ Check if user token matches auth token and if so give the user spotify user rights. """
        if input_token == self.auth_token:
            update.message.reply_text("Authentication successful; you can now use Spotify commands.")
            context.user_data["token"] = input_token
        else:
            update.message.reply_text("Wrong token. Please try again...")

    def authenticate(self, update: Update, context: CallbackContext):
        """ Authenticate . """
        if context.args:
            input_token = context.args
            self.compare_tokens(input_token[0], update, context)
        else:
            update.message.reply_text('Insert code: ', reply_markup=ForceReply(input_field_placeholder="Insert code: "))

    def check_auth(self, update, context):
        """ Check if user is authenticated to use spotify commands. """
        if update.effective_user.username in ADMINS:
            logger.info("This dude is Admin!")
            return True
        value = context.user_data.get("token", None)
        if value:
            if value == self.auth_token:
                logger.info("Correct token.")
                return True
            else:
                update.message.reply_text("Auth token expired. "
                                          "Use command /spotify <auth token> to authenticate. ")
                return False
        update.message.reply_text("You need to authenticate yourself before using Spotify controls. "
                                  "Use command /spotify <auth token> to authenticate. ")
        return False

    def start(self, update: Update, context: CallbackContext):
        """ Start spotify playback. """
        if not self.check_auth(update, context):
            return
        self.spotify_api.start_playback(device_id=self.device_id)

    def pause(self, update: Update, context: CallbackContext):
        """ Pause spotify playback. """
        if not self.check_auth(update, context):
            return
        self.spotify_api.pause_playback(device_id=self.device_id)

    def next_track(self, update: Update, context: CallbackContext):
        """ Skip the spotify playback to the next track. """
        if not self.check_auth(update, context):
            return
        self.spotify_api.next_track(device_id=self.device_id)

    def previous_track(self, update: Update, context: CallbackContext):
        """ Skip the spotify playback to the next track. """
        if not self.check_auth(update, context):
            return
        self.spotify_api.previous_track(device_id=self.device_id)

    def set_volume(self, action=None):
        """ Update spotify volume. """
        if action == "-" and self.volume > 0:
            self.volume -= 10
        if action == "+" and self.volume < 100:
            self.volume += 10
        self.spotify_api.volume(self.volume, device_id=self.device_id)

    def volume_control(self, update: Update, context: CallbackContext):
        """ Increase or decrease spotify volume. """
        if not self.check_auth(update, context):
            return
        keyboard = [
            [InlineKeyboardButton("-", callback_data={"type": "volume", "action": "-"}),
             InlineKeyboardButton("+", callback_data={"type": "volume", "action": "+"})],
            [InlineKeyboardButton("Done", callback_data={"type": "volume", "action": "done"})]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_text('Set volume:', reply_markup=reply_markup)

    def volume_control_button(self, update: Update, context: CallbackContext):
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
        """ Creates a keyboard for searching spotify songs. """
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

    def add_to_queue(self, update: Update, context: CallbackContext):
        """ Add song to spotify queue. """
        if not self.check_auth(update, context):
            return
        try:
            if not context.args:
                raise ValueError()
            query_input = " ".join(context.args[0:])
            if "vauhti" in query_input:
                update.message.reply_text("Vauhti kiihtyy wowowow. ")
            reply_markup = self.create_search_keyboard(query_input)
            update.message.reply_text('Results:', reply_markup=reply_markup)

        except (IndexError, ValueError):
            # update.message.reply_text('Usage: /add vauhti kiihtyy')
            update.message.reply_text('Search: ', reply_markup=ForceReply(input_field_placeholder="Search: "))

    def add_to_queue_button(self, update: Update, context: CallbackContext):
        """ Handles add_to_queue inline button presses. Adds the chosen song to the spotify play queue.  """
        if not self.check_auth(update, context):
            return
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

    def search(self, update: Update, context: CallbackContext):
        """ Query spotify for songs. """
        if not self.check_auth(update, context):
            return
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

def define_commands(dispatcher, spotify):
    """ Define bot commands! """
    dispatcher.add_handler(CommandHandler("start", start_chat))
    dispatcher.add_handler(CommandHandler("help", help_command))

    dispatcher.add_handler(CommandHandler(["cam", "kiltacam", "snap"], cam))

    if spotify:
        spotify_api = Spotify("393afc97e7cbc2502711db80685dbed507d63be0")

        dispatcher.add_handler(CommandHandler(["spotify"], spotify_api.authenticate))
        dispatcher.add_handler(CommandHandler(["queue", "add"], spotify_api.add_to_queue))
        dispatcher.add_handler(CommandHandler(["pause", "stop"], spotify_api.pause))
        dispatcher.add_handler(CommandHandler(["play", "unpause", "continue"], spotify_api.start))
        dispatcher.add_handler(CommandHandler(["next", "skip"], spotify_api.next_track))
        dispatcher.add_handler(CommandHandler(["previous"], spotify_api.previous_track))
        dispatcher.add_handler(CommandHandler(["search", "find"], spotify_api.search))
        dispatcher.add_handler(CommandHandler(["volume"], spotify_api.volume_control))
        dispatcher.add_handler(CommandHandler(["token"], spotify_api.new_token))

        dispatcher.add_handler(MessageHandler(Filters.reply & Filters.text, spotify_api.handle_replies))

        dispatcher.add_handler(CallbackQueryHandler(spotify_api.add_to_queue_button,
                                                    pattern=add_to_queue_type_check))
        dispatcher.add_handler(CallbackQueryHandler(spotify_api.volume_control_button,
                                                    pattern=volume_control_type_check))

    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, answer))


def parse_arguments():
    """ Parse system arguments. """
    parser = argparse.ArgumentParser()
    parser.add_argument("--no-spotify", dest="spotify", default="true", action="store_false",
                        help="Skip spotify authentication and disable spotify related functions. ")
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_arguments()
    # Read the api token from locally saved txt file
    with open("token.txt") as token_file:
        token = token_file.read().strip()
    updater = Updater(token, arbitrary_callback_data=True, use_context=True)

    define_commands(updater.dispatcher, args.spotify)

    # Start the Bot
    updater.start_polling()
    # Run bot in background
    updater.idle()
