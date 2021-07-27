import telepot
import sys
import time
from pprint import pprint
from telepot.loop import MessageLoop
import json
import os


######################################################################################################################
#  Start of helper functions
######################################################################################################################
def run_command(command_list, chat_id, msg):
    """
    If received text message contains / sign checks if the command is implemented in the script.
    If corresponding command is found it is called.
    :param command_list: list of string containing the commands
    :param chat_id: The id of the chat where the command originated.
    :param msg: telpot message object containing information about the message.
    :return: None
    """
    # List of command: key is the function to be executed and the list contains all of the keywords that
    # can be used to call it.
    commands = {print_help: ["help", "apua"]}

    for function in commands.keys():
        if command_list[0][1:] in commands[function]:
            function(str(chat_id), msg, command_list[1:])


def check_user(chat_id, name):
    """
    Checks if a user with given nickname exists in the json database.
    :param chat_id: int, Chat in which the user should be.
    :param name: str, (nick)name of the user.
    :return: str, id of the user
    """
    with open("database.json", 'r') as json_file:
        database = json.load(json_file)

    if chat_id in database:
        for user in database[chat_id]:
            if name in database[chat_id][user]["names"]:
                return user

######################################################################################################################
#  Start of bot commands.
######################################################################################################################


def print_help(chat_id, msg, command_list):
    """
    Gives information about the implemented bot commands.
    """
    if len(command_list) == 0:
        bot.sendMessage(chat_id, "Lista komennoista: \n"
                                 "Lisää infoa: /help <komennon nimi>")


######################################################################################################################
#  End of bot commands.
######################################################################################################################


def handle(msg):
    """
    Reads chat messages and determines wheter or not it is a command meant for the bot.
    :param msg: telpot message object containing information about the messages.
    :return:
    """
    content_type, chat_type, chat_id = telepot.glance(msg)
    command_list = ['']
    if content_type == 'text':
        command_list = msg['text'].split()
        print("Got command: %s" % command_list[0])

    if command_list[0][0] == "/":
        run_command(command_list, chat_id, msg)


if __name__ == '__main__':
    # Read the api token from locally saved txt file
    with open("token.txt") as token_file:
        token = token_file.read()
        global bot
        bot = telepot.Bot(token)
    # Runs the handle function in the background that listens the chat for possible messages.
    MessageLoop(bot, handle).run_as_thread()
    print('I am listening...')
    while 1:
        time.sleep(10)
