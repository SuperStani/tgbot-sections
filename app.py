from pyrogram import Client
from pyrogram.handlers import MessageHandler
from pyrogram.handlers import CallbackQueryHandler
import messages
import callbackdata

api_id = 00000
api_hash = ""
app = Client("my_bot", api_id, api_hash)

app.add_handler(MessageHandler(messages.messages_response))
app.add_handler(CallbackQueryHandler(callbackdata.callback_response))


app.run()

#python3 /path/app.py
