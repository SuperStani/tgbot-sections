from pyrogram.types import InlineKeyboardMarkup as Keyboard
from pyrogram.types import InlineKeyboardButton as Button

import database as db

async def callback_response(App, query):
    user_id = query.from_user.id
    section, update_data = query.data.split(":", 2)
    params = update_data.split("|")
    data = params[0]
    
    #----------------------------------SECTION HOME-----------------------------------------#
    if section == "home":
        if data == "start":
            keyboard = Keyboard([
                [Button("➕ NEW POST", "post:new")],
                [Button("SHOW ALL POSTS", "post:showall")]
            ])
            text = "Welcome"
            await query.edit_message_text(text, reply_markup=keyboard)
            db.page("home:start")
            
    elif section == "post":
      if data == "new":
          keyboard = Keyboard([
                [Button("GO BACK", "home:start")]
          ])
          await query.edit_message_text("Ok, send me the title:", reply_markup=keyboard)
          db.page("post:title", user_id)
          
      elif data == "showall":
          posts = db.rquery("SELECT id, title FROM posts", one=False)
          keyboard = Keyboard([
                [Button("GO BACK", "home:start")]
          ])
          text = "POSTS LIST\n\n"
          for post in posts:
              text += f"{post[0]}: {post[1]}\n"
          await query.edit_message_text(text, reply_markup=keyboard)
          db.page("post:showall", user_id)
