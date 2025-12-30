# +++ Modified By @Codeflix_Bots

import os
import re
import logging
from logging.handlers import RotatingFileHandler

# Regex
id_pattern = re.compile(r"-?\d+")

# ================= BOT CREDENTIALS =================

TG_BOT_TOKEN = "8225598276:AAGH5UsdyQvGvEtQFHJztW4gm0fNpPZo22M"
APP_ID = 23562992
API_HASH = "e070a310ca3e76ebc044146b9829237c"

OWNER_ID = 7524032836
PORT = 8080

# ================= DATABASE =================

DB_URI = "mongodb+srv://rj5706603:O95nvJYxapyDHfkw@cluster0.fzmckei.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
DB_NAME = "link"

DATABASE_CHANNEL = -1001234567890  # CHANGE if needed

# ================= AUTO APPROVE =================

CHAT_ID = []
TEXT = (
    "<b>{mention},\n\n"
    "ʏᴏᴜʀ ʀᴇǫᴜᴇsᴛ ᴛᴏ ᴊᴏɪɴ {title} ɪs ᴀᴘᴘʀᴏᴠᴇᴅ.\n\n"
    "‣ ᴘᴏᴡᴇʀᴇᴅ ʙʏ @narzoxbot</b>"
)
APPROVED = "on"

# ================= WORKERS =================

TG_BOT_WORKERS = 40

# ================= START =================

START_PIC = "https://telegra.ph/file/f3d3aff9ec422158feb05-d2180e3665e0ac4d32.jpg"

START_MSG = (
    "<b>ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛʜᴇ ᴀᴅᴠᴀɴᴄᴇᴅ ʟɪɴᴋs sʜᴀʀɪɴɢ ʙᴏᴛ.\n\n"
    "ᴛʜɪs ʙᴏᴛ ʜᴇʟᴘs ʏᴏᴜ sʜᴀʀᴇ ʟɪɴᴋs sᴀғᴇʟʏ.</b>"
)

HELP = (
    "<b>"
    "» Creator: <a href='https://t.me/Teamrajweb'>Raj</a>\n"
    "» Community: <a href='https://t.me/narzoxbot'>Narzo Team</a>\n"
    "» Developer: <a href='https://t.me/onlymrabhi'>Abhi</a>"
    "</b>"
)

ABOUT = (
    "<b>This bot securely shares Telegram invite links "
    "with auto revoke protection.</b>"
)

ABOUT_TXT = (
    "<b>"
    "›› Owner: <a href='https://t.me/cosmic_freak'>Raj</a>\n"
    "›› Language: Python 3\n"
    "›› Library: Pyrogram v2\n"
    "›› Database: MongoDB\n"
    "›› Developer: @onlymrabhi"
    "</b>"
)

CHANNELS_TXT = (
    "<b>"
    "›› Anime: <a href='https://t.me/narzoxbot'>Anime Cruise</a>\n"
    "›› Movies: <a href='https://t.me/narzoxbot'>MovieFlix</a>\n"
    "›› Webseries: <a href='https://t.me/narzoxbot'>WebFlix</a>\n"
    "›› Community: <a href='https://t.me/Teamrajweb'>Join Here</a>"
    "</b>"
)

# ================= BOT TEXT =================

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "⚠️ You are not authorized to use this command."

# ================= ADMINS =================

ADMINS = [OWNER_ID]

# ================= LOGGING =================

LOG_FILE_NAME = "links-sharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50_000_000, backupCount=5),
        logging.StreamHandler()
    ]
)

logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
