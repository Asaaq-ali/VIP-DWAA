import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from AnonX import app, Telegram
import random


@app.on_message(
    filters.command(["/start","دعائي"],"")
  & filters.private
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/6ae4c163aac6f69ad9eb9.jpg",
        caption=f""" **✧اهلين فيك يا عيوني في بوت**\n  ✧** لتفعيل البوت:**\n✧**ضيف البوت لجروبك واكتب تفعيل الادعيه **""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "أضف البوت لجروبك", url=f"https://t.me/dwaalbot?startgroup=true"), 
                ],[
                    InlineKeyboardButton(
                        " 💐𝐒𝐎𝐔𝐑𝐂𝐄 𝐒𝐎𝐇𝐀 💐", url=f"t.me/ASAAQLIO"),
                ],

            ]

        ),

    )

