import discord
import os
import random
import time
from discord.ext import commands
from urllib import request
from random import randrange
import json
import ssl

bot = commands.Bot(command_prefix='^', description="Now with 100% more cringe!")

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    #await bot.change_presence(activity = discord.Activity(name = "What's this?", type = 3))


@bot.command(aliases = ["p"])
async def ping(ctx):
    """checks if bot is running (admin only)"""
    if ctx.author.id == 192735146003267584 or ctx.author.id == 133642107259846657:
        await ctx.send("UwU")


@bot.command()
async def shutdown(ctx):
    """shutdown the bot (admin only)"""
    if ctx.author.id == 192735146003267584 or ctx.author.id == 133642107259846657:
        await ctx.send("Goodbye senpai uwu")
        exit()
    #else:
        #await ctx.send("I'm sorry, you don't have permission to do that!")


#@bot.command()
#async def pm(ctx, sendto: str, msgtosend: str):
#    msg = ctx.message
#    user = await bot.get_user_info(int(sendto))
#    await user.send(msgtosend)
#    await msg.add_reaction("✅")



@bot.event
async def on_message(message):
    if "owo" in message.content.lower() or "uwu" in message.content.lower():
        if "^" not in message.content.lower() and message.author.id != 605445941285224455:
            await message.channel.send("What's this?")
    await bot.process_commands(message)


@bot.command(aliases = ["uwufy"])
async def owofy(ctx):
    """OwOfy a message! Usage: ^owofy [message]"""
    msg = ctx.message
    try:
        await msg.delete()
    except:
        pass
    totranslate = str(msg.content)
    if len(totranslate) > 6:
        id = ('<@%s>' % ctx.author.id)
        totranslate = totranslate.replace("^owofy", "")
        totranslate = totranslate.replace("r", "w")
        totranslate = totranslate.replace("l", "w")
        #totranslate = totranslate.replace("you", "senpai")
        totranslate = totranslate + " UwU" + ("\n - %s" % id)
        await ctx.send(totranslate)
    else:
        await ctx.send("You need to put a message after the command! (^owofy [message])")

@bot.command(aliases = ["git"])
async def github(ctx):
    """PMs you the github link"""
    user = await bot.get_user_info(int(sendto))
    await user.send(https://github.com/rompy1/owo-bot)
    try:
        await msg.delete()
    except:
        pass
    
    

bot.run(str(os.environ.get('BOT_TOKEN')))
