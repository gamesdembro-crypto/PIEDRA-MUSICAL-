import random
import asyncio
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.environ.get("TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

songs = [
    "https://youtu.be/dQw4w9WgXcQ",
    "https://youtu.be/3tmd-ClpJxA",
    "https://youtu.be/fJ9rUzIMcZQ",
    "https://youtu.be/kJQP7kiw5Fk"
]

async def music(update: Update, context: ContextTypes.DEFAULT_TYPE):
    song = random.choice(songs)
    await update.message.reply_text(f"🎵 Вот случайная песня:\n{song}")

async def auto_music(context: ContextTypes.DEFAULT_TYPE):
    song = random.choice(songs)
    await context.bot.send_message(chat_id=CHAT_ID, text=f"🎶 Авто-песня:\n{song}")

async def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("music", music))

    # Автоматическая отправка каждые 30 минут
    app.job_queue.run_repeating(auto_music, interval=1800, first=10)

    print("Бот запущен 🚀")
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
