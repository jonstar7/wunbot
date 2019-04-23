
import discord
from discord.ext import commands
import asyncio
import datetime
import glob, csv
import os, sys, subprocess, random
import psutil 
import sqlite3
import youtube_dl

class FileSender(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    today = datetime.datetime.now()
    day_of_year = (today - datetime.datetime(today.year, 1, 1)).days + 1
    filenames = glob.glob1('pictures', '*.*')
    filenames = sorted(filenames, key=lambda x: float(x.split()[0]))
    canSend = True


    script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
    rel_path = "files"
    abs_file_path = os.path.join(script_dir, rel_path)
    filename = " "
    def open_file(filename):
        if sys.platform == "win32":
            os.startfile(filename)
        else:
            opener ="open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, filename])
    
    async def my_background_task():
        file = open("sendtracker.txt", "r") 
        contents = file.read()
        if int(contents) == day_of_year:
            canSend = False
        else:
            canSend = True
        file.close()
        if canSend:
            canSend = False
            await bot.wait_until_ready()
            channel = bot.get_channel(channelID)
            try:
                file = open("sendtracker.txt","w+") 
                file.write(str(day_of_year))
                file.close()
                await channel.send("pictures\\" + filenames[day_of_year])
                await asyncio.sleep(5)
            except:
                print("File for day " + str(day_of_year) + " not found")






