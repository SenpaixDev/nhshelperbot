import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='/')

@bot.command()
async def greet(ctx):
    await ctx.send(":smiley: :wave: Hello, there!")

bot.run('NTcxNzM3MjI1MzIzMzQ3OTY4.XMTgGg.Yi1e2oCmiuAEjiwgIlAXbrq5ThY')






