import os
import dotenv
import build as Bot
from api import getQuote

dotenv.load_dotenv(dotenv.find_dotenv())

email = os.getenv('email')
password = os.getenv('password')
quote = getQuote();

Bot.browseTwitter();
Bot.login(email, password);
Bot.makeTwit(quote);
# Bot.closeChrome();