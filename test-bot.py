import discord
from discord.ext import commands
from discord.utils import get
import youtube_dl
import os

from discord.ext import commands

client = discord.Client()

@client.event
async def on_message(message):
    message.content = message.content.lower()

    # this is for greetings
    if message.author == client.user:
        return
    if message.content.startswith("hi ms terry"):
        if str(message.author) == "IWuvMeSumChicken#7835":
            await message.channel.send("fuck you faggot")
        else:
            await message.channel.send("Hi, " + str(message.author) + " :heart: !")
    if message.content.startswith("ms terry"):
        if message.content.endswith("?"):
            if str(message.author) == "IWuvMeSumChicken#7835":
                await message.channel.send("shut up idiot")
            else:
                await message.channel.send("Yes, sure!")
        else:
            if str(message.author) == "IWuvMeSumChicken#7835":
                await message.channel.send("get the fuck away from me retard")
            else:
                await message.channel.send("No thanks!")

    # this is for reacting with emojis
    if message.content.startswith("i love u ms terry"):
        if str(message.author) == "IWuvMeSumChicken#7835":
            await message.channel.send(":sick: :face_vomiting:")
        else:
            await message.add_reaction("\U0001F60D")





client.run('XXXXXXXXXXXXXXXXXXXXXXXXXXX')
