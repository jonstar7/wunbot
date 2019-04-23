import discord
from discord.ext import commands
import asyncio
import datetime
import glob, csv
import os, sys, subprocess, random
import psutil 
import sqlite3
import youtube_dl

# local imports
import music
import fileSender



bot = commands.Bot(command_prefix='$')
apikey = os.getenv("apikey")
channelID = os.getenv("channelID")
bot = commands.Bot(command_prefix=commands.when_mentioned_or("!"),
                   description='Slap your friends')

# sql variables
aliasDB = "aliases.db"
aliasTable = "strike"

conn = sqlite3.connect(aliasDB)
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS alias (
    id integer PRIMARY KEY, 
    name text
    )""")
conn.commit()

reactionLock = asyncio.Lock()

reactionMemberDict = {
}

@bot.command()
async def length(ctx):
    await ctx.send('Your message is {} characters long.'.format(len(ctx.message.content)))

@bot.command()
async def t(ctx):
    msg = await ctx.message.author.fetch_message(570140364036505600)
    await ctx.send('Your message is {} characters long.'.format(len(msg.content)))
last_chan_sent_msg_id = 0
@bot.command()
async def goode(ctx):
    # await asyncio.sleep(3)
    # print(ctx.message.author.id) 
    reactionMemberDict[ctx.message.author.id] = ctx.message.id
    await ctx.send('message id = {}'.format(ctx.message.id))
    await ctx.send('React to this message with every good boy emote{}'.format(ctx.message.reactions))
    last_chan_sent_msg_id = ctx.channel.last_message_id
    lastMsg = await ctx.channel.fetch_message(last_chan_sent_msg_id)
    print(lastMsg)

@bot.command()
async def finish(ctx):
    lastMsg = await ctx.channel.fetch_message(last_chan_sent_msg_id)
    print(lastMsg)
    react_list = lastMsg.reactions
    await ctx.send('react_list = {}'.format(react_list))
    # messid = 0
    # if ctx.message.author.id in reactionMemberDict:
    #     messid = reactionMemberDict[ctx.message.author.id]
    #     await ctx.send('messid = {}'.format(messid))
    # else:
    #     await ctx.send('Please run the accompanying command first')
    #     return
    # msg = await ctx.message.author.fetch_message(messid)
    # await ctx.send('Reactions: {}'.format(ctx.message.reactions))


@bot.event
async def on_message(message):
    if message.content.startswith('and DANCE'):
        await message.channel.send(':D-<')
        await message.channel.send(':D|-<')
        await message.channel.send(':D/-<')
    
    # allows @bot.command() to continue functioning
    await bot.process_commands(message)

@bot.event
async def on_reaction_add(reaction, user):
    channel = reaction.message.channel
    # debug limiting to #commands
    if channel != bot.get_channel(139855291629043713):
        return
    print(reaction.emoji)
    await channel.send('{} has added {} to the message {}'.format(user.name,reaction.emoji,reaction.message.content))



# mean easter egg 
@bot.event
async def on_message_delete(message):
    alex = bot.get_member(126249469950951424) # gets alex
    if alex == message.author:
        fmt = '{0.author} has deleted the message: {0.content}'
        msgchan = bot.get_channel(487356952528027670) # proletariat_resistance
        await msgchan.send(fmt.format(message))

class Alias(commands.Cog):
    """Holds alias manipulation. Resides in its own cog for learning purposes."""
    def __init__(self, bot):
        self.bot = bot
        tid = 9845780123
        name = "coruman"
        # TODO should alias be deleted if member is gone for x days?
        # TODO maybe add prune command
    @commands.command()
    async def alias(self, ctx):
        """TODO"""
        await ctx.send("Alias test")
        

        # await ctx.send(memlistname)
    @commands.command()
    async def editalias(self, ctx, arg):
        """TODO"""
        await ctx.send("Alias test")

@bot.event
async def on_ready():
    print('Logged in as {0} ({0.id})'.format(bot.user))
    print('------')

    # creates temp table to compare changes
    c.execute("""CREATE TEMPORARY TABLE temp (
    id integer PRIMARY KEY, 
    name text
    )""")

    # iterate through all members and add to temp table
    members = bot.get_all_members()
    for member in members:
        c.execute("INSERT INTO temp VALUES ({},'{}')".format(member.id, member.name))
    
    # compare temp with alias and Insert Where Not Exists 
    c.execute("""
    INSERT INTO alias (id, name)
    SELECT id, name
    FROM temp
    WHERE NOT EXISTS (Select id, name From alias WHERE alias.id = temp.id)
    """)

    # commits changes and prints debug message
    conn.commit()
    c.execute("SELECT * FROM alias")
    print("okay")
    print(c.fetchall())

bot.add_cog(music.Music(bot))
bot.add_cog(fileSender.FileSender(bot))
bot.add_cog(Alias(bot))
bot.run(apikey)
