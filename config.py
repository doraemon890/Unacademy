
import os
from os import getenv

API_ID = int(os.environ.get("API_ID"))

API_HASH = os.environ.get("API_HASH")

BOT_TOKEN = os.environ.get("BOT_TOKEN")
BOT_USERNAME = os.environ.get("BOT_USERNAME")
OWNER_ID = int(os.environ.get("OWNER_ID"))

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
CHANNEL_ID = int(os.environ.get("CHANNEL_ID"))
MONGO_URL = os.environ.get("MONGO_URL")
