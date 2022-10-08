import os

from telethon import Button, events

from JE313P import *

IMG = os.environ.get(
    "PING_PIC", "https://telegra.ph/file/9a6d3b1a325656c0c7a13.jpg"
)
ms = 4

ALIVE = os.environ.get(
    "ALIVE", "@UUQEO"
)

CAPTION = f"**سرعة البنك:** {ms}\n المالك:『{ALIVE}』"


@JE313P.on(events.NewMessage(pattern="^/بنك"))
async def _(event):
    UMM = [[Button.url("مطور السورس", "https://t.me/UUQEO")]]
    await JE313P.send_file(event.chat_id, IMG, caption=CAPTION, buttons=UMM)
