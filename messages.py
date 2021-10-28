from pyrogram.types import InlineKeyboardMarkup as Keyboard
from pyrogram.types import InlineKeyboardButton as Button

import database as db

async def messages_response(App, message):
    try:
        user_id = message.from_user.id
    except:
        user_id = message.chat.id
        
    if message.entities is not None and message.entities[0].type == 'bot_command':
        await command_response(App, message, user_id)
    else:
        page = db.getPage(user_id)
        section, update_data = page.split(":", 2)
        params = update_data.split("|")
        data = params[0]
        
        if message.text is not None:
            #----------------------------------> POST SECTION <---------------------------------------#
            if section == "post":
                if data == "title":
                    post_id = db.wquery("INSERT INTO posts SET title = %s", message.text)
                    keyboard = Keyboard([
                        [Button("GO BACK", "home:home|param1|param2")], #params are optional
                    ])
                    await message.reply("Ok, send me the description", reply_markup=keyboard)
                    db.page(f"post:description|{post_id}", user_id)
                    
                elif data == "description":
                    post_id = params[1]
                    #.......SOME CODE HERE.........
                    
            #----------------------------------> ANOTHER SECTION <-------------------------------------#
            elif section == "anotther_section":
                if data == "some_data":
                    pass
                elif data == "some_data":
                    pass
                  
        elif message.photo is not None:
            if section == "":
                if data == "":
                    pass
                  
async def command_response(App, message, chat_id):
    command = message.text
    if command == "/start":
        await message.reply("Hello, the bot is online!")
        db.page("home:start", chat_id)
