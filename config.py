from os import getenv

API_ID = int(getenv("API_ID", "20400887")) #optional
API_HASH = getenv("API_HASH", "535abea1d0cc67a4be1f57de026a846f") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5702610439").split()))
OWNER_ID = int(getenv("OWNER_ID", "5702610439"))
MONGO_URL = getenv("MONGO_URL", )
BOT_TOKEN = getenv("BOT_TOKEN", "")
ALIVE_PIC = getenv("ALIVE_PIC")
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = getenv("LOG_GROUP")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/ITZ-ZAID/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
