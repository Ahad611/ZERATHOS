from SHUKLAMUSIC.core.bot import SHUKLA
from SHUKLAMUSIC.core.dir import dirr
from SHUKLAMUSIC.core.git import git
from SHUKLAMUSIC.core.userbot import Userbot
from SHUKLAMUSIC.misc import dbb, heroku

from SafoneAPI import SafoneAPI
from .logging import LOGGER

# Initialize core utilities
dirr()
git()
dbb()
heroku()

# Clients
app = SHUKLA
userbot = Userbot()
api = SafoneAPI()

# --- FIXED STARTUP SEQUENCE ---
import asyncio

BOT_ID = None
BOT_USERNAME = None
BOT_MENTION = None

async def _init_bot_info():
    global BOT_ID, BOT_USERNAME, BOT_MENTION
    # Start the client before using it
    await app.start()
    me = await app.get_me()
    BOT_ID = me.id
    BOT_USERNAME = me.username
    BOT_MENTION = me.mention
    LOGGER(__name__).info(f"✅ Bot started as {me.first_name} (@{me.username})")

# Run the info fetcher at startup
loop = asyncio.get_event_loop()
loop.run_until_complete(_init_bot_info())
# --- FIX END ---

from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()

APP = "ll_DRAGON_MUSIC_BOT"  # connect music api key "Dont change it"
