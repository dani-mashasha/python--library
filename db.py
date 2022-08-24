from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

DB_USER=os.getenv("DB_USER")
DB_PASS=os.getenv("DB_PASS")
DB_NAME=os.getenv("DB_NAME")
DB_COLLECTION=os.getenv("DB_COLLECTION")
DB_HOST=os.getenv("DB_HOST")

cluster = MongoClient(f"mongodb+srv://{DB_USER}:{DB_PASS}@{DB_HOST}/?retryWrites=true&w=majority")
db = cluster[DB_NAME]
collection = db[DB_COLLECTION]

