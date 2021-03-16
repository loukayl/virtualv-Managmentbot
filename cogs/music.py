import os, sys, discord
import datetime
import random
from discord.ext import commands
if not os.path.isfile("config.py"):
    sys.exit("'config.py' not found! Please add it and try again.")
else:
    import config

class music(commands.Cog, name="music"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="help")
    async def help(self, context):
        """
        List all commands from every Cog the bot has loaded.
        """    
        prefix = config.BOT_PREFIX
        if not isinstance(prefix, str):
            prefix = prefix[0]
        embed = discord.Embed(title="Help", description="Liste der Commands:", color=0x00FF00)
        for i in self.bot.cogs:
            cog = self.bot.get_cog(i.lower())
            commands = cog.get_commands()
            command_list = [command.name for command in commands]
            command_description = [command.help for command in commands]
            help_text = '\n'.join(f'{prefix}{n} - {h}' for n, h in zip(command_list, command_description))
            embed.add_field(name=i.capitalize(), value=f'```{help_text}```', inline=False)
        await context.send(embed=embed)

    @commands.command(name="clip")
    async def clip(self, context, member: discord.Member, *args):
        """
        Plays a clip sound.
        """
        await context.message.delete()

    @commands.command(name="clips")
    async def clips(self, context, member: discord.Member, *, name: str):
        """
        List all clips
        """
        await context.message.delete()

    @commands.command(name="filter")
    async def filter(self, context, member: discord.Member, *args):
        """
        filter zum song hinzufügen.
        """
        await context.message.delete()
    @commands.command(name="loop (l)")
    async def loop(self, context, member: discord.Member, *args):
        """
        Song wiederholen.
        """
        await context.message.delete()
            
    @commands.command(name="lyrics (ly)")
    async def lyrics(self, context, member: discord.Member, *args):
        """
        Get lyrics for the currently playing song.
        """
        await context.message.delete()
    @commands.command(name="move (mv)")
    async def smove(self, context, member: discord.Member, *args):
        """
        Move songs around in the queue.
        """
        await context.message.delete()
    @commands.command(name="vnp")
    async def vnp(self, context, member: discord.Member, *args):
        """
        Show now playing song.
        """
        await context.message.delete()
    @commands.command(name="pause")
    async def pause(self, context, member: discord.Member, *args):
        """
        Pause the currently playing music.
        """   
        await context.message.delete()
    @commands.command(name="play")
    async def play(self, context, member: discord.Member, *args):
        """
        Plays audio from YouTube or Soundcloud with Links.
        """   
        await context.message.delete()
    @commands.command(name="playlist (pl)")
    async def playlist(self, context, member: discord.Member, *args):
        """
        Play a playlist from youtube.
        """   
        await context.message.delete()
    @commands.command(name="prunning")
    async def prunning(self, context, member: discord.Member, *args):
        """
        Toggle pruning of bot messages.
        """   
        await context.message.delete()
    @commands.command(name="queue (q)")
    async def queue(self, context, member: discord.Member, *args):
        """
        Show the music queue and now playing.
        """   
        await context.message.delete()
    @commands.command(name="remove")
    async def remove(self, context, member: discord.Member, *args):
        """
        Remove song from the queue.
        """   
        await context.message.delete()
    @commands.command(name="resume (r)")
    async def resume(self, context, member: discord.Member, *args):
        """
        Resume currently playing music.
        """   
        await context.message.delete()
    @commands.command(name="search")
    async def search2(self, context, member: discord.Member, *args):
        """
        Search and select videos to play.
        """   
        await context.message.delete()
    @commands.command(name="shuffle")
    async def shuffle(self, context, member: discord.Member, *args):
        """
        Shuffle queue.
        """   
        await context.message.delete()
    @commands.command(name="skip (s)")
    async def skip3(self, context, member: discord.Member, *args):
        """
        Skip the currently playing song.
        """   
        await context.message.delete()
    @commands.command(name="skipto (st)")
    async def skip4(self, context, member: discord.Member, *args):
        """
        Skip to the selected queue number.
        """   
        await context.message.delete()
    @commands.command(name="stop")
    async def stop5(self, context, member: discord.Member, *args):
        """
        Stops the music.
        """   
        await context.message.delete()
    @commands.command(name="uptime")
    async def uptime(self, context, member: discord.Member, *args):
        """
        Check the uptime.
        """   
        await context.message.delete()
    @commands.command(name="volume")
    async def uptime(self, context, member: discord.Member, *args):
        """
        Change volume of currently playing music (1-100).
        """   
        await context.message.delete()
def setup(bot):
    bot.add_cog(music(bot))