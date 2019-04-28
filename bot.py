import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print ("0 Errors found so far.")
    print ("NHS Helper Bot is online")
    await bot.change_presence(game=discord.Game(name='Do "/cmds" to get started!'))

bot.run('NTcxNzM3MjI1MzIzMzQ3OTY4.XMTgGg.Yi1e2oCmiuAEjiwgIlAXbrq5ThY')






