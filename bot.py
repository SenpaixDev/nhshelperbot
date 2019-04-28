import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

bot.run('NTcxNzM3MjI1MzIzMzQ3OTY4.XMTgGg.Yi1e2oCmiuAEjiwgIlAXbrq5ThY')






