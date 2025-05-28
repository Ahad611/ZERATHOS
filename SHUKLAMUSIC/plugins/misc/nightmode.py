import random
from pyrogram import filters, Client, enums
from SHUKLAMUSIC import app
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from pyrogram.types import ChatPermissions
from SHUKLAMUSIC.mongo.nightmodedb import nightdb, nightmode_on, nightmode_off, get_nightchats

# Corrected chat permissions
CLOSE_CHAT = ChatPermissions(
    can_send_messages=False,
    can_send_media_messages=False,
    can_send_polls=False,
    can_send_other_messages=False,
    can_add_web_page_previews=False,
    can_change_info=False,
    can_invite_users=False,
    can_pin_messages=False
)

OPEN_CHAT = ChatPermissions(
    can_send_messages=True,
    can_send_media_messages=True,
    can_send_other_messages=True,
    can_send_polls=True,
    can_add_web_page_previews=True,
    can_change_info=True,
    can_invite_users=True,
    can_pin_messages=True
)

buttons = InlineKeyboardMarkup([[
    InlineKeyboardButton("๏ ᴇɴᴀʙʟᴇ ๏", callback_data="add_night"),
    InlineKeyboardButton("๏ ᴅɪsᴀʙʟᴇ ๏", callback_data="rm_night")
]])

@app.on_message(filters.command("nightmode") & filters.group)
async def _nightmode(_, message):
    await message.reply_photo(
        photo="https://telegra.ph//file/06649d4d0bbf4285238ee.jpg",
        caption="**ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴇɴᴀʙʟᴇ ᴏʀ ᴅɪsᴀʙʟᴇ ɴɪɢʜᴛᴍᴏᴅᴇ ɪɴ ᴛʜɪs ᴄʜᴀᴛ.**",
        reply_markup=buttons
    )

@app.on_callback_query(filters.regex("^(add_night|rm_night)$"))
async def nightcb(_, query: CallbackQuery):
    data = query.data
    chat_id = query.message.chat.id
    user_id = query.from_user.id
    check_night = await nightdb.find_one({"chat_id": chat_id})
    administrators = []
    async for m in app.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
        administrators.append(m.user.id)

    if user_id in administrators:
        if data == "add_night":
            if check_night:
                await query.message.edit_caption("**๏ ɴɪɢʜᴛᴍᴏᴅᴇ ɪs ᴀʟʀᴇᴀᴅʏ ᴇɴᴀʙʟᴇᴅ ɪɴ ᴛʜɪs ᴄʜᴀᴛ.**")
            else:
                await nightmode_on(chat_id)
                await query.message.edit_caption(
                    "**๏ ᴀᴅᴅᴇᴅ ᴄʜᴀᴛ ᴛᴏ ᴍʏ ᴅᴀᴛᴀʙᴀsᴇ . ᴛʜɪs ɢʀᴏᴜᴘ ᴡɪʟʟ ʙᴇ ᴄʟᴏsᴇᴅ ᴏɴ 𝟷𝟸ᴀᴍ [IST] ᴀɴᴅ ᴡɪʟʟ ᴏᴘᴇɴᴇᴅ ᴏɴ 𝟶𝟼ᴀᴍ [IST] .**"
                )
        elif data == "rm_night":
            if check_night:
                await nightmode_off(chat_id)
                await query.message.edit_caption("**๏ ɴɪɢʜᴛᴍᴏᴅᴇ ʀᴇᴍᴏᴠᴇᴅ ғʀᴏᴍ ᴍʏ ᴅᴀᴛᴀʙᴀsᴇ !**")
            else:
                await query.message.edit_caption("**๏ ɴɪɢʜᴛᴍᴏᴅᴇ ɪs ᴀʟʀᴇᴀᴅʏ ᴅɪsᴀʙʟᴇᴅ ɪɴ ᴛʜɪs ᴄʜᴀᴛ.**")

# Night mode closing job
async def start_nightmode():
    chats = await get_nightchats()
    if not chats:
        return

    for chat in chats:
        chat_id = int(chat["chat_id"])
        try:
            await app.send_photo(
                chat_id,
                photo="https://telegra.ph//file/06649d4d0bbf4285238ee.jpg",
                caption=(
                    "**ᴍᴀʏ ᴛʜᴇ ᴀɴɢᴇʟs ғʀᴏᴍ ʜᴇᴀᴠᴇɴ ʙʀɪɴɢ ᴛʜᴇ sᴡᴇᴇᴛᴇsᴛ ᴏғ ᴀʟʟ ᴅʀᴇᴀᴍs ғᴏʀ ʏᴏᴜ. "
                    "ɢʀᴏᴜᴘ ɪs ᴄʟᴏsɪɴɢ, ɢᴏᴏᴅ ɴɪɢʜᴛ ᴇᴠᴇʀʏᴏɴᴇ!**"
                )
            )
            await app.set_chat_permissions(chat_id, CLOSE_CHAT)
        except Exception as e:
            print(f"[Error] Unable to close group {chat_id} - {e}")

# Morning open job
async def close_nightmode():
    chats = await get_nightchats()
    if not chats:
        return

    for chat in chats:
        chat_id = int(chat["chat_id"])
        try:
            await app.send_photo(
                chat_id,
                photo="https://telegra.ph//file/14ec9c3ff42b59867040a.jpg",
                caption=(
                    "**ɢʀᴏᴜᴘ ɪs ᴏᴘᴇɴɪɴɢ, ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ ᴇᴠᴇʀʏᴏɴᴇ!\n\n"
                    "ᴍᴀʏ ᴛʜɪs ᴅᴀʏ ʙʀɪɴɢ ʏᴏᴜ ʟᴏᴠᴇ, ʜᴀᴘᴘɪɴᴇss ᴀɴᴅ sᴜᴄᴄᴇss.**"
                )
            )
            await app.set_chat_permissions(chat_id, OPEN_CHAT)
        except Exception as e:
            print(f"[Error] Unable to open group {chat_id} - {e}")

# Scheduler setup
scheduler = AsyncIOScheduler(timezone="Asia/Kolkata")
scheduler.add_job(start_nightmode, trigger="cron", hour=23, minute=59)
scheduler.add_job(close_nightmode, trigger="cron", hour=6, minute=1)
scheduler.start()
