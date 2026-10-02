import os
import sys
from pathlib import Path

from dotenv import load_dotenv

import pandas as pd
import pymongo
import certifi

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging


# Load environment variables from .env
load_dotenv()

# Get MongoDB URL from .env
MONGO_DB_URL = os.getenv("MONGO_DB_URL")


class NetworkDataExtract:
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def csv_to_json_convertor(self, file_path):
        try:
            # Read CSV file
            data = pd.read_csv(file_path)

            # Reset index
            data.reset_index(drop=True, inplace=True)

            # Convert DataFrame to a list of dictionaries (one per row)
            records = data.to_dict(orient="records")

            logging.info(f"Converted {len(records)} rows from {file_path}")
            return records

        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def insert_records(self, records, database, collection):
        try:
            if not MONGO_DB_URL:
                raise ValueError("MONGO_DB_URL is not set. Check your .env file.")

            # Connect to MongoDB
            self.mongo_client = pymongo.MongoClient(
                MONGO_DB_URL,
                tlsCAFile=certifi.where()
            )

            # Select database and collection
            self.database = self.mongo_client[database]
            self.collection = self.database[collection]

            # Insert records
            result = self.collection.insert_many(records)

            logging.info(f"Inserted {len(result.inserted_ids)} records into {database}.{collection}")
            return f"Data inserted successfully: {len(result.inserted_ids)} records"

        except Exception as e:
            raise NetworkSecurityException(e, sys)


if __name__ == "__main__":

    # Build the path relative to this script, so it works from any folder
    BASE_DIR = Path(__file__).resolve().parent
    FILE_PATH = BASE_DIR / "Network_Data" / "phisingData.csv"

    DATABASE = "DeepShah"
    COLLECTION = "NetworkData"

    # Create object
    networkobj = NetworkDataExtract()

    # Convert CSV to JSON records
    records = networkobj.csv_to_json_convertor(file_path=FILE_PATH)

    print("CSV converted to JSON successfully")
    print(f"Number of records: {len(records)}")

    # Insert records into MongoDB
    result = networkobj.insert_records(records, DATABASE, COLLECTION)

    print(result)