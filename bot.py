import sys
import glob
import importlib
import logging
import logging.config
import pytz
import asyncio
from pathlib import Path
from datetime import date, datetime
from aiohttp import web
from pyrogram import Client, __version__
from pyrogram.raw.all import layer
from database.ia_filterdb import Media
from database.users_chats_db import db
from info import *
from utils import temp
from plugins import web_server
from TechVJ.bot import TechVJBot
from TechVJ.util.keepalive import ping_server
from TechVJ.bot.clients import initialize_clients
from pyrogram import types

ppath = "plugins/*.py"
files = glob.glob(ppath)

# Configure logging
logging.config.fileConfig('logging.conf')
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("imdbpy").setLevel(logging.ERROR)

class Bot(Client):
    def __init__(self):
        super().__init__(
            name=SESSION,
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=50,
            plugins={"root": "plugins"},
            sleep_threshold=5,
        )

async def initialize_plugins():
    for name in files:
        with open(name) as a:
            patt = Path(a.name)
            plugin_name = patt.stem.replace(".py", "")
            plugins_dir = Path(f"plugins/{plugin_name}.py")
            import_path = f"plugins.{plugin_name}"
            spec = importlib.util.spec_from_file_location(import_path, plugins_dir)
            load = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(load)
            sys.modules[import_path] = load
            print(f"Tech VJ Imported => {plugin_name}")

async def start():
    print('\n')
    print('Initializing Your Bot')
    bot = Bot()
    await bot.start()
    
    # Initialize clients and plugins
    await initialize_clients()
    await initialize_plugins()
    
    # Ping server if running on Heroku
    if ON_HEROKU:
        asyncio.create_task(ping_server())
    
    # Load banned users and chats
    b_users, b_chats = await db.get_banned()
    temp.BANNED_USERS = b_users
    temp.BANNED_CHATS = b_chats
    
    # Ensure indexes for Media
    await Media.ensure_indexes()
    
    # Get bot information
    me = await TechVJBot.get_me()
    temp.ME = me.id
    temp.U_NAME = me.username
    temp.B_NAME = me.first_name
    
    # Logging and information
    logging.info(f"{me.first_name} with Pyrogram v{__version__} (Layer {layer}) started on {me.username}.")
    logging.info(LOG_STR)
    
    # Send restart message
    tz = pytz.timezone('Asia/Kolkata')
    today = date.today()
    now = datetime.now(tz)
    time = now.strftime("%H:%M:%S %p")
    await TechVJBot.send_message(chat_id=LOG_CHANNEL, text=script.RESTART_TXT.format(today, time))
    
    # Configure and start web server
    app = web.Application()
    app.add_routes([web.get('/', web_server)])
    runner = web.AppRunner(app)
    await runner.setup()
    bind_address = '0.0.0.0'
    await web.TCPSite(runner, bind_address, PORT).start()

async def stop():
    await TechVJBot.stop()
    logging.info("Bot stopped. Bye.")

if __name__ == '__main__':
    try:
        asyncio.run(start())
    except KeyboardInterrupt:
        asyncio.run(stop())
