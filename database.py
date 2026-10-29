from pymongo import MongoClient
import bcrypt
import os

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
DB_NAME   = os.getenv("DB_NAME",   "agri_rental_db")

client = MongoClient(MONGO_URI)
db     = client[DB_NAME]

equipment_collection = db["equipment"]
rentals_collection   = db["rentals"]
customers_collection = db["customers"]
users_collection     = db["users"]

def init_db():
    # Drop old indexes
    try:
        equipment_collection.drop_index("equipment_id_1")
    except: pass
    try:
        customers_collection.drop_index("email_1")
    except: pass
    try:
        users_collection.drop_index("username_1")
    except: pass

    # Recreate indexes
    equipment_collection.create_index(
        "equipment_id", unique=True, sparse=True)
    customers_collection.create_index(
        "email", unique=True, sparse=True)
    users_collection.create_index(
        "username", unique=True, sparse=True)

    # Create default admin only if not exists
    if not users_collection.find_one({"username": "admin"}):
        hashed = bcrypt.hashpw(
            "admin123".encode(), bcrypt.gensalt())
        users_collection.insert_one({
            "username":  "admin",
            "password":  hashed.decode(),
            "role":      "admin",
            "full_name": "System Admin"
        })
        print("✅ Admin created: admin / admin123")
    else:
        print("✅ Admin already exists")

    print(f"📦 Equipment : {equipment_collection.count_documents({})} records")
    print(f"👥 Customers : {customers_collection.count_documents({})} records")
    print(f"📋 Rentals   : {rentals_collection.count_documents({})} records")
    print("✅ Anyone can register and login!")