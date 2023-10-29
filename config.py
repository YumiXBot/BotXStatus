import os

from os import getenv


API_ID = int(getenv("API_ID", "26850449"))
API_HASH = getenv("API_HASH", "72a730c380e68095a8549ad7341b0608")
SESSION_STRING = getenv("SESSION_STRING", "BQBI1LPXrt5NRAPDMClbmk8UCbSah6XF1BYGkBomSWoOdrZVAr918cmXNcRciSQwMtxthSHCCJaqey4ItjXewgbCixNZdK9rBzUueLVxL_JctFvmIMMAvyhQpX8Z251YttsVJ2te_g1I04wg5PSE5Gc_UrPqdhm2ZX9CQGeLpYNptraAakUuvfuiOoUpC3qHleZ_7F_2Wo0Vn39_oUjn5H3RMWxzSsHnE3LXqLjMU1IIj3Alo-GNGaUTNWef1T0tgoS6ly0Ie9P2zqbnrz0waWK226kUU-iVr5_MFmVNbTcfOnaO9DKB78kT9Hp5P_TZ_iSTYtBt-rzCLXVxEMheF87dAAAAAVKUpfgA")
GROUP_ID = int(getenv("GROUP_ID", "-1001819089478"))
CHANNEL_OR_GROUP_ID = int(getenv("CHANNEL_OR_GROUP_ID", "-1002135419834"))
MESSAGE_ID = int(getenv("MESSAGE_ID", "3"))
CHANNEL_NAME = getenv("CHANNEL_NAME", "˹ᴀʟᴏɴᴇ 〄 ᴜᴘᴅᴀᴛᴇs˼")
TIME_ZONE = getenv("TIME_ZONE", "Asia/Kolkata")
BOT_LIST = list(getenv("BOT_LIST", "AloneXRobot AloneXMusicBot AloneXOneBot AloneXTwoBot AloneXThreeBot AloneXFourBot AloneXFiveBot").split())
BOT_ADMIN_IDS = list(map(int, getenv("BOT_ADMIN_IDS", "6079943111").split()))
