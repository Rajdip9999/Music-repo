from pyrogram import Client, filters

from AnonXMusic import app
from AnonXMusic.utils.bgtmusic.bk import command

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@app.on_message(
    filters.command("owner")
    )
async def owner(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/f4333d880d3a5479ec9a8.jpg",
        caption=f"""🥀 𝐂𝐥𝐢𝐜𝐤 𝐇𝐞𝐫𝐞 𝐅𝐨𝐫 𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐎𝐰𝐧𝐞𝐫𝐬 Lucifer� 𝐎𝐫 𝐊𝐚𝐚𝐥, 𝐈𝐟 𝐘𝐨𝐮 𝐖𝐚𝐧𝐭 𝐏𝐫𝐨𝐦𝐨𝐭𝐞 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩𝐬 𝐎𝐫 𝐎𝐭𝐡𝐞𝐫𝐬 𝐋𝐢𝐧𝐤 𝐓𝐡𝐞𝐧 [𝐂𝐥𝐢𝐜𝐤 𝐇𝐞𝐫𝐞](https://t.me/BgtPromote) & 𝐂𝐥𝐢𝐜𝐤 𝐎𝐭𝐡𝐞𝐫'𝐬 𝐁𝐮𝐭𝐭𝐨𝐧 & 𝐉𝐨𝐢𝐧 𝐎𝐮𝐫 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 𝐎𝐫 𝐆𝐫𝐨𝐮𝐩.. 🥀 [𝐘𝐨𝐮𝐭𝐮𝐛𝐞](https://youtube.com/@AnonXMusicgadgetstech).""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🥀 Lucifer� 🥀", url=f"https://t.me/AnonXMusicHalder")
            ],          
            [
                    InlineKeyboardButton(
                        "🥀 𝐊𝐚𝐚𝐥 🥀", url=f"https://t.me/AdityaHalder")
                ],
                [
                    InlineKeyboardButton(
                        "🥀 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 🥀", url=f"https://t.me/Bgt_Chat"
                    ),
                    InlineKeyboardButton(
                        "🥀 𝐔𝐩𝐝𝐚𝐭𝐞𝐬 🥀", url=f"https://t.me/AnonXMusicGadgetsTech")
                ]
            ]
        ),
    )
