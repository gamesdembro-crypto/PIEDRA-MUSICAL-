import random
import asyncio
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

songs = [
    "https://youtu.be/dQw4w9WgXcQ",
    "https://youtu.be/3tmd-ClpJxA",
    "https://youtu.be/fJ9rUzIMcZQ",
    "https://youtu.be/kJQP7kiw5Fk"
]

async def random_song(update: Update, context: ContextTypes.DEFAULT_TYPE):
    song = random.choice(songs)
    await update.message.reply_text(f"🎵 Рандомная песня:\n{song}")

async def auto_music(app):
    while True:
        song = random.choice(songs)
        await app.bot.send_message(chat_id=CHAT_ID, text=f"🎶 Авто-песня:\n{song}")
        await asyncio.sleep(1800)

async def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("music", random_song))
    asyncio.create_task(auto_music(app))
    await app.run_polling()

asyncio.run(main())
