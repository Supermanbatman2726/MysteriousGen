import discord
from discord.ext import commands
import random

class Accounts(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_command_error(self,ctx,error):
        if isinstance(error,commands.MissingRole):
            await ctx.send(embed=discord.Embed(title='Missing Required Role',description='You dont have the required role "Gen Access" to run this command.'))
        else:
            await ctx.send(embed=discord.Embed(title='There was an unhandeled exception.',description=f'Please create an issue and send this.\n```{error}```'))
    
    @commands.command(aliases=['m','minecraf'])
    @commands.has_role('Gen Access')
    @commands.cooldown(1, 86400, commands.BucketType.user)
    async def minecraft(ctx):
        with open('accounts/minecraft.txt') as f:
            i = f.read().splitlines()
            a = random.choice(i)
            
            await ctx.author.send(embed=discord.Embed(title='Your Account',description=f'Here is your generated account: {a}'))
            await ctx.send(embed=discord.Embed(title='Your account has been generated.',description='Your account was successfully generated. You can run this command again for more.'))

    @commands.command(aliases=['spotif'])
    @commands.has_role('Gen Access')
    @commands.cooldown(1, 86400, commands.BucketType.user)
    async def spotify(ctx):
        with open('accounts/spotify.txt') as f:
            i = f.read().splitlines()
            a = random.choice(i)
            await ctx.author.send(embed=discord.Embed(title='Your Account',description=f'Here is your generated account: {a}'))
            await ctx.send(embed=discord.Embed(title='Your account has been generated.',description='Your account was successfully generated. You can run this command again for more.'))

    @commands.command(aliases=['nor'])# frick
    @commands.has_role('Gen Access')
    @commands.cooldown(1, 86400, commands.BucketType.user)
    async def nord(ctx):
        with open('accounts/nord.txt') as f:
            i = f.read().splitlines()
            a = random.choice(i)
            await ctx.author.send(embed=discord.Embed(title='Your Account',description=f'Here is your generated account: {a}'))
            await ctx.send(embed=discord.Embed(title='Your account has been generated.',description='Your account was successfully generated. You can run this command again for more.'))

    @commands.command(aliases=['s','stea'])
    @commands.has_role('Gen Access')
    @commands.cooldown(1, 86400, commands.BucketType.user)
    async def steam(ctx):
        with open('accounts/steam.txt') as f:
            i = f.read().splitlines()
            a = random.choice(i)
            await ctx.author.send(embed=discord.Embed(title='Your Account',description=f'Here is your generated account: {a}'))
            await ctx.send(embed=discord.Embed(title='Your account has been generated.',description='Your account was successfully generated. You can run this command again for more.'))


def setup(bot):
	bot.add_cog(Accounts(bot))