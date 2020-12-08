import discord
from discord.ext import commands
import random
import string

class Giftcards(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_command_error(self,ctx,error):
        if isinstance(error,commands.MissingRole):
            await ctx.send(embed=discord.Embed(title='Missing Required Role',description='You dont have the required role "Gen Access" to run this command.'))
        else:
            await ctx.send(embed=discord.Embed(title='There was an unhandeled exception.',description=f'Please create an issue and send this.\n```{error}```'))
    @commands.command(aliases=['nitr','n'])
    @commands.has_role('Gen Access')
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def nitro(ctx):
        Ncode = ('').join(random.choices(string.ascii_letters + string.digits, k=16))
        discord_url = "https://discord.gift/"
        await ctx.author.send(embed=discord.Embed(title='Your Giftcard',description=f'Here is your generated giftcard: {discord_url+Ncode}'))
        await ctx.send(embed=discord.Embed(title='Your giftcard has been generated.',description='Your giftcard was successfully generated. You can run this command again for more.'))

    @commands.command(aliases=['amazo','a'])
    @commands.has_role('Gen Access')
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def amazon(ctx):
        Acode = ('').join(random.choices(string.ascii_letters + string.digits, k=16))
        await ctx.author.send(embed=discord.Embed(title='Your Giftcard',description=f'Here is your generated giftcard: {Acode}'))
        await ctx.send(embed=discord.Embed(title='Your giftcard has been generated.',description='Your giftcard was successfully generated. You can run this command again for more.'))

    @commands.command(aliases=['minecraftwindows10','minecraft-bedrock'])
    @commands.has_role('Gen Access')
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def mcwin10(ctx):
        Mcode = ('').join(random.choices(string.ascii_letters + string.digits, k=25))
        await ctx.author.send(embed=discord.Embed(title='Your Giftcard',description=f'Here is your generated giftcard: {Mcode}'))
        await ctx.send(embed=discord.Embed(title='Your giftcard has been generated.',description='Your giftcard was successfully generated. You can run this command again for more.'))

    @commands.command(aliases=['r','rbx','bobux'])
    @commands.has_role('Gen Access')
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def robux(ctx):
        Rcode = ('').join(random.choices(string.digits, k=10))
        await ctx.author.send(embed=discord.Embed(title='Your Giftcard',description=f'Here is your generated giftcard: {Rcode}'))
        await ctx.send(embed=discord.Embed(title='Your giftcard has been generated.',description='Your giftcard was successfully generated. You can run this command again for more.'))

    @commands.command(aliases=['sk','skey'])
    @commands.has_role('Gen Access')
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def steamkey(ctx):
        Scode = ('').join(random.choices(string.ascii_letters + string.digits, k=13))
        await ctx.author.send(embed=discord.Embed(title='Your Giftcard',description=f'Here is your generated giftcard: {Scode}'))
        await ctx.send(embed=discord.Embed(title='Your giftcard has been generated.',description='Your giftcard was successfully generated. You can run this command again for more.'))

    @commands.command(aliases=['gp','g'])
    @commands.has_role('Gen Access')
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def gplay(ctx):
        Gcode = ('').join(random.choices(string.ascii_letters + string.digits, k=16))
        await ctx.author.send(embed=discord.Embed(title='Your Giftcard',description=f'Here is your generated giftcard: {Gcode}'))
        await ctx.send(embed=discord.Embed(title='Your giftcard has been generated.',description='Your giftcard was successfully generated. You can run this command again for more.'))
    


def setup(bot):
	bot.add_cog(Giftcards(bot))