import asyncio
import importlib
from pyrogram import idle
from Ava.modules import ALL_MODULES

# Initialize the event loop
loop = asyncio.get_event_loop()

async def raven_boot():
    # Import all modules listed in ALL_MODULES
    for module in ALL_MODULES:
        importlib.import_module(f"Ava.modules.{module}")

    print("» ʙᴏᴛ ᴅᴇᴘʟᴏʏᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ ✅")
    await idle()
    print("» ɢᴏᴏᴅ ʙʏᴇ! sᴛᴏᴘᴘɪɴɢ ʙᴏᴛ.")

# Run the raven_boot function if this script is executed
if __name__ == "__main__":
    loop.run_until_complete(raven_boot())
