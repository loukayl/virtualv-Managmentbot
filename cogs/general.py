import os, sys, discord, platform, random, aiohttp, json
import time
import os
import platform
import re
import asyncio
import inspect
import textwrap
from datetime import datetime, timedelta
from collections import Counter
import aiohttp
import discord
from discord.ext import commands
if not os.path.isfile("config.py"):
    sys.exit("'config.py' not found! Please add it and try again.")
else:
    import config

class general(commands.Cog, name="general"):
    def __init__(self, bot):
        self.bot = bot

    @staticmethod
    def _getRoles(roles):
        string = ''
        for role in roles[::-1]:
            if not role.is_default():
                string += f'{role.mention}, '
        if string == '':
            return 'None'
        else:
            return string[:-2]


    @commands.command(name="info", aliases=["botinfo"])
    async def info(self, context):
        """
        Get some useful (or not) information about the bot.
        """
        await context.message.delete()
        embed = discord.Embed(
            description="Lous Managment Bot",
            color=0x00FF00
        )
        embed.set_author(
            name="Bot Information"
        )
        embed.add_field(
            name="Owner:",
            value="𝕷𝖎𝖘𝖆 𝕷𝖔𝖚#8888",
            inline=True
        )
        embed.add_field(
            name="Python Version:",
            value=f"{platform.python_version()}",
            inline=True
        )
        embed.add_field(
            name="Prefix:",
            value=f"{config.BOT_PREFIX}",
            inline=False
        )
        embed.set_footer(
            text=f"Angefragt von {context.message.author}"
        )
        await context.send(embed=embed)

    @commands.command(aliases=['howhot', 'hot'])
    async def hotcalc(self, ctx, *, user: discord.Member = None):
        """ Returns a random percent for how hot is a discord user """
        await ctx.message.delete()
        user = user or ctx.author

        random.seed(user.id)
        r = random.randint(1, 100)
        hot = r / 1.17

        emoji = "💔"
        if hot > 25:
            emoji = "❤"
        if hot > 50:
            emoji = "💖"
        if hot > 75:
            emoji = "💞"

        await ctx.send(f"**{user.name}** is **{hot:.2f}%** hot {emoji}")

    @commands.command(aliases=['slots', 'bet'])
    @commands.cooldown(rate=1, per=3.0, type=commands.BucketType.user)
    async def slot(self, ctx):
        """ Roll the slot machine """
        await ctx.message.delete()
        emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
        a = random.choice(emojis)
        b = random.choice(emojis)
        c = random.choice(emojis)

        slotmachine = f"**[ {a} {b} {c} ]\n{ctx.author.name}**,"

        if (a == b == c):
            await ctx.send(f"{slotmachine} All matching, you won! 🎉")
        elif (a == b) or (a == c) or (b == c):
            await ctx.send(f"{slotmachine} 2 in a row, you won! 🎉")
        else:
            await ctx.send(f"{slotmachine} No match, you lost 😢")
    
    @commands.command(name="hypu", aliases=["train"])
    async def hype(self, ctx):
        '''HYPE TRAIN CHOO CHOO'''
        await ctx.message.delete()
        hypu = ['https://cdn.discordapp.com/attachments/102817255661772800/219514281136357376/tumblr_nr6ndeEpus1u21ng6o1_540.gif',
                'https://cdn.discordapp.com/attachments/102817255661772800/219518372839161859/tumblr_n1h2afSbCu1ttmhgqo1_500.gif',
                'https://gfycat.com/HairyFloweryBarebirdbat',
                'https://i.imgur.com/PFAQSLA.gif',
                'https://abload.de/img/ezgif-32008219442iq0i.gif',
                'https://i.imgur.com/vOVwq5o.jpg',
                'https://i.imgur.com/Ki12X4j.jpg',
                'https://media.giphy.com/media/b1o4elYH8Tqjm/giphy.gif']
        msg = f':train2: CHOO CHOO {random.choice(hypu)}'
        await ctx.send(msg)
    
    @commands.command(aliases=['witz', 'joke'])
    async def pun(self, ctx):
        '''Weil jeder schlechte Witze mag'''
        await ctx.message.delete()
        puns = ['Was sagt das eine Streichholz zum anderen Streichholz?\n Komm, lass uns durchbrennen',
                'Wieviele Deutsche braucht man um eine Glühbirne zu wechseln?\n Einen, wir sind humorlos und effizient.',
                'Wo wohnt die Katze?\n Im Miezhaus.',
                'Wie begrüßen sich zwei plastische Chirurgen?\n "Was machst du denn heute für ein Gesicht?"',
                'Warum essen Veganer kein Huhn?\n Könnte Ei enthalten',
                '85% der Frauen finden ihren Arsch zu dick, 10% zu dünn, 5% finden ihn so ok, wie er ist und sind froh, dass sie ihn geheiratet haben...',
                'Meine Freundin meint, ich wär neugierig...\n...zumindest\' steht das in ihrem Tagebuch.',
                '"Schatz, Ich muss mein T-Shirt waschen! Welches Waschmaschinen Programm soll ich nehmen?" - "Was steht denn auf dem T-Shirt drauf?"\n "Slayer!"',
                'Gestern erzählte ich meinem Freund, dass ich schon immer dieses Ding aus Harry Potter reiten wollte.\n"einen Besen?" "nein, Hermine."',
                'Warum gehen Ameisen nicht in die Kirche?\nSie sind in Sekten.',
                'Was steht auf dem Grabstein eines Mathematikers?\n"Damit hat er nicht gerechnet."',
                'Wenn ein Yogalehrer seine Beine senkrecht nach oben streckt und dabei furzt, welche Yoga Figur stellt er da?\n Eine Duftkerze',
                'Warum ging der Luftballon kaputt?\n Aus Platzgründen.',
                'Ich wollte Spiderman anrufen, aber er hatte kein Netz.',
                'Was vermisst eine Schraube am meisten? Einen Vater',
                'Geht ein Panda über die Straße. Bam....Bus!']
        emojis = [':laughing:', ':smile:', ':joy:', ':sob:', ':rofl:']
        msg = f'{random.choice(emojis)} {random.choice(puns)}'
        await ctx.send(msg)
    

    @commands.command(name="kiss")
    async def kiss(self, ctx, member: discord.Member = None):
        '''/r/kiss kiss kiss kiss :3
        Beispiel:
        -----------
        vkiss @lou#xxxx
        '''
        await ctx.message.delete()
        gifs = ['https://media.tenor.com/images/9a48e76b31f2045211817c57c9a47439/tenor.gif',
                'https://media1.tenor.com/images/503bb007a3c84b569153dcfaaf9df46a/tenor.gif',
                'https://media1.tenor.com/images/78095c007974aceb72b91aeb7ee54a71/tenor.gif',
                'https://media1.tenor.com/images/ea9a07318bd8400fbfbd658e9f5ecd5d/tenor.gif',
                'https://media1.tenor.com/images/f102a57842e7325873dd980327d39b39/tenor.gif',
                'https://media1.tenor.com/images/bc5e143ab33084961904240f431ca0b1/tenor.gif',
                'https://media1.tenor.com/images/f5167c56b1cca2814f9eca99c4f4fab8/tenor.gif',
                'https://media.tenor.com/images/dd777838018ab9e97c45ba34596bb8de/tenor.gif',
                'https://media.tenor.com/images/b020758888323338c874c549cbca5681/tenor.gif',
                'https://media.tenor.com/images/02b3ad0fb1d6aa77daeee0ace21d5774/tenor.gif',
                'https://media.tenor.com/images/7e640ecfea0090dd0e29b998c625c642/tenor.gif',
                'https://media.tenor.com/images/45246226e54748be5175ab15206de1c5/tenor.gif',
                'https://68.media.tumblr.com/f95f14437809dfec8057b2bd525e6b4a/tumblr_omvkl2SzeK1ql0375o1_500.gif',
                'https://media.tenor.com/images/5fae48a5065440df87efb803cf8e43ce/tenor.gif',
                'https://media.tenor.com/images/5a6a04fc81d70ef353d928a87ed25f6b/tenor.gif',
                'https://media.tenor.com/images/de18124ebe36764446ee2dbf54a672bf/tenor.gif',
                'https://media.tenor.com/images/a639662ea62cf7c74e594d5f3d030b1a/tenor.gif',
                'https://media.tenor.com/images/5ff039d2eb65999e8a3d2e2eb138e8bf/tenor.gif',
                'https://media.tenor.com/images/a52fc5d0edbe45ff9771555e18514b82/tenor.gif',
                'https://media.tenor.com/images/48ddb8f9bd0580697882ae5e0d70b080/tenor.gif']

        if member == ctx.me:
            msg = f'Arigato {ctx.author.mention} <:lou:820970474820730900> \n{random.choice(gifs)}'
            await ctx.send(msg)
        elif member is not None:
            msg = f'{ctx.author.mention} küsst dich liebevoll {member.mention} :3 \n{random.choice(gifs)}'
            await ctx.send(msg)


    @commands.command(name="pat")
    async def pat(self, ctx, member: discord.Member = None):
        '''/r/headpats Pat Pat Pat :3
        Beispiel:
        -----------
        :pat @Der-Eddy#6508
        '''
        await ctx.message.delete()
        gifs = ['https://gfycat.com/PoisedWindingCaecilian',
                'https://cdn.awwni.me/sou1.jpg',
                'https://i.imgur.com/Nzxa95W.gifv',
                'https://cdn.awwni.me/sk0x.png',
                'https://i.imgur.com/N0UIRkk.png',
                'https://cdn.awwni.me/r915.jpg',
                'https://i.imgur.com/VRViMGf.gifv',
                'https://i.imgur.com/73dNfOk.gifv',
                'https://i.imgur.com/UXAKjRc.jpg',
                'https://i.imgur.com/dzlDuNs.jpg',
                'https://i.imgur.com/hPR7SOt.gif',
                'https://i.imgur.com/IqGRUu4.gif',
                'https://68.media.tumblr.com/f95f14437809dfec8057b2bd525e6b4a/tumblr_omvkl2SzeK1ql0375o1_500.gif',
                'https://i.redd.it/0ffv8i3p1vrz.jpg',
                'http://i.imgur.com/3dzA6OU.png',
                'http://i.imgur.com/vkFKabZ.jpg',
                'https://i.imgur.com/Lb4p20s.jpg',
                'https://cdn.awwni.me/snot.jpg',
                'https://i.imgur.com/5yEOa6u.jpg',
                'https://i.redd.it/dc7oebkfsetz.jpg']

        if member == ctx.me:
            msg = f'Arigato {ctx.author.mention} <:lou:820970474820730900> \n{random.choice(gifs)}'
            await ctx.send(msg)
        elif member is not None:
            msg = f'{ctx.author.mention} tätschelt dich {member.mention} :3 \n{random.choice(gifs)}'
            await ctx.send(msg)


    @commands.command(aliases=['c++', 'c#', 'objective-c'])
    async def csharp(self, ctx):
        '''Wie soll man da überhaupt durchblicken???'''
        await ctx.message.delete()
        await ctx.send(':interrobang: Meintest du C, C++, C# oder Objective-C? https://i.imgflip.com/235kvm.jpg')

    @commands.command(name="whois", aliases=["uis"])
    async def whois(self, ctx, member: discord.Member=None):
        '''Gibt Informationen über einen Benutzer aus
        Beispiel:
        -----------
        :whois @Lou#XXXX
        '''
        await ctx.message.delete()
        if member == None:
            member = ctx.author

        if member.top_role.is_default():
            topRole = 'everyone' #to prevent @everyone spam
            topRoleColour = '#000000'
        else:
            topRole = member.top_role
            topRoleColour = member.top_role.colour

        if member is not None:
            embed = discord.Embed(color=member.top_role.colour)
            embed.set_footer(text=f'UserID: {member.id}')
            embed.set_thumbnail(url=member.avatar_url)
            if member.name != member.display_name:
                fullName = f'{member} ({member.display_name})'
            else:
                fullName = member
            embed.add_field(name=member.name, value=fullName, inline=False)
            embed.add_field(name='Discord beigetreten am', value='{}\n(Tage seitdem: {})'.format(member.created_at.strftime('%d.%m.%Y'), (datetime.now()-member.created_at).days), inline=True)
            embed.add_field(name='Server beigetreten am', value='{}\n(Tage seitdem: {})'.format(member.joined_at.strftime('%d.%m.%Y'), (datetime.now()-member.joined_at).days), inline=True)
            embed.add_field(name='Avatar Link', value=member.avatar_url, inline=False)
            embed.add_field(name='Rollen', value=self._getRoles(member.roles), inline=True)
            embed.add_field(name='Rollenfarbe', value='{} ({})'.format(topRoleColour, topRole), inline=True)
            embed.add_field(name='Status', value=member.status, inline=True)
            await ctx.send(embed=embed)
        else:
            msg = ':no_entry: Du hast keinen Benutzer angegeben!'
            await ctx.send(msg)
    
    @commands.command(name="serverinfo")
    async def serverinfo(self, context):
        """
        Get some useful (or not) information about the server.
        """
        server = context.message.guild
        roles = [x.name for x in server.roles]
        role_length = len(roles)
        if role_length > 50:
            roles = roles[:50]
            roles.append(f">>>> Displaying[50/{len(roles)}] Roles")
        roles = ", ".join(roles)
        channels = len(server.channels)
        time = str(server.created_at)
        time = time.split(" ")
        time = time[0]

        embed = discord.Embed(
            title="**Server Name:**",
            description=f"{server}",
            color=0x00FF00
        )
        embed.set_thumbnail(
            url=server.icon_url
        )
        embed.add_field(
            name="Server ID",
            value=server.id
        )
        embed.add_field(
            name="Member Count",
            value=server.member_count
        )
        embed.add_field(
            name="Text/Voice Channels",
            value=f"{channels}"
        )
        embed.add_field(
            name=f"Roles ({role_length})",
            value=roles
        )
        embed.set_footer(
            text=f"Created at: {time}"
        )
        await context.send(embed=embed)

    @commands.command(name="ping")
    async def ping(self, context):
        """
        Check if the bot is alive.
        """
        await context.message.delete()
        embed = discord.Embed(
            color=0x00FF00
        )
        embed.add_field(
            name="Pong!",
            value=":ping_pong:",
            inline=True
        )
        embed.set_footer(
            text=f"Pong request by {context.message.author}"
        )
        await context.send(embed=embed)

    @commands.command(name="invite")
    async def invite(self, context):
        """
        Get the invite link of the bot to be able to invite it.
        """
        await context.message.delete()
        await context.send("Du hast ne DM erhalten!")
        await context.author.send(f"Invite me by clicking here: https://discordapp.com/oauth2/authorize?&client_id={config.APPLICATION_ID}&scope=bot&permissions=8")

    @commands.command(name="server")
    async def server(self, context):
        """
        Get the invite link of the discord server of the bot for some support.
        """
        await context.message.delete()
        await context.send("Du hast ne DM erhalten!")
        await context.author.send("Join my discord server by clicking here: https://discord.gg/QJfZnSJd7m")

    @commands.command(name="poll")
    async def poll(self, context, *args):
        """
        Create a poll where members can vote.
        """
        await context.message.delete()
        poll_title = " ".join(args)
        embed = discord.Embed(
            title="Dies ist eine neue Abstimmung!",
            description=f"{poll_title}",
            color=0x00FF00
        )
        embed.set_footer(
            text=f"Abstimmung wurde gestartet von: {context.message.author} • reagiere zum voten!"
        )
        embed_message = await context.send(embed=embed)
        await embed_message.add_reaction("👍")
        await embed_message.add_reaction("👎")
        await embed_message.add_reaction("🤷")

    @commands.command(name="8ball")
    async def eight_ball(self, context, *args):
        """
        Ask any question to the bot.
        """
        await context.message.delete()
        answers = ['It is certain.', 'It is decidedly so.', 'You may rely on it.', 'Without a doubt.',
                   'Yes - definitely.', 'As I see, yes.', 'Most likely.', 'Outlook good.', 'Yes.',
                   'Signs point to yes.', 'Reply hazy, try again.', 'Ask again later.', 'Better not tell you now.',
                   'Cannot predict now.', 'Concentrate and ask again later.', 'Don\'t count on it.', 'My reply is no.',
                   'My sources say no.', 'Outlook not so good.', 'Very doubtful.']
        embed = discord.Embed(
            title="**My Answer:**",
            description=f"{answers[random.randint(0, len(answers))]}",
            color=0x00FF00
        )
        embed.set_footer(
            text=f"Question asked by: {context.message.author}"
        )
        await context.send(embed=embed)

    @commands.command(name="bitcoin")
    async def bitcoin(self, context):
        """
        Get the current price of bitcoin.
        """
        await context.message.delete()
        url = "https://api.coindesk.com/v1/bpi/currentprice/BTC.json"
        # Async HTTP request
        async with aiohttp.ClientSession() as session:
            raw_response = await session.get(url)
            response = await raw_response.text()
            response = json.loads(response)
            embed = discord.Embed(
                title=":information_source: Info",
                description=f"Bitcoin price is: ${response['bpi']['USD']['rate']}",
                color=0x00FF00
            )
            await context.send(embed=embed)




def setup(bot):
    bot.add_cog(general(bot))