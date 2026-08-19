import disnake, os, dotenv
from lib import languagelib


# Just bot token
dotenv.load_dotenv()
TOKEN: str = os.getenv("VIO_TOKEN")

languages = languagelib.LANGUAGES
base_language = languages.get("en_US") 

PROFILE: dict = {
    "prefix": "v!",
    "owner_ids": [
        890139054228783124, 
        721095369441804342, 
        1121470117516161217
    ],
    "test_guilds": [
        1195781157191688233,
        1112050416063090840,
        1143154725659869317,
        973213303516053564,
        1267874600272924704
    ],
    "status": disnake.Status.do_not_disturb,
    "activity_type": disnake.ActivityType.custom,
    "activity_name": "Just..",
    "activity_state": "📡 I Want to Believe"
}