import random
import discord
from discord.ext import commands
from discord.ext.commands import bot
import string
from discord import Game


bot = commands.Bot(command_prefix='!')

bot.remove_command('help')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print(discord.__version__)
    print('------')
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("DM MysteriousK#1476 to buy prem Access"))

@bot.command(name='minecraft')
@commands.has_role('Gen Access')
@commands.cooldown(1, 86400, commands.BucketType.user)
async def minecraft(ctx):
    with open('minecraft.txt') as f:
                i = f.read().splitlines()
                a = random.choice(i)
                await ctx.author.send(a)
                await ctx.send("You account has been sent enjoy (:")

@bot.command(name='spotify')
@commands.has_role('Gen Access')
@commands.cooldown(1, 86400, commands.BucketType.user)
async def spotify(ctx):
    with open('spotify.txt') as f:
                i = f.read().splitlines()
                a = random.choice(i)
                await ctx.author.send(a)
                await ctx.send("You account has been sent enjoy (:")

@bot.command(name='nord')
@commands.has_role('Gen Access')
@commands.cooldown(1, 86400, commands.BucketType.user)
async def nord(ctx):
    with open('nord.txt') as f:
                i = f.read().splitlines()
                a = random.choice(i)
                await ctx.author.send(a)
                await ctx.send("You account has been sent enjoy (:")

@bot.command(name='steam')
@commands.has_role('Gen Access')
@commands.cooldown(1, 86400, commands.BucketType.user)
async def steam(ctx):
    with open('steam.txt') as f:
                i = f.read().splitlines()
                a = random.choice(i)
                await ctx.author.send(a)
                await ctx.send("You account has been sent enjoy (:")

@bot.command(name='nitro')
@commands.has_role('Gen Access')
@commands.cooldown(1, 10, commands.BucketType.user)
async def nitro(ctx):
    Ncode = ('').join(random.choices(string.ascii_letters + string.digits, k=16))
    discord_url = "https://discordapp.com/gifts/"
    await ctx.author.send(discord_url + Ncode)
    await ctx.send("sent nitro in your dms")

@bot.command()
@commands.has_role('Gen Access')
@commands.cooldown(1, 10, commands.BucketType.user)
async def amazon(ctx):
    Acode = ('').join(random.choices(string.ascii_letters + string.digits, k=16))
    await ctx.author.send(Acode)
    await ctx.send("You Amazon giftcard has been sent enjoy ^^")

@bot.command()
@commands.has_role('Gen Access')
@commands.cooldown(1, 10, commands.BucketType.user)
async def mcwin10(ctx):
    Mcode = ('').join(random.choices(string.ascii_letters + string.digits, k=25))
    await ctx.author.send(Mcode)
    await ctx.send("Sent a win 10 minecraft code enjoy ^^")

@bot.command()
@commands.has_role('Gen Access')
@commands.cooldown(1, 10, commands.BucketType.user)
async def robux(ctx):
    Rcode = ('').join(random.choices(string.digits, k=10))
    await ctx.author.send(Rcode)
    await ctx.send("Sent a robux code")

@bot.command()
@commands.has_role('Gen Access')
@commands.cooldown(1, 10, commands.BucketType.user)
async def steamkey(ctx):
    Scode = ('').join(random.choices(string.ascii_letters + string.digits, k=13))
    await ctx.author.send(Scode)
    await ctx.send("A key has been sent")

@bot.command()
@commands.has_role('Gen Access')
@commands.cooldown(1, 10, commands.BucketType.user)
async def gplay(ctx):
    Gcode = ('').join(random.choices(string.ascii_letters + string.digits, k=16))
    await ctx.send("A code has been sent enjoy kiddo")
    await ctx.author.send(Gcode)
    

@bot.command(name='help')
async def help_gen(ctx):
    embed = discord.Embed(title="69420 Gen Bot™ Help menu ", description="**NOTE:** All the commands are case sensitive & requires the role **Gen Access**" , color=0xff0000)
    embed.add_field(name="**Generate Spotify**", value="command: !spotify" , inline=False)
    embed.add_field(name="**Generate Minecraft**", value="command: !minecraft", inline=False)
    embed.add_field(name="**Generate NordVPN**", value="command: !nord" , inline=False)
    embed.add_field(name="**Generate Steam**", value="command: !steam", inline=False)
    embed.add_field(name="**Generate Nitro(has a very less chance of getting a working one)**", value="command: !nitro", inline=False)
    embed.add_field(name="**Generate Amazon GiftCard(has a very less chance of getting a working one)**", value="command: !amazon", inline=False)
    embed.add_field(name="**Generate Minecraft Windows 10 Code(has a very less chance of getting a working one)**", value="command: !mcwin10", inline=False)
    embed.add_field(name="**Generate Steam Key(has a very less chance of getting a working one)**", value="command: !robux", inline=False)
    embed.add_field(name="**Generate Minecraft Windows 10 Code(has a very less chance of getting a working one)**", value="command: !steamkey", inline=False)
    embed.add_field(name="**Generate Minecraft Google Play GiftCard(has a very less chance of getting a working one)**", value="command: !gplay", inline=False)
    embed.add_field(name="**DM Devs To Buy Premium Access/Custom Gen Bot For Yourself**", value="MysteriousK#1476", inline=True)
    embed.set_author(name="Made by MysteriousK#1476", icon_url="https://cdn.discordapp.com/avatars/652456629316485120/97697929da00bc0bfeb3610cbd2624ef.png?size=256g")
    await ctx.send(embed=embed)



bot.run('token')
