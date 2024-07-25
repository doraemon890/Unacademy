import os

# Retrieve environment variables and convert them to the appropriate types
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
BOT_USERNAME = os.getenv("BOT_USERNAME")
OWNER_ID = int(os.getenv("OWNER_ID"))

# Define fixed values
SUDO_USERS = "7044783841"
CHANNEL_ID = "-1002094238295"

# Database connection URL
MONGO_URL = os.getenv("MONGO_URL")
