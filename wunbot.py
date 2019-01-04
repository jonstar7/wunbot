
# Discord bot that sends 1 file in pictures/*.* based on the day, once daily. 

import discord
from discord.ext import commands
import asyncio
import datetime
import glob, csv
import os, sys, subprocess
import psutil 
import sqlite3

bot = commands.Bot(command_prefix='$')
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


# sql variables
strikeDB = "testdatabase.db"
strikeTable = "strike"

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

# @client.event
# async def discord.on_command(left : int, right : int):
#     """Adds two numbers together."""
#     await bot.say(left + right)


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
    elif message.content.startswith('!strike'):
        temp_strike_msg = "Strike given to " + message.content[8:]
        await client.send_message(message.channel, temp_strike_msg) #, tts=True
        # await client.send_message(message.channel, message.mentions[0])
        conn = sqlite3.connect(strikeDB)
        c = conn.cursor()
        #  Creating a new SQLite table with 1 column
        c.execute('CREATE TABLE {tn} ({nf} {ft},strikes integer)'\
                .format(tn=strikeTable, nf="user", ft="TEXT"))


        conn.commit()
        conn.close()


        # temp_list = []
        # with open('strikes.csv', newline='') as csvfile:
        #     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        #     for row in spamreader:
        #         print(' '.join(row))
        #     temp_list.extend(spamreader)
        # with open('strikes.csv', 'w+', newline='') as csvfile:
        #     spamwriter = csv.writer(csvfile, delimiter=' ',
        #                     quotechar='|', quoting=csv.QUOTE_MINIMAL)
        #     for line, row in enumerate(temp_list):
        #         data = message.mentions[0].get(line, row)
        #         spamwriter.writerow(data)


        # TODO add launching functionality back
        # TODO add restart and stop functionality
        # TODO add user friendly way to add and remove programs
        # TODO add command to display currently running programs 
        # TODO add python image generation and send images with information about currently running programs

        # with open('strikes.csv', 'rb') as infile, open('strikes.csv.new', 'wb') as outfile:
        # # with open('strikes.csv','w+',newline='\n') as csvDataFile:
        # #     csvReader = csv.reader(csvDataFile)
        # #     csvWriter = csv.writer(csvDataFile)
        #     writer = csv.writer(outfile)
        #     print("writer init")
        #     for row in csv.writer(infile):
        #         if row[0] == message.mentions[0]:
        #             print("if")
        #             # print(message.mentions[0] + " has " + row[1] + " strikes.")
        #             # writer.writerow([message.mentions[0]], 1)
        #         else:
        #             print("else")
        #             ## newstrike = row[1]+1
        #             # writer.writerow([message.mentions[0]], 1)
        # os.rename('strikes.csv.new','strikes.csv')
    # elif message.content.startswith('!launch Sev'): # terrible code
    #     await client.send_message(message.channel, "opening " + "Sev")
    #     with open('files.csv') as csvDataFile:
    #         csvReader = csv.reader(csvDataFile)
    #         for row in csvReader:
    #             if row[0] == "Sev":
    #                 print("launching " + row[1])
    #                 #open_file(row[1])
                    
    #                 #joins the working directory and the filename
    #                 abs_file_path_row = os.path.join(abs_file_path,row[1])
    #                 open_file(abs_file_path_row)
    # elif message.content.startswith('!launch sev'):# terrible code, I'm sorry albert einstein 
    #     await client.send_message(message.channel, "opening " + "Sev")
    #     with open('files.csv') as csvDataFile:
    #         csvReader = csv.reader(csvDataFile)
    #         for row in csvReader:
    #             if row[0] == "Sev":
    #                 print("launching " + row[1])
    #                 #open_file(row[1])
                    
    #                 #joins the working directory and the filename
    #                 abs_file_path_row = os.path.join(abs_file_path,row[1])
    #                 open_file(abs_file_path_row)



client.run(apikey)
