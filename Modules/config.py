from distutils.util import strtobool
import os
from dotenv import load_dotenv
from pyrogram.types import BotCommand


# Load environment variables from .env file
load_dotenv()


class Config(object):

    # Your API HASH
    API_HASH = os.environ.get('ed80c99568c99f73e8b739f09771bd3b')

    # Your API ID
    APP_ID = int(os.environ.get('32468786')

    # Your Bot Token
    BOT_TOKEN = os.environ.get('8240655341:AAFNqdnLuPMj778MkBLWoN0vQiYuZ6z9vW8')

    # Your Telegram ID (optional)
    OWNER_ID = os.environ.get('5501488547')

    # Upload method (default to False)
    AS_ZIP = bool(strtobool(os.environ.get('AS_ZIP', 'False')))

    # Channel/Group ID where you dump all the downloaded files.
    DUMP_ID = int(os.environ.get('1003860418822')
                  ) if os.environ.get('1003860418822') else None

    PLUGINS = {'root': 'Bot.plugins'}

    DOWNLOAD_DIR = "./downloads/"

    BOT_COMMANDS = [
        BotCommand('start', 'start bot'),
        BotCommand('help', 'help messages'),
        BotCommand('thumbnail', 'custom thumbnail'),
        BotCommand('caption', 'custom caption')
    ]
