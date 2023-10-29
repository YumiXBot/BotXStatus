import os

from os import getenv


API_ID = int(getenv("API_ID", "26850449"))
API_HASH = getenv("API_HASH", "72a730c380e68095a8549ad7341b0608")
SESSION_STRING = getenv("SESSION_STRING", "BQCzTb8AYQ4o4Ew8D6uaSspcnpkrAoBWfYAn6Sc_XFeGF9K2PjoOXRpM7MoPW-OXUekIqc3u4WCvKwqx8QWyr6Sllpc_MH7aStOufb7MsvRuI-1tpJKoghy9kJAazi1m8oxb8N-MAjch5ZQDkN48hxL_jGPB0IX7D2xwrOCVOuZ8dVw8K-o8NFzjxcSyfvKfxEkrxV7X7NP6DITRYZH8F_MHzISWA1ljxgLEB-5xtA4rcx9WFOmV6sjZht8S9kPXliMHb7y-EulWN9xxyd47xLapgtwsmrdumF44Cr5_PFjmIJYoiPlYnrogynWpoysNcTp2j6vlxkG6Ay49ro65-gdGOXD7HQAAAABqwr10AA")
GROUP_ID = int(getenv("GROUP_ID", "-1001819089478"))
CHANNEL_OR_GROUP_ID = int(getenv("CHANNEL_OR_GROUP_ID", "-1002135419834"))
MESSAGE_ID = int(getenv("MESSAGE_ID", "3"))
CHANNEL_NAME = getenv("CHANNEL_NAME", "˹ᴀʟᴏɴᴇ 〄 ᴜᴘᴅᴀᴛᴇs˼")
TIME_ZONE = getenv("TIME_ZONE", "Asia/Kolkata")
BOT_LIST = list(getenv("BOT_LIST", "AloneXRobot AloneXMusicBot AloneXOneBot AloneXTwoBot AloneXThreeBot AloneXFourBot AloneXFiveBot").split())
BOT_ADMIN_IDS = list(map(int, getenv("BOT_ADMIN_IDS", "6079943111").split()))
