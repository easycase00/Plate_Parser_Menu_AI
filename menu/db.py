from pymongo import MongoClient
#from dotenv import load_dotenv
import os
from urllib.parse import quote_plus
import streamlit as st
from urllib.parse import quote_plus

#load_dotenv()

username = quote_plus(os.getenv("MONGO_USERNAME"))
password = quote_plus(os.getenv("MONGO_PASSWORD"))
cluster = os.getenv("MONGO_CLUSTER")

# MongoDB Atlas connection URI
uri = f"mongodb+srv://{username}:{password}@{cluster}/?retryWrites=true&w=majority"

client = MongoClient(uri)
db = client["menu_db"]
collection = db["menus"]

def store_menu(data: dict):
    collection.insert_one(data)

def get_all_menus():
    return list(collection.find({}, {"_id": 0}))
