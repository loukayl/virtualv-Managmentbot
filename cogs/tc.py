import os, sys, discord
from discord.ext import commands
if not os.path.isfile("config.py"):
    sys.exit("'config.py' not found! Please add it and try again.")
else:
    import config

class tc(commands.Cog, name="teamcommands"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='vkick', pass_context=True)
    async def vkick(self, context, member: discord.Member, *args):
        """
        Kicke einen Spieler vom Server.
        """
        await context.message.delete()

    @commands.command(name="vrevive")
    async def vnick(self, context, member: discord.Member, *, name: str):
        """
        Revive einen Spieler
        """
        await context.message.delete()

    @commands.command(name="vban")
    async def vban(self, context, member: discord.Member, *args):
        """
        Ban einen Spieler.
        """
        await context.message.delete()

    @commands.command(name="vsetjob")
    async def vwarnen(self, context, member: discord.Member, *args):
        """
        Gib einem Spieler einen job.
        """
        await context.message.delete()

    @commands.command(name="vgivemoney")
    async def vwarn(self, context, member: discord.Member, *args):
        """
        Gib einem Spieler Geld.
        """
        await context.message.delete()
        
def setup(bot):
    bot.add_cog(tc(bot))