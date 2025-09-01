import re
from os import getenv
# ------------------------------------
# ------------------------------------
from dotenv import load_dotenv
from pyrogram import filters
# ------------------------------------
# ------------------------------------
load_dotenv()
# ------------------------------------
# -----------------------------------------------------
API_ID = int(getenv("API_ID","22657083"))
API_HASH = getenv("API_HASH","d6186691704bd901bdab275ceaab88f3")
# ------------------------------------------------------
BOT_TOKEN = getenv("BOT_TOKEN","7981435750:AAEeeoaooxgq2lh8e_5TPkXctyQirH-d29c")
# -------------------------------------------------------
OWNER_USERNAME = getenv("OWNER_USERNAME","Og_Zerathos")
# --------------------------------------------------------
BOT_USERNAME = getenv("BOT_USERNAME" , "CardioMuzicBot")
# --------------------------------------------------------
BOT_NAME = getenv("BOT_NAME" , "-  `𝐂α᱂ᴅɪᴏ ꭗ‌ 𝐌ᴜѕɪᴄ")
# ---------------------------------------------------------
ASSUSERNAME = getenv("ASSUSERNAME" , "sexyKakrox")
# ---------------------------------------------------------


#---------------------------------------------------------------
#---------------------------------------------------------------
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://cardiomusic4:cardiomusic4@cluster0.4n3ee1d.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
#---------------------------------------------------------------
#---------------------------------------------------------------

# ----------------------------------------------------------------
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))
# ----------------------------------------------------------------

# ----------------------------------------------------------------
LOGGER_ID = int(getenv("LOGGER_ID", "-1002681848382"))
# ----------------------------------------------------------------
# ----------------------------------------------------------------
OWNER_ID = int(getenv("OWNER_ID", "7694170809"))
# -----------------------------------------------------------------
# -----------------------------------------------------------------

# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME","Ivan")
# ----------------------------------------------------------------
HEROKU_API_KEY = getenv("HEROKU_API_KEY","HRKU-AApD2ZG7a151gNkH6-WUTcHUYjUnxQRhGM3rCgJbmMBw_____wvruQGJTR0f")
# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------
UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Ahad6111/ZERATHOS",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # ----------------------------------------------------------------
# -------------------------------------------------------------------
# --------------------------------------------------------------------
# --------------------------------------------------------------------



# ------------------------------------------------------------------------
# -------------------------------------------------------------------------
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/botXjarvis")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/JarvisXsupport")
# ------------------------------------------------------------------------------
# -------------------------------------------------------------------------------







# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "True")
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "9000"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", "9999999"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "9999999"))
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "46f72f0c2b5b4541bfd0f02ec1d41378")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "9fd35265f82444109bf725b44f9358b9")
# ----------------------------------------------------------------------------------




# -----------------------------------------------------------------------------------
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
# ------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "5242880000"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "5242880000"))
# --------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------



# ------------------------------------
# ------------------------------------
# ------------------------------------
# ------------------------------------
STRING1 = getenv("STRING1", None)
STRING2 = getenv("STRING2", None)
STRING3 = getenv("STRING3", None)
STRING4 = getenv("STRING4", None)
STRING5 = getenv("STRING5", None)
STRING6 = getenv("STRING6", None)
STRING7 = getenv("STRING7", None)
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

# ------------------------------------
# ------------------------------------
# ------------------------------------
# ------------------------------------

# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
START_IMG_URL = getenv(
    "START_IMG_URL", "SHUKLAMUSIC/assets/st3.png"
)
PING_IMG_URL = [
    "SHUKLAMUSIC/assets/ping.png"
    "SHUKLAMUSIC/assets/beautiful girl.jpeg",
    "SHUKLAMUSIC/assets/Teju Ashwini.jpeg",
    "SHUKLAMUSIC/assets/download (4).jpeg",
    "SHUKLAMUSIC/assets/download (3).jpeg",
    "SHUKLAMUSIC/assets/download (2).jpeg",
    "SHUKLAMUSIC/assets/Teju Ashwini.jpeg",
    "SHUKLAMUSIC/assets/download (5).jpeg"
]
PLAYLIST_IMG_URL = "https://files.catbox.moe/ujpc4j.jpg"
STATS_IMG_URL = getenv(
    "STATS_IMG_URL", "SHUKLAMUSIC/assets/stats.png"
)

TELEGRAM_AUDIO_URL = "SHUKLAMUSIC/assets/download (5).jpeg"
TELEGRAM_VIDEO_URL = "SHUKLAMUSIC/assets/download (5).jpeg"
STREAM_IMG_URL = "SHUKLAMUSIC/assets/download (5).jpeg"
SOUNCLOUD_IMG_URL = "SHUKLAMUSIC/assets/download (5).jpeg"
YOUTUBE_IMG_URL = "SHUKLAMUSIC/assets/download (5).jpeg"
SPOTIFY_ARTIST_IMG_URL = "SHUKLAMUSIC/assets/download (5).jpeg"
SPOTIFY_ALBUM_IMG_URL = "SHUKLAMUSIC/assets/download (5).jpeg"
SPOTIFY_PLAYLIST_IMG_URL = "SHUKLAMUSIC/assets/download (5).jpeg"

# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# ------------------------------------------------------------------------------
if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
# ---------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
