#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 23532861
API_HASH = "6f0cfb9808100e072b7dab1d6b9ee3c8"
BOT_TOKEN = "6259477626:AAF7YdZR1q4kGnS0dAKe7GSISJEpmqXjjqw"
SESSION = "BQFnFT0AEOOLRK1eMzS3oK7uHH4sjAcKWDHQ02zY_i0Us5e95XO8Zyx5XvYTfAGGTWGRIHM9QjBM_gdFQubvhPwx1U_NKYOG4Dy2MBYGen3hIzy6JzHB44roE_9Zl7mEylFSyA0TR6rmVnwX_57TaKadMNc_RqiHVoWbtXTVmC1_jNziA0PNoAtLp6MSkGiy5BgHuKSfzNIr6JQr6i5IFDcpDib3bkoVbiaFihXF8nouRIFssPxJNZ29uQEX491WjzP9Oq2Y8fvqzzOjcpH6lzBqjwYiDU4LP_ZVFT1fRCSpRW8q1X_ZPqQvNwlvPkOALq_mV2Ym_NrKEKub3r9nTajFxAlFOgAAAAAUw-IZAA"
FORCESUB = "SaveR_estrictedContentBot"
AUTH = "MShaun"

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
