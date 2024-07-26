import asyncio
import logging
from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN

# Configure logging
logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s",
    level=logging.INFO,
)

# Initialize the event loop
loop = asyncio.get_event_loop()

# Initialize the Pyrogram client
app = Client(
    ":Ava:",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
)

async def info_bot():
    global BOT_ID, BOT_NAME
    
    # Start the client
    await app.start()
    
    # Retrieve bot information
    getme = await app.get_me()
    BOT_ID = getme.id
    BOT_NAME = f"{getme.first_name} {getme.last_name}" if getme.last_name else getme.first_name

# Run the info_bot function until complete
loop.run_until_complete(info_bot())
