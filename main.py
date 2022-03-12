# Variables ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

import os
discordToken = os.getenv("TOKEN")

import nextcord
from nextcord.ext import commands

bot = commands.Bot(command_prefix = "uh ")
from nextcord import Interaction, interactions

# Functions ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

@bot.command(name = "test", description = "Test if the bot is working")
async def test_if_working(context):
  await context.reply(f"I'm working <@{context.author.id}>")

@bot.slash_command(name = "spin", description = "Spin", guild_ids = [586680405302968321])
async def spin_command(interaction: Interaction):

  await interaction.response.send_message("https://tenor.com/view/computer-computador-spin-spinning-3d-gif-23612820")

# MainSetup ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

bot.run(discordToken)