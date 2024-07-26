import os

# Retrieve environment variables and convert them to the appropriate types
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
OWNER_ID = int(os.getenv("OWNER_ID"))


# Database connection URL
MONGO_URL = os.getenv("MONGO_URL")
