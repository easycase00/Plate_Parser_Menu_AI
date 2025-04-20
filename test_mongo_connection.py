import os
from pymongo import MongoClient
from dotenv import load_dotenv
from urllib.parse import quote_plus

load_dotenv()

username = quote_plus(os.getenv("MONGO_USERNAME"))
password = quote_plus(os.getenv("MONGO_PASSWORD"))
cluster = os.getenv("MONGO_CLUSTER")

uri = f"mongodb+srv://{username}:{password}@{cluster}/?retryWrites=true&w=majority"

try:
    client = MongoClient(uri)
    db = client["menu_db"]
    collection = db["menus"]

    # Test insert
    collection.insert_one({"test": "MongoDB is working!"})
    result = collection.find_one({"test": "MongoDB is working!"})

    print("✅ Success! Connected and found:", result)

except Exception as e:
    print("❌ Connection failed:", e)



