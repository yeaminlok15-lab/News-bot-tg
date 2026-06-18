import aiosqlite

async def init_db():
    async with aiosqlite.connect("news_bot.db") as db:
        await db.execute('''CREATE TABLE IF NOT EXISTS articles 
                            (id INTEGER PRIMARY KEY, title TEXT UNIQUE, url TEXT, summary TEXT)''')
        await db.execute('''CREATE TABLE IF NOT EXISTS sources 
                            (id INTEGER PRIMARY KEY, name TEXT, url TEXT)''')
        await db.commit()
