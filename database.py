
# from pymongo.mongo_client import MongoClient

# uri = "mongodb+srv://online:Gaurav@321@online.ol4zd0a.mongodb.net/?retryWrites=true&w=majority"
from pymongo import MongoClient
from urllib.parse import quote_plus

username = "online"  # Replace with your actual username
password = "Gaurav@321"  # Replace with your actual password

escaped_username = quote_plus(username)
escaped_password = quote_plus(password)

uri = f"mongodb+srv://{escaped_username}:{escaped_password}@online.ol4zd0a.mongodb.net/onlinr?retryWrites=true&w=majority"

client = MongoClient(uri)

def get_database():
    connection_string = "mongodb://atlas-sql-649f109d3916b8466dca1fc0-45hpj.a.query.mongodb.net/mongodbVSCodePlaygroundDB?ssl=true&authSource=admin"
    client = MongoClient(uri)
    return client['online']

def add_customer(db, name, mobile):
    db.customers.insert_one({"name": name, "mobile": mobile})

def get_customer_by_mobile(db, mobile):
    return db.customers.find_one({"mobile": mobile})

def add_product_to_customer(db, mobile, product, price):
    db.customers.update_one({"mobile": mobile}, {"$push": {"products": {"name": product, "price": price}}})

# mongodb+srv://<username>:<password>@cluster0.2hzf2nt.mongodb.net/?retryWrites=true&w=majority

# from pymongo.mongo_client import MongoClient
# from pymongo.server_api import ServerApi

# uri = "mongodb+srv://<username>:<password>@cluster0.2hzf2nt.mongodb.net/?retryWrites=true&w=majority"

# # Create a new client and connect to the server
# client = MongoClient(uri, server_api=ServerApi('1'))

# # Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)