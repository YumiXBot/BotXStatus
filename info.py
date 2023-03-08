import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot settings
BUTTON = True
USE_CAPTION_FILTER = True
BROADCAST_AS_COPY = True
BROADCAST_ADMIN_ID = [5038784553]


# MongoDB information
DATABASE_URI = "mongodb+srv://Rakesh:Rakesh@cluster0.r28mu.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
DATABASE_NAME = "Cluster0"
COLLECTION_NAME = 'Telegram_files_rakesh'


# Bot information
SESSION = 'Media_search'
API_ID = 13292294
API_HASH = "68cf86881e7d9e706a3c886471ffdc21"
BOT_TOKEN = "5044256210:AAEXDpYvbpwzsE90zozNjwZt-wjGoXfyM6Y"


# Admins, Channels & Users
ADMINS = [5038784553, 1442442077]
CHANNELS = [-1001444993900]
auth_users = []
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
AUTH_CHANNEL = -1001330862638
AUTH_GROUPS = []


# PICS LINKS
default_pics_links = """
https://telegra.ph/file/0fa6431e2d6bc7afe5c5e.jpg
https://telegra.ph/file/02ebd3c876fe1544d8b62.jpg
https://telegra.ph/file/7e56d907542396289fee4.jpg
https://telegra.ph/file/9aa8dd372f4739fe02d85.jpg
https://telegra.ph/file/adffc5ce502f5578e2806.jpg
https://telegra.ph/file/6937b60bc2617597b92fd.jpg
https://telegra.ph/file/09a7abaab340143f9c7e7.jpg
https://telegra.ph/file/5a82c4a59bd04d415af1c.jpg
https://telegra.ph/file/323986d3bd9c4c1b3cb26.jpg
https://telegra.ph/file/b8a82dcb89fb296f92ca0.jpg
https://telegra.ph/file/31adab039a85ed88e22b0.jpg
https://telegra.ph/file/c0e0f4c3ed53ac8438f34.jpg
https://telegra.ph/file/eede835fb3c37e07c9cee.jpg
https://telegra.ph/file/e17d2d068f71a9867d554.jpg
https://telegra.ph/file/8fb1ae7d995e8735a7c25.jpg
https://telegra.ph/file/8fed19586b4aa019ec215.jpg
https://telegra.ph/file/8e6c923abd6139083e1de.jpg
https://telegra.ph/file/0049d801d29e83d68b001.jpg
"""
PICS = (environ.get('PICS', default_pics_links)).split()


### Start Messages ###
default_start_msg = """
𝐇𝐞𝐥𝐥𝐨 🔏
𝐈 𝐂𝐚𝐧 𝐏𝐫𝐨𝐯𝐢𝐝𝐞 𝐌𝐨𝐯𝐢𝐞𝐬 😍
𝐉𝐮𝐬𝐭 𝐀𝐝𝐝 𝐌𝐞 𝐈𝐧 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩 😈
𝐌𝐚𝐤𝐞 𝐀𝐝𝐦𝐢𝐧 𝐀𝐧𝐝 𝐄𝐧𝐉𝐨𝐲 𝐔𝐧𝐥𝐢𝐦𝐢𝐭𝐞𝐝 𝐌𝐨𝐯𝐢𝐞𝐬 🤭
"""
START_MSG = environ.get('START_MSG', default_start_msg)


### Custom Caption ###
default_file_caption = """
📁 [@RymOfficial {file_name}](https://t.me/RymOfficial)
★━━━━━━ ⊛ 🇮🇳 ⊛ ━━━━━━★
╔══⚘⚚ Jᴏɪɴ Oᴜʀ Nᴇᴛᴡᴏʀᴋ ⚘⚚═══╗
☞ Nᴇᴛᴡᴏʀᴋ @RymOfficial         ☜
☞ Mᴏᴠɪᴇs @SonalModdingGod      ☜
☞ Sᴜᴘᴘᴏʀᴛ @JaiHindChatting     ☜
╚══⚘⚚ Jᴏɪɴ Oᴜʀ Nᴇᴛᴡᴏʀᴋ ⚘⚚═══╝
♥️ 𝗧𝗲𝗮𝗺 ➜ [𝐑𝐲𝐦 𝐎𝐟𝐟𝐢𝐜𝐢𝐚𝐥](https://t.me/RymOfficial)
★━━━━━━ ⊛ 🇮🇳 ⊛ ━━━━━━★
"""
FILE_CAPTION = environ.get('CUSTOM_CAPTION_FILE', default_file_caption)


OMDB_API_KEY = environ.get("OMDB_API_KEY", "")
if FILE_CAPTION.strip() == "":
    CUSTOM_FILE_CAPTION=None
else:
    CUSTOM_FILE_CAPTION=FILE_CAPTION
if OMDB_API_KEY.strip() == "":
    API_KEY=None
else:
    API_KEY=OMDB_API_KEY
