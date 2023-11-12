# Copyright (©️) @M8N_OFFICIAL
# By : Pavan Magar

from AnonX import app
from pyrogram import filters
from pyrogram.types import Chat, Message, User
from config import (
    BOT_USERNAME,
)

@app.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: app, message: Message):
  await app.send_message(message.chat.id,"هلا حبيبي , هذا رد تلقائي الحساب خاص للمساعد اذا عندك شي راسل المطور\n\n‹ اتمنى ماتدز رسائل مزعجة ›")
  return
