import disnake, os, dotenv

# Just bot token
dotenv.load_dotenv()
TOKEN: str = os.getenv("VIO_TOKEN")

PROFILE: map = {
    "prefix": "v!",
    "owner_ids": [
        "890139054228783124", 
        "721095369441804342", 
        "1121470117516161217"
    ],
    "status": disnake.Status.do_not_disturb,
    "activity_name": "",
    "activity_state": ""
}