import discord
from discord.ext import commands
import random
import string

class Help(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_command_error(self,ctx,error):
        if isinstance(error,commands.MissingRole):
            await ctx.send(embed=discord.Embed(title='Missing Required Role',description='You dont have the required role "Gen Access" to run this command.'))
        else:
            await ctx.send(embed=discord.Embed(title='There was an unhandeled exception.',description=f'Please create an issue and send this.\n```{error}```'))
    
    @commands.command(aliases=['h','hel','halp','help'])
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
        embed.add_field(name="**DM the Dev To Buy Custom Bot's For Yourself**", value="MysteriousK#0420", inline=True)
        embed.set_author(name="Made by MysteriousK#0420", icon_url="https://cdn.discordapp.com/avatars/652456629316485120/97697929da00bc0bfeb3610cbd2624ef.png?size=256g")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Help(bot))