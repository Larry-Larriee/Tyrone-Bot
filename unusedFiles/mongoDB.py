# Variables ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Environment variable to hide API tokens!!
from dotenv import load_dotenv
import os
load_dotenv()

# Datastore for discord messages :O
import pymongo
from pymongo import MongoClient
mongoToken = os.getenv("mongoToken")

cluster = MongoClient(f"mongodb+srv://Tyrone:{mongoToken}@cluster0.abmnh.mongodb.net/discord?retryWrites=true&w=majority")
database = cluster["discord"]
collection = database["messages"]

# Functions ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

async def collect_message(userInput):
  
    # Collects data about the user's input whenever they send a message in a channel
    messageId = collection.count_documents({})
    post = {"_id": messageId + 1,"Discord Server": userInput.author.guild.name, "Channel": userInput.channel.name, "Discord Author": userInput.author.name, "Message Sent": userInput.content}

    # Stores all messages across all servers the bot is in
    collection.insert_one(post)

    return 

# INSERTING DATA ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# AKA bullet point list under collection under database
# collection.insert_one(post)

# ANALYSIS OF DATA ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

'''
output = collection.find({"test": "dab"})

for result in output:
  print(result["_id"])

'''

#countTotal = collection.count_documents({"test": "dab"})
#print(countTotal)

# DELETION OF DATA ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#target = collection.delete_one({"_id":1})
#target2 = collection.delete_many({})

# Mass Purge Data

'''
purgeCount = collection.count_documents({})

for i in range(0,purgeCount):
  target = collection.delete_one({"_id": (i)})

'''

# MainSetup ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

