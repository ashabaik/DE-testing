import json
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from flatten_json import flatten  # Import flatten_json package
from bson import ObjectId  # Import ObjectId for conversion
import pandas as pd

# MongoDB connection URI
uri = "mongodb+srv://shabaik1996:Shekaa%401996@cluster0.chkql.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create client connection
client = MongoClient(uri, server_api=ServerApi('1'))

# Specify the database and collection
db = client["sample_mflix"]  # Replace with your actual database name
users_collection = db["users"]  # Access the "users" collection

# Function to convert ObjectId to string
def convert_objectid(doc):
    """ Convert ObjectId fields to strings in a document """
    if isinstance(doc, dict):
        return {k: str(v) if isinstance(v, ObjectId) else v for k, v in doc.items()}
    return doc

# Fetch all documents from the "users" collection
try:
    users_data = [convert_objectid(user) for user in users_collection.find()]  # Convert ObjectId to string
    print("Connected successfully and retrieved users data!")

    # Flatten each document using flatten_json
    flattened_data = [flatten(user) for user in users_data]

    # Convert flattened JSON to a readable JSON format
    flattened_json_output = json.dumps(flattened_data, indent=4)

    # Print or save to a file
    # print(flattened_json_output)

    # Save to a JSON file (optional)
    with open("flattened_users.json", "w") as f:
        f.write(flattened_json_output)

except Exception as e:
    print(f"Failed to fetch users data: {e}")
    
    
try:
    df=pd.DataFrame(flattened_data)
    print(df.shape)
except Exception as e:
    print(f"Failed to create DataFrame: {e}")
