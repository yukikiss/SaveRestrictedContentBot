#Github.com/Vasusen-code

import time, os

from .. import bot as Drone
from .. import userbot_telethon, userbot, Bot, AUTH
from .. import get_whitelist, load_whitelist, save_whitelist
from .. import FORCESUB as fs

from main.plugins.pyroplug import get_msg, get_msg_clean
from main.plugins.helpers import get_link, join

from telethon import events
from pyrogram.errors import FloodWait

from ethon.telefunc import force_sub

ft = f"To use this bot you've to join @{fs}."

message = "Send me the message link you want to start saving from, as a reply to this message."

# list all whitelisted chats
@Drone.on(events.NewMessage(incoming=True, from_users=AUTH, pattern='/list'))
async def list(event):
    message = "Chat name, Chat Id, Output Channel"
    for chat_id, output_channel in get_whitelist().items(): 
        chat = await userbot.get_chat(chat_id)
        message += f"\n{chat.title}, {chat_id}, {output_channel}"
    await event.reply(message)
    return

# reload whitelist from file
@Drone.on(events.NewMessage(incoming=True, from_users=AUTH, pattern='/reload'))
async def list(event):
    load_whitelist()
    # print(get_whitelist())
    await event.reply("Success!")
    return

@Drone.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
async def clone(event):
    if event.is_reply:
        reply = await event.get_reply_message()
        if reply.text == message:
            return
    try:
        link = get_link(event.text)
        if not link:
            return
    except TypeError:
        return
    s, r = await force_sub(event.client, fs, event.sender_id, ft)
    if s == True:
        await event.reply(r)
        return
    edit = await event.reply("Processing!")
    try:
        if 't.me/+' in link:
            q = await join(userbot, link)
            await edit.edit(q)
            return
        if 't.me/' in link:
            await get_msg(userbot, Bot, Drone, event.sender_id, edit.id, link, 0)
    except FloodWait as fw:
        return await Drone.send_message(event.sender_id, f'Try again after {fw.x} seconds due to floodwait from telegram.')
    except Exception as e:
        print(e)
        await Drone.send_message(event.sender_id, f"An error occurred during cloning of `{link}`\n\n**Error:** {str(e)}")
    
