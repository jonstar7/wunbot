import discord
from discord.ext import commands
import asyncio
import datetime
import glob, csv
import os, sys, subprocess, random
import psutil 
import sqlite3
import youtube_dl
from dotenv import load_dotenv

# local imports
import music
# import fileSender
# import disorder
# import alias

load_dotenv() # load secrets from .gitignored .env file 
# bot = commands.Bot(command_prefix='$')
apikey = os.getenv("apikey")
# channelID = os.getenv("channelID")
bot = commands.Bot(command_prefix=commands.when_mentioned_or("!"),
                   description='Slap your friends')

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

reactSetupDone = False
@bot.command()
async def goode(ctx):
    # await asyncio.sleep(3)
    # print(ctx.message.author.id) 
    reactSetupDone = False
    reactionMemberDict[ctx.message.author.id] = ctx.message.id
    await ctx.send('message id = {}'.format(ctx.message.id))
    await ctx.send('React to this message with every good boy emote{}'.format(ctx.message.reactions))
    last_chan_sent_msg_id = ctx.channel.last_message_id
    lastMsg = await ctx.channel.fetch_message(last_chan_sent_msg_id)
    print(lastMsg)
    while reactSetupDone != True:
        await ctx.send('we\'re stuck in a loop reactSetupDone={}'.format(reactSetupDone))
        await asyncio.sleep(1)
    reactSetupDone = False
    react_list = lastMsg.reactions
    await ctx.send('react_list = {}'.format(react_list))


@bot.command()
async def finish(ctx):
    await ctx.send('Finishing')
    reactSetupDone = True
    # messid = 0
    # if ctx.message.author.id in reactionMemberDict:
    #     messid = reactionMemberDict[ctx.message.author.id]
    #     await ctx.send('messid = {}'.format(messid))
    # else:
    #     await ctx.send('Please run the accompanying command first')
    #     return
    # msg = await ctx.message.author.fetch_message(messid)
    # await ctx.send('Reactions: {}'.format(ctx.message.reactions))

@bot.command()
async def alex(ctx):
    await ctx.send("alex is {} should be {}".format(bot.get_user(126249469950951424), 126249469950951424))

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


@bot.event
async def on_member_update(before,after):
        n = after.nick
        if n:
            if n.lower().count("tim") > 0:
                last = before.nick
                if last:
                    await after.edit(nick=last)
                else:
                    await after.edit(nick="Naw man do not do it")

@bot.event
async def on_ready():
    print('Logged in as {0} ({0.id})'.format(bot.user))
    print('------')
    bot.add_cog(music.Music(bot))
    # bot.add_cog(fileSender.FileSender(bot))
    bot.add_cog(alias.Alias(bot))
    bot.add_cog(disorder.Disorder(bot))
    bot.add_cog(music.Alarm(bot))



bot.run(apikey)
