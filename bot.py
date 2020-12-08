import discord
from discord.ext import commands
from discord.ext.commands import bot
from discord import Game
import os

bot = commands.Bot(command_prefix='!')

bot.remove_command('help')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print(discord.__version__)
    print('------')
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("Bot made by MysteriousK#0420."))

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")
        print(f"Loaded cog {filename}")
        print()

bot.run('NzczMDkyODk1NDgwNjEwODE2.X6EM3Q.1B7O_sWcCOpFqgeS5uLv2BjW8lk')
