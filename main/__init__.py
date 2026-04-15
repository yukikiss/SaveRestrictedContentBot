#Github.com/Vasusen-code

from pyrogram import Client
from pyrogram import filters
from pyrogram.handlers import MessageHandler

from telethon.sessions import StringSession
from telethon.sync import TelegramClient, events

from decouple import config
import logging, time, sys
import json

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("API_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
BOT_TOKEN = config("BOT_TOKEN", default=None)
SESSION = config("SESSION", default=None)
SESSION_TELETHON = config("SESSION_TELETHON", default=None)
FORCESUB = config("FORCESUB", default=None)
AUTH = config("AUTH", default=None, cast=int)
WHITELIST_JSON_FILE = config("WHITELIST_JSON_FILE", default=None)
DIALOG_INITIALIZE_LIMIT = config("DIALOG_INITIALIZE_LIMIT", default=100, cast=int)

WHITELIST = {}

def load_whitelist():
    global WHITELIST
    with open(WHITELIST_JSON_FILE, 'r') as file:
        WHITELIST = json.load(file)

def save_whitelist(whitelist : dict):
    with open(WHITELIST_JSON_FILE, 'w') as file:
        json.dump(whitelist, file, indent=4)  # Use indent for pretty printing

def get_whitelist():
    return WHITELIST

load_whitelist()

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot_telethon = TelegramClient(StringSession(SESSION_TELETHON), API_ID, API_HASH)
userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
    print('dialogs initialization...')
    for dialog in userbot.get_dialogs(DIALOG_INITIALIZE_LIMIT):
        print(dialog.chat.first_name or dialog.chat.title, dialog.chat.id)
    print('dialogs initialization... Done!')
    
except BaseException as e:
    print(e)
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
    userbot_telethon.start()
except Exception as e:
    print(e)
    sys.exit(1)
