from pymongo import MongoClient

uri = "mongodb+srv://deepshahstudy100:Admin123%40@cluster0.5dqr6d9.mongodb.net/?appName=Cluster0"

client = MongoClient(uri)

try:
    client.admin.command("ping")
    print("Connected successfully")
except Exception as e:
    print("MongoDB connection failed:", e)
finally:
    client.close()