# Variables ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Environment variable to hide API tokens!!
from dotenv import load_dotenv
import os
load_dotenv()

# Grab the discord library & keep the bot on
from discord import FFmpegPCMAudio
import discord
from discord.ext import commands
discordToken = os.getenv("discordToken")

from KeepAlive import keep_alive
bot = commands.Bot(command_prefix = "dude ")

# Sleep function 
import asyncio

# Datastore for discord messages
from mongoDB import collect_message

# Functions ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

@bot.event
async def on_ready():
  await bot.change_presence(activity = discord.Game(name = "Roblox"))
  print(f" {bot.user} is Working")

# Collect all user messages when they type in the chat
@bot.event
async def on_message(message):
  await collect_message(message)

  # Allows bot.command to run as discord and discord.ext is different from eachother
  await bot.process_commands(message)

@bot.command(name = "help_me")
async def what_are_commands(context):

  await context.reply(f"I'm a work in progress <@{context.author.id}>")
  await asyncio.sleep(1)
  await context.send("Documentation: https://github.com/Larrieeee/Tyrone-Bot/blob/Main-Page/README.md")

@bot.event
async def on_command_error(context, error):
  await context.send(f"{error}")

# PlayAudio ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Voice channel join command for the bot to join a voice channel and play an audio file
@bot.command(name = "join")
async def join_channel(context):

  if (context.author.voice):
    channel = context.author.voice.channel

    voice = await channel.connect()
    source = FFmpegPCMAudio("audioPackages/clashAudio.mp3")

    voice.play(source)

  else:
    await context.reply("Not in channel???")

# Forces the bot to leave the current channel that is is inside 
@bot.command(name = "leave")
async def leave_channel(context):

  # If the bot is in a channel
  if (context.voice_client):
    await context.guild.voice_client.disconnect()

  else:
    await context.reply("I'm not even in a channel???")

# States for the bot to pause the audio file that it is currently playing
@bot.command(name = "pause")
async def pause_audio(context):

  # Call discord ultilities & current voice channel/song
  voice = discord.utils.get(bot.voice_clients, guild = context.guild)

  if voice.is_playing():
    voice.pause()

  else:
    await context.reply("Not playing a song??")

# MainSetup ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

keep_alive()
bot.run(discordToken)
