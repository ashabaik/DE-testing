import pandas as pd
import boto3
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Retrieve AWS credentials from environment variables
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")

# Initialize S3 client with provided AWS credentials
s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID,
                  aws_secret_access_key=AWS_SECRET_ACCESS_KEY, region_name='us-east-1')

# Function to load data from S3 bucket into a pandas DataFrame
def load_data_from_s3(bucket_name, file_key):
    # Retrieve the object from the S3 bucket
    response = s3.get_object(Bucket=bucket_name, Key=file_key)
    # Convert the content of the object to a DataFrame
    data = pd.read_json(response['Body'])
    return data

# Function to upload data from DataFrame to S3 in JSON format
def upload_to_s3(dataframe, bucket_name, file_key):
    # Convert DataFrame to JSON format
    json_buffer = dataframe.to_json(orient='records', lines=True)
    # Upload the JSON data to S3
    s3.put_object(Bucket=bucket_name, Key=file_key, Body=json_buffer)
    print(f"File {file_key} uploaded to S3 successfully!")

# Main ETL function to extract, transform, and load data
def etl_process():
    # Load raw data from S3
    customers_df = load_data_from_s3('shipping-company-data-training', 'raw_data/customers_raw.json')
    products_df = load_data_from_s3('shipping-company-data-training', 'raw_data/products_raw.json')
    orders_df = load_data_from_s3('shipping-company-data-training', 'raw_data/orders_raw.json')

    # Perform transformations on the data (ETL)
    
    # Example transformation for customers
    customers_cleaned_df = customers_df.dropna()  # Remove rows with missing values
    
    # Example transformation for products
    products_final_df = products_df.drop_duplicates()  # Remove duplicate rows
    
    # Merge orders with products to get the product price
    orders_merged_df = pd.merge(orders_df, products_df[['product_id', 'price']], on='product_id', how='left')
    
    # Calculate the total_amount for each order (quantity * price)
    orders_merged_df['total_amount'] = orders_merged_df['quantity'] * orders_merged_df['price']
    
    # Filter orders with positive total_amount
    orders_transformed_df = orders_merged_df[orders_merged_df['total_amount'] > 0]
    
    # Upload transformed data back to S3
    upload_to_s3(customers_cleaned_df, 'shipping-company-data-training', 'processed_data/customers_cleaned.json')
    upload_to_s3(products_final_df, 'shipping-company-data-training', 'processed_data/products_final.json')
    upload_to_s3(orders_transformed_df, 'shipping-company-data-training', 'processed_data/orders_transformed.json')

# Execute the ETL process
etl_process()
