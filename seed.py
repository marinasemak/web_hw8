from models import Author, Quote
import json
from mongoengine import connect, ValidationError, NotUniqueError
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()

MONGO_HOST = os.getenv("MONGO_HOST", "localhost")
MONGO_PORT = int(os.getenv("MONGO_PORT", 27017))
MONGO_USER = os.getenv("MONGO_INITDB_ROOT_USERNAME")
MONGO_PASSWORD = os.getenv("MONGO_INITDB_ROOT_PASSWORD")
MONGO_DB = os.getenv("MONGO_DB", "test_db082024")
MONGO_COLLECTION = os.getenv("MONGO_COLLECTION", "authors")


def connect_db():
    """Establishes a connection to the MongoDB database using MongoEngine."""
    try:
        connect(
            db=MONGO_DB,
            host=MONGO_HOST,
            port=MONGO_PORT,
            username=MONGO_USER,
            password=MONGO_PASSWORD,
            authentication_source="admin",
        )
        print("MongoDB connection: SUCCESS")
    except ConnectionError as e:
        print(f"MongoDB connection: FAILED\nError: {e}")
        exit(1)


def fill_data():
    #  Fill authors
    with open('authors.json') as f:
        data_from_file = json.load(f)
        for el in data_from_file:
            try:
                author = Author(
                    fullname=el.get("fullname"),
                    born_date=datetime.strptime(el.get("born_date"), '%B %d, %Y'),
                    born_location=el.get("born_location"),
                    description=el.get("description"),
                )
                author.save()
                print(f"Created author: {author.id}")
            except ValidationError as e:
                print(f"Validation Error: {e}")
            except NotUniqueError as e:
                print(f"NotUnique Error: {e}")
    # Fill quotes
    with open('quotes.json') as f:
        data_from_file = json.load(f)
        for el in data_from_file:
            try:
                author = Author.objects.get(fullname=el.get("author"))
                quote = Quote(
                    tags=el.get("tags"),
                    author=author,
                    quote=el.get("quote"),
                )
                quote.save()
                print(f"Created author: {quote.id}")
            except ValidationError as e:
                print(f"Validation Error: {e}")



if __name__ == "__main__":
    connect_db()
    fill_data()
