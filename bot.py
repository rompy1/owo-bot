import discord
import random
import time
from discord.ext import commands
from urllib import request
from random import randrange
import json
import ssl

bot = commands.Bot(command_prefix='^', description="I am a test")

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    #await bot.change_presence(activity = discord.Activity(name = "What's this?", type = 3))


@bot.command(aliases = ["p"])
async def ping(ctx):
    """Says Pong!"""
    await ctx.send("UwU")


@bot.command()
async def shutdown(ctx):
    """shutdown the bot (admin only)"""
    if ctx.author.id == 192735146003267584 or 133642107259846657:
        await ctx.send("Goodbye senpai uwu")
        exit()
    else:
        await ctx.send("I'm sorry, you don't have permission to do that!")


@bot.command()
async def pm(ctx, sendto: str, msgtosend: str):
    msg = ctx.message
    user = await bot.get_user_info(int(sendto))
    await user.send(msgtosend)
    await msg.add_reaction("✅")



@bot.event
async def on_message(message):
    if "owo" in message.content.lower() or "uwu" in message.content.lower():
        if "^" not in message.content.lower() and message.author.id != 456091144502247444:
            await message.channel.send("What's this?")
    await bot.process_commands(message)


@bot.command()
async def owofy(ctx):
    msg = ctx.message
    try:
        await msg.delete()
    except:
        pass
    totranslate = str(msg.content)
    id = ('<@%s>' % ctx.author.id)
    totranslate = totranslate.replace("^owofy", "")
    totranslate = totranslate.replace("r", "w")
    totranslate = totranslate.replace("l", "w")
    #totranslate = totranslate.replace("you", "senpai")
    totranslate = totranslate + " UwU" + ("\n - %s" % id)
    await ctx.send(totranslate)


bot.run(str(os.environ.get('BOT_TOKEN')))
