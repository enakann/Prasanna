import pymongo
from pymongo import MongoClient
client = MongoClient()
db=client.shop
products=db.products

product1={
	'name':'tshirt',
	'price':'100'
	}

products.insert_one(product1)

print(db.list_collection_names())

print(list(products.find()))

