from .. import bot as Drone
from .. import userbot_telethon, userbot, Bot, AUTH
from .. import get_whitelist
from main.plugins.pyroplug import get_msg_clean

from telethon import events

@userbot_telethon.on(events.NewMessage(func= lambda e: e.is_group))
async def new_message_event_handler(event):
    chat = await event.get_chat()
    chat_id = event.chat_id
    sender = await event.get_sender()
    sender_id = event.sender_id
    whitelist = get_whitelist() 

    if str(chat_id) in whitelist and event.media and not sender.bot:
        url = f"https://t.me/c/{event.chat.id}/{event.message.id}"
        print(chat_id, chat.title, chat.id, url, whitelist[str(chat_id)])
        
        await get_msg_clean(userbot, Bot, Drone, int(whitelist[str(chat_id)]), url)
        return 
