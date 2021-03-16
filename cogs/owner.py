import os, sys, discord
import asyncio
import aiohttp
import discord
from discord.ext import commands
import discord
from discord.ext.commands import Cog
from discord.ext.commands import command, has_permissions, has_role
from discord import Member
from discord import Embed,File
from typing import Optional
from random import choice
from asyncio import TimeoutError, sleep
from lib.util.util import convert
if not os.path.isfile("config.py"):
    sys.exit("'config.py' not found! Please add it and try again.")
else:
    import config

class owner(commands.Cog, name="owner"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="shutdown")
    async def shutdown(self, context):
        """
        Make the bot shutdown
        """
        await context.message.delete()
        if context.message.author.id in config.OWNERS:
            embed = discord.Embed(
                description="Ich schalte mich aus. Bye! Bye! :wave:",
                color=0x00FF00
            )
            await context.send(embed=embed)
            await self.bot.logout()
            await self.bot.close()
        else:
            embed = discord.Embed(
                title="Fehler!",
                description="Du hast keine Berechtigung dazu.",
                color=0x00FF00
            )
            await context.send(embed=embed)


    @commands.command(name="giftcr", aliases=["giveaway", "gcreate", "gcr"])
    @has_permissions(manage_guild=True)
    # @has_role("admin")
    async def create_giveaway(self, ctx):
        """
        Giveaway erstellen
        """
        await ctx.message.delete()
        #Ask Questions
        embed = Embed(title="Giveaway Time!!✨",
                      description="Bitte beantworte die Fragen innerhalb von 30 sekunden!",
                      color=ctx.author.color)
        await ctx.send(embed=embed)
        questions=["In welchen Channel soll das Giveaway gehostet werden #🎉giveaways?",
                   "Wie lange soll das Giveaway gehen? Trage die Zeit ein mit der Nummer und = (s|m|h|d)",
                   "Was ist der Giveaway preis?"]
        answers = []
        #Check Author
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel
        
        for i, question in enumerate(questions):
            embed = Embed(title=f"Frage {i}",
                          description=question)
            await ctx.send(embed=embed)
            try:
                message = await self.bot.wait_for('message', timeout=30, check=check)
            except TimeoutError:
                await ctx.send("Leider hast du zulange gebraucht! Bitte wiederhole denn Command")
                return
            answers.append(message.content)
        #Check if Channel Id is valid
        try:
            channel_id = int(answers[0][2:-1])
        except:
            await ctx.send(f"Der bereitgestellte Kanal war falsch. Der Kanal sollte sein {ctx.channel.mention}")
            return

        channel = self.bot.get_channel(channel_id)
        time = convert(answers[1])
        #Check if Time is valid
        if time == -1:
            await ctx.send("Das Zeitformat ist falsch")
            return
        elif time == -2:
            await ctx.send("Die Zeit war keine konventionelle Zahl")
            return
        prize = answers[2]

        await ctx.send(f"Ihr Giveaway wird in gehostet {channel.mention} und wird dauern {answers[1]}")
        embed = Embed(title="Giveaway Time !!",
                    description=f"Gewinne {prize} heute!",
                    colour=0x00FFFF)
        embed.add_field(name="Hosted By:", value=ctx.author.mention)
        embed.set_footer(text=f"Giveway endet in {answers[1]} in")
        newMsg = await channel.send(embed=embed)
        await newMsg.add_reaction("🎉")
        #Check if Giveaway Cancelled
        self.cancelled = False
        await sleep(time)
        if not self.cancelled:
            myMsg = await channel.fetch_message(newMsg.id)

            users = await myMsg.reactions[0].users().flatten()
            users.pop(users.index(self.bot.user))
            #Check if User list is not empty
            if len(users) <= 0:
                emptyEmbed = Embed(title="Giveaway Time !!",
                                   description=f"Gewinne {prize} heute!")
                emptyEmbed.add_field(name="Hosted By:", value=ctx.author.mention)
                emptyEmbed.set_footer(text="Keiner hat das Giveaway gewonnen!")
                await myMsg.edit(embed=emptyEmbed)
                return
            if len(users) > 0:
                winner = choice(users)
                winnerEmbed = Embed(title="Giveaway Time !!",
                                    description=f"Gewinnt {prize} heute!",
                                    colour=0x00FFFF)
                winnerEmbed.add_field(name=f"Herzlichen Glückwunsch zum Gewinn {prize}", value=winner.mention)
                winnerEmbed.set_image(url="https://i.imgur.com/cQ3nxtC.png")
                await myMsg.edit(embed=winnerEmbed)
                return

    # @create_giveaway.error
    # async def create_giveaway_error(self, ctx, exc):
    #     if isinstance(exc, MissingPermissions):
    #         await ctx.send("You are not allowed to create Giveaways")
        

    @commands.command(name="giftrrl", aliases=["gifreroll", "gftroll", "grr"])
    @has_permissions(manage_guild=True)
    # @has_role("admin")
    async def giveaway_reroll(self, ctx, channel : discord.TextChannel, id_: int):
        """
        Giveaway Gewinner rerollen
        """
        await ctx.message.delete()
        try:
            msg = await channel.fetch_message(id_)
        except:
            await ctx.send("Der angegebene Kanal oder die angegebene ID war falsch")
        users = await msg.reactions[0].users().flatten()
        if len(users) <= 0:
            emptyEmbed = Embed(title="Giveaway Time !!",
                                   description=f"Gewinne einen Preis")
            emptyEmbed.add_field(name="Hosted By:", value=ctx.author.mention)
            emptyEmbed.set_footer(text="Keiner hat dieses mal gewonnen!")
            await msg.edit(embed=emptyEmbed)
            return
        if len(users) > 0:
            winner = choice(users)
            winnerEmbed = Embed(title="Giveaway Time !!",
                                description=f"Gewinne heute einen preis",
                                colour=0x00FFFF)
            winnerEmbed.add_field(name=f"Herzlichen Glückwunsch zum Gewinn", value=winner.mention)
            winnerEmbed.set_image(url="https://i.imgur.com/cQ3nxtC.png")
            await msg.edit(embed=winnerEmbed)
            return

                # users.pop(users.index(self.bot.user))
                # winner = choice(users)
                # await channel.send(f"Congratulations {winner.mention} on winning the Giveaway")

    @commands.command(name="giftdel", aliases=["gifdel", "gftdel", "gdl"])
    @has_permissions(manage_guild=True)
    # @has_role("admin")
    async def giveaway_stop(self, ctx, channel : discord.TextChannel, id_: int):
        """
        Giveaway Gewinner rerollen
        """
        await ctx.message.delete()
        try:
            msg = await channel.fetch_message(id_)
            newEmbed = Embed(title="Giveaway abgebrochen", description="Das Giveaway wurde abgebrochen!!")
            #Set Giveaway cancelled
            self.cancelled = True
            await msg.edit(embed=newEmbed) 
        except:
            embed = Embed(title="Fehler!", description="Kann das Giveaway nicht abbrechen!")
            await ctx.send(emebed=embed)


    @commands.command(name="say")
    async def say(self, context, *, args):
        """
        The Bot ill say this whats you want.
        """
        await context.message.delete()
        if context.message.author.id in config.OWNERS:
            embed = discord.Embed(
                description=args,
                color=0x00FF00
            )
            await context.send(embed=embed)
        else:
            embed = discord.Embed(
                title="Fehler!",
                description="Du hast keine Berechtigung dazu.",
                color=0x00FF00
            )
            await context.send(embed=embed)
            

    @commands.command(name="embed")
    async def embed(self, context, *, args):
        """
        The bot will say anything you want, but within embeds.
        """
        await context.message.delete()
        if context.message.author.id in config.OWNERS:
            embed = discord.Embed(
                description=args,
                color=0x00FF00
            )
            await context.send(embed=embed)
        else:
            embed = discord.Embed(
                title="Fehler!",
                description="Du hast keine Berechtigung dazu.",
                color=0x00FF00
            )
            await context.send(embed=embed)

    @commands.group(name="blacklist")
    async def blacklist(self, context):
        """
        Lets you add or remove a user from not being able to use the bot.
        """
        await context.message.delete()
        if context.invoked_subcommand is None:
            embed = discord.Embed(
                title=f"Das sind geblacklistete {len(config.BLACKLIST)} IDs",
                description=f"{config.BLACKLIST}",
                color=0x0000FF
            )
            await context.send(embed=embed)

    @blacklist.command(name="add")
    async def blacklist_add(self, context, member: discord.Member):
        """
        Lets you add a user from not being able to use the bot.
        """
        if context.message.author.id in config.OWNERS:
            userID = member.id
            try:
                config.BLACKLIST.append(userID)
                embed = discord.Embed(
                    title="User Blacklisted",
                    description=f"**{member.name}** wurde erfolgreich geblacklisted",
                    color=0x00FF00
                )
                embed.set_footer(
                    text=f"There are now {len(config.BLACKLIST)} users in the blacklist"
                )
                await context.send(embed=embed)
            except:
                embed = discord.Embed(
                    title="Fehler!",
                    description=f"Ein unbekannter Fehler ist aufgetreten beim setzen von**{member.name}** auf die Blacklist.",
                    color=0xFF0000
                )
                await context.send(embed=embed)
        else:
            embed = discord.Embed(
                title="Fehler!",
                description="Du hast keine Berechtigung dazu.",
                color=0x00FF00
            )
            await context.send(embed=embed)

    @blacklist.command(name="remove")
    async def blacklist_remove(self, context, member: discord.Member):
        """
        Lets you remove a user from not being able to use the bot.
        """
        if context.message.author.id in config.OWNERS:
            userID = member.id
            try:
                config.BLACKLIST.remove(userID)
                embed = discord.Embed(
                    title="User Unblacklisted",
                    description=f"**{member.name}** has been successfully removed from the blacklist",
                    color=0x00FF00
                )
                embed.set_footer(
                    text=f"There are now {len(config.BLACKLIST)} users in the blacklist"
                )
                await context.send(embed=embed)
            except:
                embed = discord.Embed(
                    title="Error!",
                    description=f"An unknown error occurred when trying to remove **{member.name}** from the blacklist.",
                    color=0xFF0000
                )
                await context.send(embed=embed)
        else:
            embed = discord.Embed(
                title="Error!",
                description="You don't have the permission to use this command.",
                color=0x00FF00
            )
            await context.send(embed=embed)
            

    @commands.command(name="upprank")
    @commands.has_permissions(manage_roles = True)
    @commands.bot_has_permissions(manage_roles = True)
    async def setrank(self, ctx, member: discord.Member=None, *rankName: str):
        '''Teamler einen Upprank geben
        Beispiel:
        -----------
        :setrole @Der-Eddy#6508 Member
        '''
        rank = discord.utils.get(ctx.guild.roles, name=' '.join(rankName))
        await ctx.message.delete()
        if member is not None:
            await member.add_roles(rank)
            await ctx.send(f':white_check_mark: Teamler **{member.name}** wurde auf **{rank.name}** Uppranked')
        else:
            await ctx.send(':no_entry: Du musst einen Benutzer angeben!')

    @commands.command(name="derank")
    @commands.has_permissions(manage_roles = True)
    @commands.bot_has_permissions(manage_roles = True)
    async def rmrank(self, ctx, member: discord.Member=None, *rankName: str):
        '''Gibt einem Teamler ein RankDown
        Beispiel:
        -----------
        :rmrole @Der-Eddy#6508 Member
        '''
        rank = discord.utils.get(ctx.guild.roles, name=' '.join(rankName))
        await ctx.message.delete()
        if member is not None:
            await member.remove_roles(rank)
            await ctx.send(f':white_check_mark: Teamler **{member.name}** wurde auf **{rank.name}** downranked')
        else:
            await ctx.send(':no_entry: Du musst einen Benutzer angeben!')



    @commands.group(name="whitelist")
    async def whitelist(self, context):
        """
        Lets you add or remove a user from not being able to join the server.
        """
        await context.message.delete()
        if context.invoked_subcommand is None:
            embed = discord.Embed(
                title=f"Whitelistete Staatsbürger : {len(config.WHITELIST)} IDs",
                description=f"{config.WHITELIST}",
                color=0x0000FF
            )
            await context.send(embed=embed)

    @whitelist.command(name="add")
    async def whitelist_add(self, context, member: discord.Member):
        """
        Lets you add a user from not being able to join the server.
        """
        if context.message.author.id in config.OWNERS:
            userID = member.id
            try:
                config.WHITELIST.append(userID)
                embed = discord.Embed(
                    title="User Whitelisted",
                    description=f"**{member.name}** wurde erfolgreich whitelisted",
                    color=0x00FF00
                )
                embed.set_footer(
                    text=f"There are now {len(config.WHITELIST)} users in the whitelist"
                )
                await context.send(embed=embed)
            except:
                embed = discord.Embed(
                    title="Fehler!",
                    description=f"Ein unbekannter Fehler ist aufgetreten beim setzen von**{member.name}** auf die whitelist.",
                    color=0xFF0000
                )
                await context.send(embed=embed)
        else:
            embed = discord.Embed(
                title="Fehler!",
                description="Du hast keine Berechtigung dazu.",
                color=0x00FF00
            )
            await context.send(embed=embed)

def setup(bot):
    bot.add_cog(owner(bot))