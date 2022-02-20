# Variables ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Environment variable to hide API tokens!!
from dotenv import load_dotenv
import os
load_dotenv()

# Grab the discord library
import discord
discordToken = os.getenv("discordToken")

# Datastore for discord messages :O
import pymongo
from pymongo import MongoClient
mongoToken = os.getenv("mongoToken")

cluster = MongoClient(f"mongodb+srv://Tyrone:{mongoToken}@cluster0.abmnh.mongodb.net/discord?retryWrites=true&w=majority")
database = cluster["discord"]
collection = database["messages"]

# Functions ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# MainSetup ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



















# INSERTING DATA ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# AKA bullet point list under collection under database
post = {"_id": 1, "test": "dab"}
post2 = {"_id": 2, "test": "dab"}
post3 = {"_id": 13, "test": "hello World!"}

#collection.insert_many([post, post2, post3])

# ANALYSIS OF DATA ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

'''
output = collection.find({"test": "dab"})

for result in output:
  print(result["_id"])
'''

countTotal = collection.count_documents({"test": "dab"})
print(countTotal)

# DELETION OF DATA ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#target = collection.delete_one({"_id":1})

#target2 = collection.delete_many({"test": "dab"})
