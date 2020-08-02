import discord
from discord.ext import commands
import asyncio
import datetime

class Disorder(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
    
    # virus object
    class Virus:
        def __init__(self, name, level, date_created):
            self.name = name
            self.level = age
            self.date_created = date_created

        def myfunc(self, abc):
            print("Hello my name is " + abc.name)


    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send('Welcome {0.mention}.'.format(member))

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        pass

    @commands.command()
    async def pet(self, ctx):
        await ctx.send('*~ bips and bobs happily! ~*')
        # print(ctx.author)
        # await ctx.send('Hello {0.name}~'.format(member))
        # channel = member.guild.system_channel
        # if channel is not None:
        #     await channel.send('Welcome {0.mention}.'.format(member))

        


    @commands.command()
    async def hello(self, ctx, *, member: discord.Member = None):
        """Says hello"""
        member = member or ctx.author

        # retrieve cog by name
        alias = self.bot.get_cog('Alias')

        if self._last_member is None or self._last_member.id != member.id:
            await ctx.send('Hello {0.name}~'.format(member))
            retrieved_member = await alias.isMemberInfected(member.id)
            await ctx.send('{}'.format(retrieved_member))

        else:
            await ctx.send('Hello {0.name}... This feels familiar.'.format(member))
        self._last_member = member