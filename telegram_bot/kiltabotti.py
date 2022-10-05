import logging

import telegram
from telegram import ReplyKeyboardMarkup, ForceReply, InlineKeyboardMarkup,\
    InlineKeyboardButton, KeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
import random
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import argparse
import requests
import datetime
import os
import sys

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

# TG-bot admins. These users have full access to every bot function!
ADMINS = ["Vesaliina"]
# Path to media folder.
MEDIA_PATH = os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), "media")
# Define system path to image from guildroom.
PHOTO_PATH = "/home/pi/webcam/image.jpeg"


def add_to_queue_type_check(callback_data):
    """ Checks if CallbackQuery should be handled by add_to_queue handler. """
    if type(callback_data) == dict and callback_data["type"] == "add_to_queue":
        return True
    return False


def restaurant_type_check(callback_data):
    if type(callback_data) == dict and callback_data["type"] == "restaurant":
        return True
    return False


def check_admin(update, context):
    """ Check is user admin. """
    is_admin = context.user_data.get("admin", False)
    if update.effective_user.username in ADMINS or is_admin:
        return True
    return False


def create_command_keyboard(update, context, startup=False):
    """ Create keyboard for spotify commands. """
    if startup:
        keyboard = [[KeyboardButton("/spotify"), KeyboardButton("/cam")],
                    [KeyboardButton("/menu")]]
    elif check_admin(update, context):
        keyboard = [[KeyboardButton("/previous"), KeyboardButton("/play"), KeyboardButton("/next")],
                    [KeyboardButton("/queue"), KeyboardButton("/pause"), KeyboardButton("/add")],
                    [KeyboardButton("/restrict"), KeyboardButton("/token"), KeyboardButton("/back")]]
    else:
        keyboard = [[KeyboardButton("/previous"), KeyboardButton("/next")],
                    [KeyboardButton("/play"), KeyboardButton("/pause")],
                    [KeyboardButton("/queue"), KeyboardButton("/add")],
                    [KeyboardButton("/back")]]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)


def bot_send_media(update, path=MEDIA_PATH, media_type="voice", name=""):
    """ Open and send media. """
    try:
        with open(os.path.join(path, name), 'rb') as media:
            if media_type == "audio":
                update.message.reply_audio(media)
            if media_type == "voice":
                update.message.reply_voice(media)
    except FileNotFoundError:
        return


######################################################################################################################
#  Start of bot commands.
######################################################################################################################


def print_menu(update, context):
    """ Print menu for the chosen restaurant. """
    if context.args:
        restaurant = context.args[0].upper()
        if restaurant in RESTAURANTS:
            RESTAURANTS[restaurant](update, context)
            return
    keyboard = [
        [InlineKeyboardButton("Reaktori", callback_data={"type": "restaurant", "function": reaktori})],
        [InlineKeyboardButton("Hertsi", callback_data={"type": "restaurant", "function": hertsi})],
        [InlineKeyboardButton("Newton", callback_data={"type": "restaurant", "function": newton})]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Choose restaurant:', reply_markup=reply_markup)


def restaurant_button(update, context):
    """ Handles the button actions of /menu command. """
    query = update.callback_query
    update.callback_query.data["function"](update, context)
    query.edit_message_text(text="Menu: ")
    context.drop_callback_data(query)


def reaktori(update, context):
    """ Prints Reaktori's menu"""
    language = "fi"
    url = "https://www.foodandco.fi/modules/json/json/Index?costNumber=0812&language={}".format(language)
    response = requests.get(url)
    data = response.json()["MenusForDays"]
    date = datetime.datetime.now().strftime("%y-%m-%d")
    message = ""
    for day in data:
        if date in day["Date"]:
            if not day["LunchTime"]:
                message += "It looks like the restaurant is closed today. "
                break
            for menu in day["SetMenus"]:
                message += "\n<b>{}</b> -- <i>{}</i>\n".format(menu["Name"], menu["Price"])
                for component in menu["Components"]:
                    message += "\t\t{}\n".format(component)

    context.bot.send_message(update.effective_message.chat_id, message, parse_mode=telegram.ParseMode.HTML)


def hertsi(update, context):
    """ Prints Hertsi's menu"""
    url = "https://www.sodexo.fi/en/ruokalistat/output/weekly_json/111"
    response = requests.get(url)
    data = response.json()["mealdates"]
    current_weekday = datetime.datetime.today().strftime('%A')
    message = ""
    for day in data:
        if current_weekday == day["date"]:
            for menu_num in day["courses"]:
                menu = day["courses"][menu_num]
                message += "\n<b>{}</b> -- <i>{}</i>\n".format(menu["title_fi"], menu["price"])
                for recipe_num in menu["recipes"]:
                    if "name" in menu["recipes"][recipe_num]:
                        message += "\t\t{}\n".format(menu["recipes"][recipe_num]["name"])
    if not message:
        message += "It looks like the restaurant is closed today. "

    context.bot.send_message(update.effective_message.chat_id, message, parse_mode=telegram.ParseMode.HTML)


def newton(update, context):
    """ Prints Newton's menu"""
    message = ""
    date = datetime.datetime.now().strftime("%Y%m%d")
    url = "https://fi.jamix.cloud/apps/menuservice/rest/haku/menu/12347/6/?lang=fi&date={}&date2={}".format(date, date)
    response = requests.get(url)
    data = response.json()[0]["menuTypes"]
    for menu_name in data:
        if menu_name["menuTypeName"] in ["Lounas", "Kasvis", "Konehuone"]:
            meal_list = menu_name["menus"][0]["days"][0]["mealoptions"]
            for meal in meal_list:
                message += "\n<b>{}</b>\n".format(meal["name"], "price")
                for recipe in meal["menuItems"]:
                    message += "\t\t{}\n".format(recipe["name"])
    context.bot.send_message(update.effective_message.chat_id, message, parse_mode=telegram.ParseMode.HTML)


RESTAURANTS = {"REAKTORI": reaktori, "HERTSI": hertsi, "NEWTON": newton}


class BotController:
    def __init__(self, spotify=True, idle=False):
        """ Class for handling bot commands"""
        self.spotify_enabled = spotify
        self.updater = self.startup(idle)


    def startup(self, idle):
        """ Authenticate the bot and initialize the updater. """
        # Read the api token from locally saved txt file
        script_dir = os.path.dirname(os.path.realpath(sys.argv[0]))
        with open(os.path.join(script_dir, "auth/token.txt")) as token_file:
            token = token_file.readlines()[0].strip()
        updater = Updater(token, arbitrary_callback_data=True, use_context=True)

        self.define_commands(updater.dispatcher)
        updater.start_polling()
        if idle:
            updater.idle()
        return updater

    def define_commands(self, dispatcher):
        """ Define bot commands! """
        dispatcher.add_handler(CommandHandler("start", self.start_chat))
        dispatcher.add_handler(CommandHandler("help", self.help_command))

        dispatcher.add_handler(CommandHandler(["cam", "kiltacam", "snap"], self.cam))
        dispatcher.add_handler(CommandHandler(["menu", "ruokalista"], print_menu))
        dispatcher.add_handler(CallbackQueryHandler(restaurant_button, pattern=restaurant_type_check))

        if self.spotify_enabled:
            spotify_api = Spotify("393afc97e7cbc2502711db80685dbed507d63be0")

            dispatcher.add_handler(CommandHandler(["spotify"], spotify_api.authenticate))
            dispatcher.add_handler(CommandHandler(["add"], spotify_api.add_to_queue))
            dispatcher.add_handler(CommandHandler(["queue"], spotify_api.print_queue))
            dispatcher.add_handler(CommandHandler(["pause", "stop"], spotify_api.pause))
            dispatcher.add_handler(CommandHandler(["play", "unpause", "continue"], spotify_api.start))
            dispatcher.add_handler(CommandHandler(["next", "skip"], spotify_api.next_track))
            dispatcher.add_handler(CommandHandler(["previous"], spotify_api.previous_track))
            dispatcher.add_handler(CommandHandler(["back"], spotify_api.back))

            # Admin commands
            dispatcher.add_handler(CommandHandler(["admin"], spotify_api.admin))
            dispatcher.add_handler(CommandHandler(["token"], spotify_api.new_token))
            dispatcher.add_handler(CommandHandler(["restrict"], spotify_api.restrict_access))

            dispatcher.add_handler(MessageHandler(Filters.reply & Filters.text, spotify_api.handle_replies))
            dispatcher.add_handler(CallbackQueryHandler(spotify_api.add_to_queue_button,
                                                        pattern=add_to_queue_type_check))
            dispatcher.add_error_handler(error_callback)
        else:
            dispatcher.add_handler(CommandHandler(["spotify"], spotify_info))

        dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, self.answer))

    def start_chat(self, update, context):
        """ Start a new chat with the bot. """
        markup = create_command_keyboard(update, context, startup=True)
        update.message.reply_markdown_v2(
            f"Hi {update.effective_user.mention_markdown_v2()}, \n"
            f"Welcome to the free 30 day trial of KiltaBot \n"
            f"Use command /help to list currently available commands \n",
            reply_markup=markup
        )


    def help_command(self, update, context):
        """Send a message when the command /help is issued."""
        update.message.reply_text("List of available commands: \n"
                                  "/start - Open bot menu. \n"
                                  "/help - Show this help message. \n"
                                  "/spotify - Open spotify command keyboard. \n"
                                  "/admin - Register yourself as an admin. \n"
                                  "/add - Add song to queue. \n"
                                  "/queue - Print current queue. \n"
                                  "/menu - Print restaurant menus. \n"
                                  "/cam - Send image from kiltacam. ")


    def answer(self, update, context):
        """Answer to message that wasn't a command."""
        if any(phrase in update.message.text.lower() for phrase in ["moi", "hei", "hi", "hello", "helou", "moro", "mo"]):
            answers = ["Ju moii! ", "Noni terveppä terve"]
        else:
            answers = ["Ei se mua haittaa.", "Ei paasata siitä sen enempää. ", "Erittäin hyvin sanottu! "]
        update.message.reply_text(random.choice(answers))


    def cam(self, update, context):
        """ Send a picture from guild room. """
        date = datetime.datetime.now()
        if date.hour not in range(8, 21):
            # It's night
            bot_send_media(update, name="kamera_tila.ogg")
        elif date.isoweekday() not in range(1, 6):
            # It's weekend
            bot_send_media(update, name="kamera_tila.ogg")
        else:
            # Send image
            try:
                with open(PHOTO_PATH, 'rb') as photo:
                    update.message.reply_photo(photo)
            except FileNotFoundError:
                update.message.reply_text("There seems to be something wrong with the camera :/")


def spotify_info(update, context):
    """ Print error message when /spotify command is run, in --no-spotify mode. """
    update.message.reply_text("I am currently running in \"no spotify mode\". "
                              "Feature coming soon. Stay tuned. ")


class Spotify:
    def __init__(self, device_id, volume=70):
        """ This class handles all spotify api related actions. """
        self.device_id = device_id
        self.spotify_api = self.spotify_setup()
        self.volume = volume
        self.auth_token = "1234"
        self.admin_token = "12345678"
        self.queue = []
        self.restricted_mode = False

    @staticmethod
    def spotify_setup():
        """ Create spotify auth object. """
        # Read the api token from locally saved txt file. First line client id, second line secret token
        scope = "user-modify-playback-state user-read-currently-playing"
        script_dir = os.path.dirname(os.path.realpath(sys.argv[0]))
        with open(os.path.join(script_dir, "auth/spotify.txt")) as spotify_file:
            lines = spotify_file.readlines()
            client_id = lines[0].strip()
            client_secret = lines[1].strip()
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret,
                                                       redirect_uri="http://localhost:8888/callback/", scope=scope))
        return sp

    def handle_replies(self, update, context):
        """ Get reply commands."""
        text = update.message.text.strip()
        reply_to = update.message.reply_to_message.text.strip()
        if reply_to == "Insert code:":
            self.compare_tokens(text, update, context)
        if reply_to == "Search:":
            reply_markup = self.create_search_keyboard(text)
            update.message.reply_text('Results:', reply_markup=reply_markup)
        if reply_to == "Insert admin code:":
            self.compare_tokens(text, update, context, token_type="admin")

    def update_auth_token(self):
        """ Generate new auth string consisting of 4 numbers. """
        self.auth_token = str(random.randint(0, 9999)).zfill(4)
        logger.info(self.auth_token)

    def new_token(self, update, context):
        """ Generate new auth token. """
        if check_admin(update, context):
            self.update_auth_token()
            update.message.reply_text("New token: {}".format(self.auth_token))
        else:
            update.message.reply_text("This action requires admin rights!")

    def restrict_access(self, update, context):
        """ Restrict access for non-admin users. """
        if check_admin(update, context):
            if self.restricted_mode:
                update.message.reply_text("Restricted mode disabled. ")
                self.restricted_mode = False
            else:
                update.message.reply_text("Restricted mode enabled. ")
                self.restricted_mode = True
        else:
            update.message.reply_text("This action requires admin rights!")

    def compare_tokens(self, input_token, update, context, token_type="auth"):
        """ Check if user token matches auth token and if so give the user spotify user rights. """
        if token_type == "auth" and input_token == self.auth_token:
            update.message.reply_text("Authentication successful; you can now use Spotify commands.")
            context.user_data["token"] = input_token
            markup = create_command_keyboard(update, context)
            update.message.reply_text('Spotify controls:', reply_markup=markup)
        elif token_type == "admin" and input_token == self.admin_token:
            update.message.reply_text("Authentication successful; you now have admin rights.")
            context.user_data["admin"] = True
            markup = create_command_keyboard(update, context)
            update.message.reply_text('Spotify controls:', reply_markup=markup)
        else:
            update.message.reply_text("Wrong token. Please try again...")

    def authenticate(self, update, context):
        """ Authenticate. """
        if self.check_auth(update, context):
            markup = create_command_keyboard(update, context)
            update.message.reply_text('Spotify controls:', reply_markup=markup)
        elif context.args:
            input_token = context.args
            self.compare_tokens(input_token[0], update, context)
        else:
            update.message.reply_text('Insert code: ', reply_markup=ForceReply(input_field_placeholder="Insert code: "))

    def check_auth(self, update, context):
        """ Check if user is authenticated to use spotify commands. """
        if check_admin(update, context):
            return True
        if self.restricted_mode:
            update.message.reply_text("An admin has enabled restricted mode. "
                                      "Spotify controls are temporarily disabled. ")
            return False
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

    def admin(self, update, context):
        """ Register user as an admin. """
        if check_admin(update, context):
            markup = create_command_keyboard(update, context)
            update.message.reply_text('Spotify controls:', reply_markup=markup)
            return
        if context.args:
            input_token = context.args
            self.compare_tokens(input_token[0], update, context, token_type="admin")
            markup = create_command_keyboard(update, context)
            update.message.reply_text('Spotify controls:', reply_markup=markup)
        else:
            update.message.reply_text('Insert admin code: ',
                                      reply_markup=ForceReply(input_field_placeholder="Insert admin code: "))

    @staticmethod
    def back(update, context):
        """ Close spotify command view. """
        markup = create_command_keyboard(update, context, startup=True)
        update.message.reply_text('Spotify controls:', reply_markup=markup)

    def start(self, update, context):
        """ Start spotify playback. """
        if not self.check_auth(update, context):
            return
        self.spotify_api.start_playback()

    def pause(self, update, context):
        """ Pause spotify playback. """
        if not self.check_auth(update, context):
            return
        self.spotify_api.pause_playback()

    def next_track(self, update, context):
        """ Skip the spotify playback to the next track. """
        if not self.check_auth(update, context):
            return
        self.spotify_api.next_track()

    def previous_track(self, update, context):
        """ Skip the spotify playback to the next track. """
        if not self.check_auth(update, context):
            return
        self.spotify_api.previous_track()

    def create_search_keyboard(self, search_query, offset=0):
        """ Creates a keyboard for searching spotify songs. """
        results = self.spotify_api.search(search_query, type="track", limit=5,
                                          offset=offset, market="FI")
        keyboard = []
        for result in results["tracks"]["items"]:
            artist = result["artists"][0]["name"]
            song_name = result["name"]
            spotify_uri = result["uri"]
            pretty_name = "{} - {}".format(artist, song_name)
            keyboard.append([InlineKeyboardButton(pretty_name,
                                                  callback_data={"type": "add_to_queue", "uri": spotify_uri,
                                                                 "name": pretty_name})])
        keyboard.append([InlineKeyboardButton("Next page",
                                              callback_data={"type": "add_to_queue", "uri": "next",
                                                             "search_query": search_query, "offset": offset+5}),
                         InlineKeyboardButton("Eiku", callback_data={"type": "add_to_queue", "uri": "cancel"})])
        reply_markup = InlineKeyboardMarkup(keyboard)
        return reply_markup

    def add_to_queue(self, update, context):
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

    def add_to_queue_button(self, update, context):
        """ Handles add_to_queue inline button presses. Adds the chosen song to the spotify play queue.  """
        if not self.check_auth(update, context):
            return
        query = update.callback_query
        query.answer()

        if "next" in query.data["uri"]:
            reply_markup = self.create_search_keyboard(query.data["search_query"], offset=query.data["offset"])
            query.edit_message_reply_markup(reply_markup=reply_markup)
        else:
            if "cancel" in query.data["uri"]:
                query.edit_message_text(text="Cancelled. ")
            else:
                self.spotify_api.add_to_queue(query.data["uri"])
                query.edit_message_text(text="Added song to the queue. ")
                self.queue.append(query.data["name"])
                context.drop_callback_data(query)
            markup = create_command_keyboard(update, context)
            context.bot.send_message(update.effective_message.chat_id, 'Spotify controls:', reply_markup=markup)

    def print_queue(self, update, context):
        """ Print the current playback queue. """
        message = ""

        data = self.spotify_api.currently_playing()
        current_artist = data["item"]["artists"][0]["name"]
        current_song_name = data["item"]["name"]
        current_pretty_name = "{} - {}".format(current_artist, current_song_name)
        progress = int(int(data["progress_ms"]) / int(data["item"]["duration_ms"]) * 20)

        message += "Currently playing:  {} \n".format(current_pretty_name)
        message += "Progress:  |{}{}| \n".format('+' * progress, '-' * (20 - progress))
        message += "Queue: \n"

        try:
            index = self.queue.index(current_pretty_name)
            self.queue = self.queue[index:]
            i = 1
            for song in self.queue:
                message += "  {}. {}\n".format(i, song)
                i += 1
                if i >= 5:
                    break
        except ValueError:
            message += "  Empty "
        update.message.reply_text(message)


######################################################################################################################
#  End of bot commands.
######################################################################################################################

def error_callback(update, context):
    """ Custom error handler. """
    try:
        raise context.error
    except spotipy.exceptions.SpotifyException as error:
        context.bot.send_message(update.effective_message.chat_id, error.msg)


def parse_arguments():
    """ Parse system arguments. """
    parser = argparse.ArgumentParser()
    parser.add_argument("--no-spotify", dest="spotify", default="true", action="store_false",
                        help="Skip spotify authentication and disable spotify related functions. ")
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_arguments()
    BotController(args.spotify, True)
