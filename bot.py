from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup

# Replace these with your actual values
API_ID = 23936353
API_HASH = 'f6e329e7b2a81427e93c4e6fed1af81c'
BOT_TOKEN = '6518559992:AAGmFaHx7RuU8MDXyZRIBxxLqOYoIp5vNiE'

app = Client("delete_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@ app.on_message(filters.command("start"))
def start(_, message):
    message.reply_text("Hello! I am your delete bot. Use /delete, /deleteall, or /deleteform to delete messages.")

@ app.on_message(filters.command("delete") & filters.reply)
def delete_message(_, message):
    reply_message: Message = message.reply_to_message
    if reply_message:
        reply_message.delete()
        message.reply_text("Message deleted successfully!")

@ app.on_message(filters.command("deleteall"))
def delete_all(_, message):
    buttons = [
        [InlineKeyboardButton("Yes", callback_data="confirm_deleteall"),
         InlineKeyboardButton("No", callback_data="cancel_deleteall")]
    ]
    markup = InlineKeyboardMarkup(buttons)
    app.send_message(message.chat.id, "Are you sure you want to delete all messages?", reply_markup=markup)

@ app.on_message(filters.command("deleteform") & filters.reply)
def delete_from_message(_, message):
    app.send_message(message.chat.id, "Select the first message you want to delete from, then reply with /s.")

@ app.on_message(filters.command("s") & filters.reply)
def delete_from_selected_message(_, message):
    app.send_message(message.chat.id, "Select the last message you want to delete, then reply with /sall.")

@ app.on_message(filters.command("sall") & filters.reply)
def delete_selected_range(_, message):
    buttons = [
        [InlineKeyboardButton("Yes", callback_data="confirm_deleteform"),
         InlineKeyboardButton("No", callback_data="cancel_deleteform")]
    ]
    markup = InlineKeyboardMarkup(buttons)
    app.send_message(message.chat.id, "Are you sure you want to delete the selected range of messages?", reply_markup=markup)

def main():
    print("Starting the bot...")
    app.run()

if __name__ == "__main__":
    main()
