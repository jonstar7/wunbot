
# Discord bot that sends 1 file in pictures/*.* based on the day, once daily. 

import discord
# from discord.ext import commands
import asyncio
import datetime
import glob, csv
import os, sys, subprocess
import psutil 

client = discord.Client()

apikey = os.getenv("apikey")
channelID = os.getenv("channelID")

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

# description = '''a bot for launching'''
# bot = commands.Bot(command_prefix='???', description=description)

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
        await client.wait_until_ready()
        channel = discord.Object(id=channelID)
        try:
            file = open("sendtracker.txt","w+") 
            file.write(str(day_of_year))
            file.close()
            await client.send_file(channel, "pictures\\" + filenames[day_of_year])
            await asyncio.sleep(5)
        except:
            print("File for day " + str(day_of_year) + " not found")

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await my_background_task()

@client.event
async def on_message(message):
    await my_background_task()

    if message.content.startswith('!dayn'):
        await client.send_message(message.channel, day_of_year)
    elif message.content.startswith('!potd'):
        try:
            await client.send_file(message.channel, "pictures\\" + filenames[day_of_year])
        except:
            await client.send_message(message.channel, "File for day "+ str(day_of_year) + " not found")
    elif message.content.startswith('!launch Sev'): # terrible code
        await client.send_message(message.channel, "opening " + "Sev")
        with open('files.csv') as csvDataFile:
            csvReader = csv.reader(csvDataFile)
            for row in csvReader:
                if row[0] == "Sev":
                    print("launching " + row[1])
                    #open_file(row[1])
                    
                    #joins the working directory and the filename
                    abs_file_path_row = os.path.join(abs_file_path,row[1])
                    open_file(abs_file_path_row)
    elif message.content.startswith('!launch sev'):# terrible code, I'm sorry albert einstein 
        await client.send_message(message.channel, "opening " + "Sev")
        with open('files.csv') as csvDataFile:
            csvReader = csv.reader(csvDataFile)
            for row in csvReader:
                if row[0] == "Sev":
                    print("launching " + row[1])
                    #open_file(row[1])
                    
                    #joins the working directory and the filename
                    abs_file_path_row = os.path.join(abs_file_path,row[1])
                    open_file(abs_file_path_row)



client.run(apikey)
