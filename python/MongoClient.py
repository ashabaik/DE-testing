import os
import json
import pandas as pd
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from bson import ObjectId
import boto3
from botocore.exceptions import NoCredentialsError
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get credentials from environment variables
MONGO_URI = os.getenv("MONGO_URI")
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")

# Ensure credentials are available
if not MONGO_URI or not AWS_ACCESS_KEY_ID or not AWS_SECRET_ACCESS_KEY:
    raise ValueError("Missing required credentials. Set MONGO_URI, AWS_ACCESS_KEY_ID, and AWS_SECRET_ACCESS_KEY.")

# Connect to MongoDB
client = MongoClient(MONGO_URI, server_api=ServerApi('1'))
db = client["sample_mflix"]  
users_collection = db["users"]  

# Function to convert ObjectId fields to strings
def convert_objectid(doc):
    """ Convert ObjectId fields to strings in a document """
    if isinstance(doc, dict):
        return {k: str(v) if isinstance(v, ObjectId) else v for k, v in doc.items()}
    return doc

# Fetch all user data from MongoDB
try:
    users_data = [convert_objectid(user) for user in users_collection.find()] 
    print("Connected to MongoDB and retrieved users' data successfully.")

    # Save the original data to a JSON file
    with open("original_users.json", "w") as f:
        json.dump(users_data, f, indent=4)
    print("Original users data saved successfully.")

except Exception as e:
    print(f"Error fetching users data: {e}")

# Data cleaning: Add 'age' column by calculating it from 'date_of_birth'
try:
    # Load birth dates file (CSV format)
    birth_dates_file = 'D:/DATA/random_users_with_dob.csv'  
    birth_dates_df = pd.read_csv(birth_dates_file)  
    print("Birth dates file loaded successfully.")

    # Merge original user data with birth dates based on 'name'
    original_df = pd.DataFrame(users_data)
    merged_df = pd.merge(original_df, birth_dates_df, on='name', how='left')

    # Convert 'date_of_birth' to datetime format
    merged_df['date_of_birth'] = pd.to_datetime(merged_df['date_of_birth'], format='%d/%m/%Y', errors='coerce')  
    merged_df['age'] = (pd.to_datetime('today') - merged_df['date_of_birth']).dt.days // 365

    # Convert 'date_of_birth' back to string format for JSON compatibility
    merged_df['date_of_birth'] = merged_df['date_of_birth'].dt.strftime('%Y-%m-%d')

    # Remove invalid age values
    merged_df = merged_df.dropna(subset=['age'])
    merged_df = merged_df[merged_df['age'] >= 0]

    # Save the cleaned data to a new JSON file
    cleaned_data = merged_df.to_dict(orient='records')
    with open("cleaned_users.json", "w") as f:
        json.dump(cleaned_data, f, indent=4)
    print("Cleaned users data saved successfully.")

except Exception as e:
    print(f"Error during data cleaning: {e}")

# Upload JSON files to AWS S3
try:
    # Initialize S3 client with credentials
    s3 = boto3.client('s3', 
                      aws_access_key_id=AWS_ACCESS_KEY_ID, 
                      aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

    # Define S3 bucket name
    bucket_name = 'mongo-data.testing' 

    # Upload the JSON files to S3
    s3.upload_file('original_users.json', bucket_name, 'original_users.json')
    s3.upload_file('cleaned_users.json', bucket_name, 'cleaned_users.json')
    print("Files uploaded successfully to S3.")

except NoCredentialsError:
    print("AWS credentials not available.")
except Exception as e:
    print(f"Error uploading files to S3: {e}")
