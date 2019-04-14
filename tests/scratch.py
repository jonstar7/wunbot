# @bot.event
# async def discord.on_command(left : int, right : int):
#     """Adds two numbers together."""
#     await bot.say(left + right)


# @bot.command(pass_context=True)
# async def and(ctex):
#     if "dance" in ctx.message.content:
#         await ctx.send('Your message is {} characters long.'.format(ctx.message.content))
    
    
    

# @bot.group()
# async def get(ctx):
#     if ctx.invoked_subcommand is None:
#         await ctx.send('Invalid dance command passed...')

# @git.command()
# async def push(ctx, remote: str, branch: str):
#     await ctx.send('Pushing to {} {}'.format(remote, branch))



# @bot.event
# async def on_message(message):
#     await my_background_task()

#     if message.content.startswith('!dayn'):
#         await bot.send_message(message.channel, day_of_year)
#     elif message.content.startswith('!potd'):
#         try:
#             await bot.send_file(message.channel, "pictures\\" + filenames[day_of_year])
#         except:
#             await bot.send_message(message.channel, "File for day "+ str(day_of_year) + " not found")
#     elif message.content.startswith('!strike'):
#         temp_strike_msg = "Strike given to " + message.content[8:]
#         await bot.send_message(message.channel, temp_strike_msg) #, tts=True
#         # await bot.send_message(message.channel, message.mentions[0])
#         conn = sqlite3.connect(strikeDB)
#         c = conn.cursor()
#         #  Creating a new SQLite table with 1 column
#         c.execute('CREATE TABLE {tn} ({nf} {ft},strikes integer)'\
#                 .format(tn=strikeTable, nf="user", ft="TEXT"))


#         conn.commit()
#         conn.close()


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
    #     await bot.send_message(message.channel, "opening " + "Sev")
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
    #     await bot.send_message(message.channel, "opening " + "Sev")
    #     with open('files.csv') as csvDataFile:
    #         csvReader = csv.reader(csvDataFile)
    #         for row in csvReader:
    #             if row[0] == "Sev":
    #                 print("launching " + row[1])
    #                 #open_file(row[1])
                    
    #                 #joins the working directory and the filename
    #                 abs_file_path_row = os.path.join(abs_file_path,row[1])
    #                 open_file(abs_file_path_row)

