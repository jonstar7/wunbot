
# Discord bot that sends 1 file in pictures/*.* based on the day, once daily. 

import discord
import asyncio
import datetime
import glob
import os

client = discord.Client()

apikey = os.getenv("apikey")
today = datetime.datetime.now()
day_of_year = (today - datetime.datetime(today.year, 1, 1)).days + 1
filenames = glob.glob1('pictures', '*.*')
filenames = sorted(filenames, key=lambda x: float(x.split()[0]))

async def my_background_task():
    file = open("sendtracker.txt", "r") 
    contents = file.read()
    file.close()
    if int(contents) == day_of_year:
        print("It's equal")
    else:
        await client.wait_until_ready()
        channel = discord.Object(id='347476380763684876')
        try:
            await client.send_file(channel, "pictures\\" + filenames[day_of_year])
            file = open("sendtracker.txt","w+") 
            file.write(str(day_of_year))
            file.close() 
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
    if message.content.startswith('!test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')
    elif message.content.startswith('!dayn'):
        await client.send_message(message.channel, day_of_year)
    elif message.content.startswith('!potd'):
        try:
            await client.send_file(message.channel, "pictures\\" + filenames[day_of_year])
        except:
            await client.send_message(message.channel, "File for day "+ str(day_of_year) + " not found")


client.run(apikey)
