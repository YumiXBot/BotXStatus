import os

from os import getenv


API_ID = int(getenv("API_ID", "26850449"))
API_HASH = getenv("API_HASH", "72a730c380e68095a8549ad7341b0608")
SESSION_STRING = getenv("SESSION_STRING", "BQAWvR-dIMXeyIIPIhP4VAfbLnyHLqoYv3vpumNArZeU84yqotqP9y1dFg_CLw1xo8hEX8tGXE2ZUbPyTg_sg0AQLFoQhCqXrflvFzdmoe-GcV7UGGENjd5Y_2VW_V0cOo0lN1PNZuDmAMZOJZbJ1qL6l_fNZVASyuls7H47ZFHun8Nl4sK7rt21KpogxlPLTnSJks_NyaUBk5smZPCgYZNp9aeGq4UJuGN6nJM3uwESr9ieKqQWUYBtlixJf1nZKkmGZMiyTgQ4ZWR8O8auzpYN3I0vjo6gaB-s5TjhLFtBluaFmc39wb-1MIoQt68jkjFuM4rbGfnRZPP0fft97VBHAAAAAWwoXUEA")
GROUP_ID = int(getenv("GROUP_ID", "-1001760687773"))
CHANNEL_OR_GROUP_ID = int(getenv("CHANNEL_OR_GROUP_ID", "-1001831916389"))
MESSAGE_ID = int(getenv("MESSAGE_ID", "158"))
CHANNEL_NAME = getenv("CHANNEL_NAME", "˹ᴍᴏᴠɪᴇs 〄 ᴜᴘᴅᴀᴛᴇs˼")
TIME_ZONE = getenv("TIME_ZONE", "Asia/Kolkata")
BOT_LIST = list(getenv("BOT_LIST", "TheFunkyFoxBot TheHinataBot TheHanCockBot TheFiltersBot").split())
BOT_ADMIN_IDS = list(map(int, getenv("BOT_ADMIN_IDS", "5709622852").split()))
