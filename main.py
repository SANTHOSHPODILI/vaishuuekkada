from pyrogram import Client, filters

vaishuu=Client(
       "vaishali x music new",
       api_hash="",
       api_id="",
       bot_token="", 
) 

@vaishuu.on_message(filters.command("start"))
async def start(bot, message):
       await message.reply_text("Hello user iam a official pyrogram music bot")
    
@vaishuu.on_message(filters.command("help"))
async def help(bot, message):
       await message.reply_text("hello user this is my help buttons click help")


vaishuu.run() 
