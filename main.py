# Variables ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

import nextcord
from nextcord import Interaction
from nextcord.ext import commands

from datetime import datetime
import os, asyncio
discordToken = os.getenv("TOKEN")
bot = commands.Bot(command_prefix = "uh ")

# Functions ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Display the date since the bot was last updated
@bot.event
async def on_ready():
    print(f"{bot.user} has turned itself on!")
    startTime = datetime.timestamp(datetime.now())

    while True:
        await asyncio.sleep(5)
        currentTime = datetime.timestamp(datetime.now())
        elapsedTime = round((float(currentTime) - float(startTime)))

        await bot.change_presence(activity = nextcord.Game(name = f"for {round((elapsedTime / 3600), 2)} Hours"))

# Test command using the command prefix
@bot.command(name = "test", description = "Test if the bot is working")
async def test_if_working(context):
  await context.reply(f"I'm working <@{context.author.id}>")

# Start a giveaway with a specified time and random select a user id
@bot.command(name = "giveaway", description = "Giveway?? It's pretty self-explanitory")
async def give_now(context):

  # Get the channel that context was sent in (context grabs all data)
  # context.message specially grabs the message that the user inputs
  channelName = bot.get_channel(context.message.channel.id)
  
  joinMessage = await channelName.send("React to join the giveaway!")
  await joinMessage.add_reaction("🎉")

# Slash command that returns a picture of a computer GIF
@bot.slash_command(name = "spin", description = "Spin", guild_ids = [586680405302968321, 949110139531722802, 834242088391540796])
async def spin_command(interaction: Interaction):

  await interaction.response.send_message("https://tenor.com/view/computer-computador-spin-spinning-3d-gif-23612820")

# MainSetup ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

bot.run("ODg2MTE0ODQxOTY4OTE0NDQ1.YTw4wQ.LmY9onKEPJQn4jTOrpKaGepm4Ok")