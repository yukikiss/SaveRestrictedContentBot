from telethon.sync import TelegramClient
from telethon.sessions import StringSession

from decouple import config

API_ID = config("API_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)

with TelegramClient(StringSession(), API_ID, API_HASH) as client:
    print(client.session.save())