from pymongo import MongoClient
from bson import ObjectId

client = MongoClient("mongodb://localhost:27017/")
db = client["shopping_db"]
print("Connection successful!")

# Read Documents from a Collection
items = db.items.find()
for item in items:
    print(item["name"])


# Try Inserting a Document
db.items.insert_one({
    "list_id": ObjectId("507f1f77bcf86cd799439011"),
    "name": "Cookies",
    "brand": "Oreo",
    "quantity": 1,
    "tags": ["Snacks"],
    "is_purchased": False
})


# Verify Inserted Items
items = db.items.find()
for item in items:
    print("Item Name:", item["name"])
    print("Brand:", item["brand"])
    print("Quantity:", item["quantity"])
    print("Tags:", item["tags"])
    print("Purchased:", item["is_purchased"])
    print("List ID:", item["list_id"])
    print("-" * 30)