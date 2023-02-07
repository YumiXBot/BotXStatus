import os

from os import getenv


API_ID = int(getenv("API_ID", "26850449"))
API_HASH = getenv("API_HASH", "72a730c380e68095a8549ad7341b0608")
SESSION_STRING = getenv("SESSION_STRING", "")
GROUP_ID = int(getenv("GROUP_ID", "-1001328686560"))
CHANNEL_OR_GROUP_ID = int(getenv("CHANNEL_OR_GROUP_ID", "-1001637830162"))
MESSAGE_ID = int(getenv("MESSAGE_ID", "30"))
CHANNEL_NAME = getenv("CHANNEL_NAME", "ᴛᴇʟᴇ ʙᴏᴛ 🍂ᴜᴘᴅᴀᴛᴇs'")
TIME_ZONE = getenv("TIME_ZONE", "Asia/Kolkata")
BOT_LIST = list(getenv("BOT_LIST", "ViewsServiceBot The_ScraperBot MrsServiceBot MrsFallenBot").split())
BOT_ADMIN_IDS = list(map(int, getenv("BOT_ADMIN_IDS", "6196151348").split()))
