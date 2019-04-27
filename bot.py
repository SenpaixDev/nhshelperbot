import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import time
import os

Client = discord.Client()
client = commands.Bot(command_prefix='/')
@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name="videos"))


client.run(os.getenv('BOT_TOKEN'))



