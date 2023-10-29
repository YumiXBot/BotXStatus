import os

from os import getenv


API_ID = int(getenv("API_ID", "26850449"))
API_HASH = getenv("API_HASH", "72a730c380e68095a8549ad7341b0608")
SESSION_STRING = getenv("SESSION_STRING", "BQCzTb8AIiPEa721vB0hL6EXw6FXWAbvxlTEOmAWbMJ_ftK7fRY_tHqIPYWdhnZ10r8H6gSwQj0n8YE6rHSjlLpeONToywAkntIWL89wW5uwpai1C6Htx5rYC8_TrqTKlo03xEIhU_dB1eiaAIiD8f-ggY-LHpd25p1HLzjbFT7rakGqvO3p1RJG3PkKJwaUatcJLLxu-C1p8CN_iNEZb-ekjUX1ndpNMUELkcmYREbvdPuwcIARc5iINie-oYZ28Z2o0vXfClpqEa51kTcydJkSAg5n8b78UvjmSWg1EiJy2ytzoli6-1ULYRo3AIoOaULCqvPZv77HAFP7VJUpPq4oCwFLaQAAAABqwr10AA")
GROUP_ID = int(getenv("GROUP_ID", "-1001819089478"))
CHANNEL_OR_GROUP_ID = int(getenv("CHANNEL_OR_GROUP_ID", "-1002135419834"))
MESSAGE_ID = int(getenv("MESSAGE_ID", "3"))
CHANNEL_NAME = getenv("CHANNEL_NAME", "˹ᴀʟᴏɴᴇ 〄 ᴜᴘᴅᴀᴛᴇs˼")
TIME_ZONE = getenv("TIME_ZONE", "Asia/Kolkata")
BOT_LIST = list(getenv("BOT_LIST", "AloneXRobot AloneXMusicBot AloneXOneBot AloneXTwoBot AloneXThreeBot AloneXFourBot AloneXFiveBot").split())
BOT_ADMIN_IDS = list(map(int, getenv("BOT_ADMIN_IDS", "6079943111").split()))
