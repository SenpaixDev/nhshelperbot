import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import random
import datetime
import json

bot = commands.Bot(command_prefix='/')

@bot.event
async def on_ready():
    print ("0 Errors found so far.")
    print ("NHS Helper Bot is online")
    await bot.change_presence(game=discord.Game(name='Do "/cmds" to get started!'))

@bot.command(pass_context=True)
async def cmds(ctx):
    emb_name = discord.Embed(title="Moderation Commands.", description="***/kick [user]*** | Kicks the specified user!\n***/ban [user]*** | Bans the specified user!\n***/clear [amount]*** | Clears the requested amount of messages!\n***/mute [user]*** | Mutes the specified user!\n***/unmute [user]*** | Unmutes the specified user!", color=discord.Color.green())
    await bot.send_message(ctx.message.channel, embed=emb_name)
    emb_name = discord.Embed(title="User Commands.", description="***/cmds*** | Brings up this message!\n***/ping*** | Pong! Checks the bots ping.\n***/report [User] [Reason]*** | Reports a user!\n***/suggest [Suggestion]*** | Makes a suggestion to be in the game!", color=discord.Color.green())
    await bot.send_message(ctx.message.channel, embed=emb_name)

@bot.command(pass_context = True)
@commands.has_permissions(mute_members=True)
async def mute(ctx, member: discord.Member=None):
    role=discord.utils.get(member.server.roles, name='Muted')
    await bot.add_roles(member, role)
    await bot.say(f"{ctx.message.author} has muted {member}! :mute:")

@bot.command(pass_context = True)
@commands.has_permissions(mute_members=True)
async def unmute(ctx, member: discord.Member=None):
    role=discord.utils.get(member.server.roles, name='Muted')
    await bot.remove_roles(member, role)
    await bot.say(f"{ctx.message.author} has unmuted {member}! :loudspeaker:")


@bot.command(pass_context = True)
async def kick(ctx, userName: discord.User):
 if "Admin" in [role.name for role in ctx.message.author.roles]:
     await bot.kick(userName)
     await bot.say(f"@{ctx.message.author} has kicked {userName}!")
 else:
            await bot.say ("You do not have permission to use this command! You need to have the 'admin' rank!")

@bot.command(pass_context = True)
async def ban(ctx, userName: discord.User):
 if "Admin" in [role.name for role in ctx.message.author.roles]:
     await bot.ban(userName)
     await bot.say(f"@{ctx.message.author} has banned {userName}!")
 else:
            await bot.say ("You do not have permission to use this command! You need to have the 'admin' rank!")


@bot.command(pass_context=True)
async def clear(ctx, amount=100):
    if "Admin" in [role.name for role in ctx.message.author.roles]:
        channel = ctx.message.channel
        messages = []
        async for message in bot.logs_from(channel, limit=int(amount) + 1):
            messages.append(message)
        await bot.delete_messages(messages)
        await bot.say(f'I have just cleared {amount} messages for you! :smiley:')
    else:
            await bot.say ("You do not have permission to use this command! You need to have the 'admin' rank!")

@bot.command(pass_context=True)
async def ping(ctx):
    t = await bot.say('Pong!')
    ms = (t.timestamp-ctx.message.timestamp).total_seconds() * 1000
    await bot.edit_message(t, new_content='Pong! Took: {}ms'.format(int(ms)))


@bot.command(pass_context=True)
async def suggest(ctx, *, suggestion):
    author = ctx.message.author
    channel = author.server.get_channel('571738785465892865')
    embed=discord.Embed(
        colour=discord.Colour.gold()
    )
    embed.set_footer(text="Suggestion brought to you by NHS Helper Bot", icon_url="https://cdn.discordapp.com/avatars/571737225323347968/c552aaed0caa38bc2e154f3ed130982c.png?size=128")
    embed.add_field(name="{0} made a suggestion".format(author), value="Suggestion: {0}".format(suggestion))
    embed.set_thumbnail(url=author.avatar_url)
    await bot.send_message(channel, embed=embed)
    await bot.add_reaction(message,"\U0001F44D")

@bot.command(pass_context=True)
async def report(ctx, *, reportion):
    author = ctx.message.author
    channel = author.server.get_channel('571739006803640370')
    embed=discord.Embed(
        colour=discord.Colour.red()
    )
    embed.set_footer(text="Report brought to you by NHS Helper Bot", icon_url="https://cdn.discordapp.com/avatars/571737225323347968/c552aaed0caa38bc2e154f3ed130982c.png?size=128")
    embed.add_field(name="{0} made a Report".format(author), value="Report: {0}".format(reportion))
    embed.set_thumbnail(url=author.avatar_url)
    await bot.send_message(channel, embed=embed)
    await bot.add_reaction(message,"\U0001F44D")

@bot.command(pass_context=True)
async def userinfo(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s info".format(user.name), description="Brought to you by NHS Helper Bot.", color=0x00ff00)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="Nickname", value=user.nick, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Is the user a bot?", value=user.bot, inline=True)
    embed.add_field(name="Highest role", value=user.top_role, inline=True)
    embed.add_field(name="Joined", value=user.joined_at, inline=True)
    embed.add_field(name="Account created at", value=user.created_at, inline=True)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.send_message(ctx.message.channel, embed=embed)

report = {}
report['users'] = []

client = discord.ext.commands.Bot(command_prefix = '?')

@bot.command(pass_context = True)
async def warn(ctx,user:discord.User,*reason:str):
 if "Admin" in [role.name for role in ctx.message.author.roles]:
  if not reason:
    await bot.say("Please provide a reason")
    return
  reason = ' '.join(reason)
  for current_user in report['users']:
    if current_user['name'] == user.name:
      current_user['reasons'].append(reason)
      break
  else:
    report['users'].append({
      'name':user.name,
      'reasons': [reason,]
    })

 else:
            await bot.say ("You do not have permission to use this command! You need to have the 'admin' rank!")


@bot.command(pass_context = True)
async def warnings(ctx,user:discord.User):
  for current_user in report['users']:
    if user.name == current_user['name']:
      await bot.say(f"{user.name} has been reported {len(current_user['reasons'])} times : {','.join(current_user['reasons'])}")
      break
  else:
    await bot.say(f"{user.name} has never been reported")  
     


bot.run(str(os.environ.get('BOT_TOKEN')))



