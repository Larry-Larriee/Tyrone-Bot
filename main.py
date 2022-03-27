# Variables ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ 

import datetime
from datetime import datetime, timedelta

import nextcord
from nextcord import interactions
from nextcord.ext import commands

import os, asyncio
bot = commands.Bot(command_prefix = "hey ")

# Functions ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ 

@bot.event
async def on_ready():
  print(f"{bot.user} has turned on!")
  await bot.change_presence(activity = nextcord.Game("Hello World!"))

# Next Goals: Add a confirm time option, anti-break system, a more specific time like 7:00 PM in LocalTime
@bot.command(name = "set")
async def set_timer(context, timer, minutes = 0, hours = 0, days = 0):
  
  # If the user inputs 'hey set timer...' then
  if timer == "timer":
    # Get the current time that the user sends the message
    currentTime = datetime.now()
    print(f"starting at {currentTime}")

    futureTime = currentTime + timedelta(minutes = minutes, hours = hours, days = days)
    await context.send(f"Alright. I have a timer set for **{futureTime} in UTC**")

    while (currentTime < futureTime) == True:
      await asyncio.sleep(30)

      currentTime = datetime.now()
      print(currentTime)

  authorUser = context.message.author.id
  await context.send(f"This is your reminder to do something <@{authorUser}>!!")

@bot.command(name = "assembly")
async def generate_profile(context, *arg):
  
  profileEmbed = nextcord.Embed(title = f"The Legendary Profile of {context.author}", description = f"About Me:\nShould follow MenofMERITS..", url = "https://www.instagram.com/jacobsmerits/"
  , color = 0xff0000, timestamp = datetime.now())

  # Send the embed 
  await context.send(embed = profileEmbed)

# MainSetup ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ 

# This token is found on Heroku's configure var section
#bot.run(os.getenv("TOKEN"))