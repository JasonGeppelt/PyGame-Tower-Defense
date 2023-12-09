import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://Geppelt:4Oga6Q16dafA70Dz@testcluster.lwyvyyp.mongodb.net/?retryWrites=true&w=majority")
db = cluster["save_manager"]
collection = db["save_state"]


# Function to save the game state
def save_game_state(level, health, money):
    game_state = {
        "player_id": "1",
        "current_level": level,
        "player_health": health,
        "player_money": money
    }
    collection.update_one({"player_id": "1"}, {"$set": game_state}, upsert=True)

# Function to load the game state
def load_game_state():
    return collection.find_one({"player_id": "1"})