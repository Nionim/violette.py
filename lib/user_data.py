import lang
from lib.database import DATABASE

class VI_USER:
    global database

    def __init__(self, id):    
        database = DATABASE(f"{id}.db")
        database.set("lang", "en_US")

    def get_language():
        return database.get("lang")
    
    def set_language(label: str):
        return database.set(label)