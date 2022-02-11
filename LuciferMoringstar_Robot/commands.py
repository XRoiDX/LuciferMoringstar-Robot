from random import choice
from config import START_MSG, FORCES_SUB, BOT_PICS, ADMINS, bot_info, DEV_NAME
from pyrogram import Client as LuciferMoringstar_Robot, filters as Worker
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from translation import LuciferMoringstar
from LuciferMoringstar_Robot.database.broadcast_db import Database

db = Database()


@LuciferMoringstar_Robot.on_message(Worker.private & Worker.command(["start"]))
async def start_message(bot, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
    if len(message.command) != 2:
        if message.from_user.id not in ADMINS: 
            buttons = [[
             InlineKeyboardButton("➕️ ᴀᴅᴅ ᴍᴇ ᴛᴏ yᴏᴜʀ ᴄʜᴀᴛ ➕️", url=f"http://t.me/{bot_info.BOT_USERNAME}?startgroup=true")
             ],[
             InlineKeyboardButton("ℹ️ ʜᴇʟᴩ", callback_data="help"),
             InlineKeyboardButton("😎 ᴀʙᴏᴜᴛ", callback_data="about") 
             ],[
             InlineKeyboardButton("🗳 ᴜᴩᴅᴀᴛᴇꜱ ᴄʜᴀɴɴᴇʟ", url="https://t.me/XRoiD_BotZ"),
             InlineKeyboardButton("🤖 ꜱᴜᴩᴩᴏʀᴛ ɢʀᴏᴜᴩ", url="https://t.me/XRoid_Support")
             ]]
        else:
            buttons = [[
             InlineKeyboardButton("➕️ ᴀᴅᴅ ᴍᴇ ᴛᴏ yᴏᴜʀ ᴄʜᴀᴛ ➕️", url=f"http://t.me/{bot_info.BOT_USERNAME}?startgroup=true")
             ],[
             InlineKeyboardButton("ℹ️ ʜᴇʟᴩ", callback_data="bot_owner"),
             InlineKeyboardButton("😎 ᴀʙᴏᴜᴛ", callback_data="about") 
             ],[
             InlineKeyboardButton("🗳 ᴜᴩᴅᴀᴛᴇꜱ ᴄʜᴀɴɴᴇʟ", url="https://t.me/XRoiD_BotZ"),
             InlineKeyboardButton("🤖 ꜱᴜᴩᴩᴏʀᴛ ɢʀᴏᴜᴩ", url="https://t.me/XRoid_Support")
             ]]    
        await message.reply_photo(photo = choice(BOT_PICS), caption=START_MSG.format(mention = message.from_user.mention, bot_name = bot_info.BOT_NAME, bot_username = bot_info.BOT_USERNAME), reply_markup=InlineKeyboardMarkup(buttons))
        
    elif len(message.command) ==2 and message.command[1] in ["subscribe"]:
        FORCES=["https://telegra.ph/file/536bc12cd8b87bfe6eb86.jpg"]
        invite_link = await bot.create_chat_invite_link(int(FORCES_SUB))
        button=[[
         InlineKeyboardButton("🔔 SUBSCRIBE 🔔", url=invite_link.invite_link)
         ]]
        reply_markup = InlineKeyboardMarkup(button)
        await message.reply_photo(
            photo=choice(FORCES),
            caption=f"""<i><b>Hello {message.from_user.mention}. \nYou Have <a href="{invite_link.invite_link}">Not Subscribed</a> To <a href="{invite_link.invite_link}">My Update Channel</a>.So you do not get the Files on Inline Mode, Bot Pm and Group</i></b>""",
            reply_markup=reply_markup
        )
        return
   
@LuciferMoringstar_Robot.on_message(Worker.private & Worker.command(["help"]))
async def help(bot, message):
    button = [[
     InlineKeyboardButton("🏠 Home", callback_data="start"),
     InlineKeyboardButton("About 😎", callback_data="about")
     ]]
    await message.reply_photo(
        photo = choice(BOT_PICS),
        caption=LuciferMoringstar.HELP_MSG.format(mention=message.from_user.mention),
        reply_markup=InlineKeyboardMarkup(button))
      
@LuciferMoringstar_Robot.on_message(Worker.private & Worker.command(["about"]))
async def about(bot, message):
    button = [[
     InlineKeyboardButton("🏠 Home", callback_data="start"),
     InlineKeyboardButton("Close 🗑️", callback_data="close")
     ]]  
    await message.reply_photo(
        photo = choice(BOT_PICS),
        caption=LuciferMoringstar.ABOUT_MSG.format(mention=message.from_user.mention, bot_name=bot_info.BOT_NAME, bot_username=bot_info.BOT_USERNAME, dev_name=DEV_NAME),
        reply_markup=InlineKeyboardMarkup(button))
        
