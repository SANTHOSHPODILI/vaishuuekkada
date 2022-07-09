from pyrogram3 import Client, filters

vaishuu=Client(
       "vaishali x music new",
       api_hash="47cf60c015aa84694b97f3d993d97dd8",
       api_id="17214501",
       bot_token="5580562376:AAEGH3FPDnJUJrVK41DII7WHQK-H2Boemdc
", 
) 

@vaishuu.on_message(filter.command("start") & filter.group)
async def start(bot, message):
    await message.reply_photo(
        photo="https://te.legra.ph/file/d25be28a8f9043ed08821.jpg",
        caption="Hello user i am official pyogram bot how can i help you",
           
    )        
           


vaishuu.run() 
