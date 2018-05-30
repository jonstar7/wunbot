import os, sys, subprocess
import discord
from discord.ext import commands
import random
import csv
import psutil    

#TODO No such file found
#TODO add utilty to add files

#sets working directory
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

description = '''a bot for launching'''
bot = commands.Bot(command_prefix='???', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def launch(filen : str, content='repeating...'):
    """Launchs a program based on filename"""
    await bot.say("opening " + filen)
    with open('files.csv') as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            if row[0] == filen:
                print("launching " + row[1])
                #open_file(row[1])
                
                #joins the working directory and the filename
                abs_file_path_row = os.path.join(abs_file_path,row[1])
                open_file(abs_file_path_row)
@bot.command()
async def test(programName : str, content='repeating...'):
    await bot.say("testing ")

#beginning of testing if a program is open or closed			
# @bot.command()
# async def cir(programName : str, content='repeating...'):
# 	if programName in (p.name() for p in psutil.process_iter()):
# 		print(programName + " is running")
# 		await bot.say(programName + " is running")
# 	else:
# 		print(programName + " is not open")
# 		await bot.say(programName + " is not open")
		
		
# @bot.command()
# async def close(filen : str, content='repeating...'):
    # """Launchs a program based on filename"""
    # await bot.say("closing " + filen)
    # with open('files.csv') as csvDataFile:
        # csvReader = csv.reader(csvDataFile)
        # for row in csvReader:
            # if row[0] == filen:
                # print("closing " + row[1])
				# for proc in psutil.process_iter():
					# if proc.name() == row[2]:
						# proc.kill()

bot.run(apikey)
