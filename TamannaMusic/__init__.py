from TamannaMusic.core.bot import Tamanna
from TamannaMusic.core.dir import dirr
from TamannaMusic.core.git import git
from TamannaMusic.core.userbot import Userbot
from TamannaMusic.misc import dbb, heroku

from SafoneAPI import SafoneAPI
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Tamanna()
api = SafoneAPI()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
