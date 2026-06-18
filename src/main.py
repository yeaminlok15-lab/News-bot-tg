import asyncio
from telegram.ext import ApplicationBuilder, CommandHandler
from src.database import init_db

async def start(update, context):
    await update.message.reply_text("বটটি রেডি! নিউজ আসা শুরু হবে।")

async def main():
    await init_db()
    app = ApplicationBuilder().token("YOUR_TELEGRAM_TOKEN").build()
    
    app.add_handler(CommandHandler("start", start))
    
    print("Bot is running...")
    await app.run_polling()

if __name__ == '__main__':
    asyncio.run(main())
