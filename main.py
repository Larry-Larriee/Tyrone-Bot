# Variables ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Environment variable to hide API tokens!!
from dotenv import load_dotenv
import os
load_dotenv()

# Grab the discord library & keep the bot on
from discord.ext import commands
from discord import FFmpegPCMAudio
discordToken = os.getenv("discordToken")

from KeepAlive import keep_alive
ext = commands.Bot(command_prefix = "dude ")

# Datastore for discord messages :O
import pymongo
from pymongo import MongoClient
mongoToken = os.getenv("mongoToken")

cluster = MongoClient(f"mongodb+srv://Tyrone:{mongoToken}@cluster0.abmnh.mongodb.net/discord?retryWrites=true&w=majority")
database = cluster["discord"]
collection = database["messages"]

# Sleep (wait command)
import asyncio

# Functions ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

@ext.event
async def on_ready():
  await ext.change_presence(activity = discord.Activity(type = discord.ActivityType.watching, name = "CocoMelon"))
  print(f" {ext.user} is Working")

'''
bot = discord.Client()

@bot.event
async def on_message(message):
  
  if message.author == bot.user:
    return

  elif message.content.lower() == "help me tyrone":
    await message.channel.send(f"I'm a work in progress <@{message.author.id}>")
    await asyncio.sleep(1)
    await message.channel.send("Documentation: https://github.com/Larrieeee/Tyrone-Bot/blob/Main-Page/README.md")

  elif message.content.lower() == "nerd":
    for i in range(69420):
      
      nerd = await message.channel.send(f"**{i + 1} Nerd** 🤓🤓🤓🤓🤓🤓🤓")
      await nerd.add_reaction("🤓")
      
      await asyncio.sleep(0.75)

  else:

    messageId = collection.count_documents({})
    post = {"_id": messageId + 1,"Discord Server": message.author.guild.name, "Channel": message.channel.name, "Discord Author": message.author.name, "Message Sent": message.content}

    # Stores all messages across all servers the bot is in
    collection.insert_one(post)
'''

@ext.command(name = "join")
async def join_channel(context):

  if (context.author.voice):
    channel = context.author.voice.channel

    voice = await channel.connect()
    source = FFmpegPCMAudio()


  else:
    await context.reply("Not in channel???")

@ext.command(name = "leave")
async def leave_channel(context):

  # If the bot is in a channel
  if (context.voice_client):
    await context.guild.voice_client.disconnect()

  else:
    await context.reply("I'm not even in a channel???")

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

keep_alive()
ext.run(discordToken)
