import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import app, Telegram
import random

@app.on_message(filters.command([f"قران", "قرأن", "سوره", "{BOT_USERNAME} قران"],""))
async def ihd(client: Client, message: Message):
    rl = random.randint(2,73)
    url = f"https://t.me/halid346/{rl}"
    await client.send_voice(message.chat.id,url,caption="`♕ ¦ تـم اختيـار الســوره  لـك`",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )