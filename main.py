# Variables ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

import os
discordToken = os.getenv("TOKEN")

import nextcord
from nextcord.ext import commands

bot = commands.Bot(command_prefix = "uh ")
from nextcord import Interaction, interactions

# Functions ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

@bot.slash_command(name = "spin", description = "Spin", guild_ids = [586680405302968321])
async def spin_command(interaction: Interaction):

  await interaction.response.send_message("https://tenor.com/view/computer-computador-spin-spinning-3d-gif-23612820")

# MainSetup ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

bot.run(discordToken)