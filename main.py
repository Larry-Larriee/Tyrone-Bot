# Variables ---------------------------------------------------------------------------------------------

import discord 
Bot = discord.Client()

import os
Token_Key = os.environ["Token"]

import time
import asyncio
from KeepAlive import keep_alive

# Bot Events --------------------------------------------------------------------------------------------

@Bot.event
async def on_ready():
  print("{0} has turned on!".format(Bot.user))
  await Bot.change_presence(activity = discord.Game("all alone {0}".format("🥺")))

@Bot.event
async def on_message(message):
  userMsg = message.content.lower()
  user = message.author
  channel = message.channel

  if user == Bot.user:
    return 

# HELP COMMANDS -----------------------------------------------------------------------------------------
  elif "help me tyrone" in userMsg:
    await channel.send(f"Thanks for using me, Tyrone 2.0, <@{user.id}>")
    await asyncio.sleep(1)
    await channel.send("Some commands include but are not limited to: **PRANK, TOMFOOLERY, YOO, PPCOUNT**")
    await asyncio.sleep(1)
    await channel.send("Give Larry some ideas to make pls. More information can be found on https://github.com/Larrieeee/Tyrone-Bot")
    
# TOMFOOLERY --------------------------------------------------------------------------------------------
  elif "prank" in userMsg:
    for LMAO in range(1,10000):
      await user.send("**You have been trolled {0} times <@{1}>!** <:WHY:827390243920412672>".format(LMAO, user.id))
      await asyncio.sleep(1)
# PISSOFF -----------------------------------------------------------------------------------------------
  elif "tomfoolery" in userMsg:
    await channel.send("Who do you want me to ping >:)")

    PersonPinging = await Bot.wait_for("Message")

    if PersonPinging.content.startswith("<@"):
      for Maximum in range(25):
        await channel.send("We do a little tomfoolery {0} :)".format(PersonPinging.content))
        await asyncio.sleep(1)
      
    else: 
      await channel.send("You're supposed to ping someone smh {0}".format(":unamused:"))

# PPCOUNT -----------------------------------------------------------------------------------------------
  
  elif "ppcount" in userMsg:
    print("\nI'm counting! and started at {0}".format(time.ctime()))

    for PenisCount in range(20000):    
      PENIS = [
    ":regional_indicator_p:", 
      ":regional_indicator_e:", 
      ":regional_indicator_n:", 
      ":regional_indicator_i:", 
      ":regional_indicator_s:"]
              
      await asyncio.sleep(1)
      await channel.send("**{0}** {1} {2} {3} {4} {5} **!**".format(str(PenisCount), PENIS[0], PENIS[1], PENIS[2], PENIS[3], PENIS[4]))

# CONTROLME ---------------------------------------------------------------------------------------------
  elif "controlme" in userMsg:
    
    while True:
      botResponse = input("\nWhat would you like me to say?\n")
      await channel.send(botResponse)
# YOO ----------------------------------------------------------------------------------------------------
  elif userMsg.startswith("yoo"):
    await channel.send("YOOOOOOOOOOO WHATS GOOD <@{0}>".format(message.author.id))
    await asyncio.sleep(1)
    await channel.send("YOOOOOOOOOOO <@{0}>".format("394888049483579395"))
# DM TYLER ----------------------------------------------------------------------------------------------
  elif message.content.lower().startswith("merry"):
    for i in range(1,10):
      await channel.send("Merry Christmas yall😱🥳🥳")
      await asyncio.sleep(1)
      await channel.send("Merry Christmas <@{0}>😱🥳🥳".format("521015407407267850"))
# Jackson wants 50 penises -------------------------------------------------------------------------------


keep_alive()
Bot.run(Token_Key)
