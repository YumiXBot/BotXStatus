import os
import re
import pytz
import asyncio
import datetime
from pyrogram import Client, filters
from pyrogram.errors import FloodWait


app = Client(
    name = "sumit",
    api_id = int(os.environ["27878007"]),
    api_hash = os.environ["61e70418c7c29d0ce7fe2cc181950ae0"],
    session_string = os.environ["AQAO4fJXBdUpd7GtEdFOqGJP9sIHldgWZCXY9KQo_TdP43C2imyOIPAJw-TBOvierXq8b_PzZQqTluIWUTBY-xEMa5XUrJvyqvlL5hM04k2NiUfn38GFr_IfYlNg_6-Ua3g_GCWBNIgXBNPMHNbRQqkE8rfzit_2K22Zh0fmhRKkuJS-Iu-2aQsGAg4saSQgi4vM5F2V7Jf24ikgCoEc_iDa8Gx1o6kCdk7_CvjJ1K1TGTFAVynLBRO-EpI72FsbYnMOSU1LudkDq-q5BA0XPOeHdC0o6E7QrFWf3y-Q64n_hKFVeIGoxzY2azwIuE_7QCIA8ZJzLhUutwHCnEsEdwHTAAAAAVyIB7AA"]
)

TIME_ZONE = os.environ["Asia/Kolkata"]
BOT_LIST = [i.strip() for i in os.environ.get("@MrsNatashaBot, @AnonMusicBot, @NixaRobot").split(' ')]
CHANNEL_OR_GROUP_ID = int(os.environ["-1001827333320"])
MESSAGE_ID = int(os.environ["1"])
BOT_ADMIN_IDS = [int(i.strip()) for i in os.environ.get("5616461719").split(' ')]
GRP_ID = os.environ.get("-1001801801469")
CHANNEL_NAME = os.environ.get("ʙᴏᴛs ᴜᴘᴅᴀᴛᴇ")

async def main_status():
    async with app:
            while True:
                print("ᴄʜᴇᴄᴋɪɴɢ...")
                xxx_teletips = f"<u>**🏷 ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ {CHANNEL_NAME} ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴄʜᴀɴɴᴇʟ**</u>\n\n 📈 | <u>**ʀᴇᴀʟ ᴛɪᴍᴇ ʙᴏᴛ's sᴛᴀᴛᴜs 🍂**</u>"
                for bot in BOT_LIST:
                    await asyncio.sleep(7)
                    try:
                        bot_info = await app.get_users(bot)
                    except Exception:
                        bot_info = bot

                    try:
                        yyy_teletips = await app.send_message(bot, "/start")
                        aaa = yyy_teletips.id
                        await asyncio.sleep(15)
                        zzz_teletips = app.get_chat_history(bot, limit = 1)
                        async for ccc in zzz_teletips:
                            bbb = ccc.id
                        if aaa == bbb:
                            xxx_teletips += f"\n\n╭⎋ **[{bot_info.first_name}](tg://user?id={bot_info.id})**\n╰⊚ **sᴛᴀᴛᴜs: ᴏғғʟɪɴᴇ ❄**"
                            for bot_admin_id in BOT_ADMIN_IDS:
                                try:
                                    await app.send_message(int(GRP_ID), f"**ʙsᴅᴋ ᴋʏᴀ ᴋᴀʀ ʀᴀʜᴀ ʜᴀɪ 😡\n[{bot_info.first_name}](tg://user?id={bot_info.id}) ᴏғғ ʜᴀɪ. ᴀᴄᴄʜᴀ ʜᴜᴀ ᴅᴇᴋʜ ʟɪʏᴀ ᴍᴀɪɴᴇ.**")
                                except Exception:...
                            await app.read_chat_history(bot)
                        else:
                            xxx_teletips += f"\n\n╭⎋ **[{bot_info.first_name}](tg://user?id={bot_info.id})**\n╰⊚ **sᴛᴀᴛᴜs: ᴏɴʟɪɴᴇ ✨**"
                            await app.read_chat_history(bot)
                    except FloodWait as e:
                        ttm = re.findall("\d{0,5}", str(e))
                        await asyncio.sleep(int(ttm))
                time = datetime.datetime.now(pytz.timezone(f"{TIME_ZONE}"))
                last_update = time.strftime(f"%d %b %Y at %I:%M %p")
                xxx_teletips += f"\n\n✔️ <u>ʟᴀsᴛ ᴄʜᴇᴄᴋᴇᴅ ᴏɴ:</u>\n**ᴅᴀᴛᴇ & ᴛɪᴍᴇ: {last_update}**\n**ᴛɪᴍᴇ ᴢᴏɴᴇ: ({TIME_ZONE})**\n\n<i><u>♻️ ʀᴇғʀᴇsʜᴇs ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴡɪᴛʜɪɴ 10 ᴍɪɴᴜᴛᴇs.</u></i>\n\n<i>**๏ ᴘᴏᴡᴇʀᴇᴅ ʙʏ sᴜᴍɪᴛ ʏᴀᴅᴀᴠ ๏**</i>"
                await app.edit_message_text(int(CHANNEL_OR_GROUP_ID), MESSAGE_ID, xxx_teletips)
                print(f"ʟᴀsᴛ ᴄʜᴇᴄᴋᴇᴅ ᴏɴ: {last_update}")                
                await asyncio.sleep(600)
                        
app.run(main_status())
