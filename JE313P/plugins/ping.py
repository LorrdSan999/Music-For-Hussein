import os

from telethon import Button, events

from JE313P import *

IMG = os.environ.get(
    "PING_PIC", "https://telegra.ph/file/1414f775c59c3b2bc8d95.jpg"
)
ms = 4

ALIVE = os.environ.get(
    "ALIVE", "@O_GH0"
)

CAPTION = f"**سرعة البنك:** {ms}\n المالك:『{ALIVE}』"


@JE313P.on(events.NewMessage(pattern="^/بنك"))
async def _(event):
    UMM = [[Button.url("مطور السورس", "https://t.me/O_GH0")]]
    await JE313P.send_file(event.chat_id, IMG, caption=CAPTION, buttons=UMM)
