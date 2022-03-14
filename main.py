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

        await bot.change_presence(activity = nextcord.Game(name = f"for {round((elapsedTime / 360), 2)} Hours"))

# Test command using the command prefix
@bot.command(name = "test", description = "Test if the bot is working")
async def test_if_working(context):
  await context.reply(f"I'm working <@{context.author.id}>")

# Slash command that returns a picture of a computer GIF
@bot.slash_command(name = "spin", description = "Spin", guild_ids = [586680405302968321, 949110139531722802, 834242088391540796])
async def spin_command(interaction: Interaction):

  await interaction.response.send_message("https://tenor.com/view/computer-computador-spin-spinning-3d-gif-23612820")

# MainSetup ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

bot.run(discordToken)