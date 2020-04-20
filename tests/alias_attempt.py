import discord
from discord.ext import commands
import asyncio
import datetime
import sqlite3
# import pdb; pdb.set_trace()

# sql variables
aliasDB = "aa.db"
aliasTable = "strike"

conn = sqlite3.connect(aliasDB)
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS alias (
    id integer PRIMARY KEY, 
    name text,
    disorder_id text
    )""")
conn.commit()

class Alias(commands.Cog):
    """Holds alias manipulation. Resides in its own cog for learning purposes."""
    def __init__(self, bot):
        self.bot = bot
        tid = 9845780123
        name = "coruman"
        # TODO should alias be deleted if member is gone for x days?
        # TODO maybe add prune command

        # iterate through all members and add to alias table
        members = bot.get_all_members()
        # breakpoint()
        
        # print("printing members")
        # for member in members:
        #     print(member.id, member.name)
        
        print("inserting members")
        
        # create temp database
        c.execute("""
        CREATE TEMPORARY TABLE temp (
        id integer PRIMARY KEY, 
        name text,
        disorder_id text
        )""")
        for member in members:
            # print("INSERT INTO alias VALUES ({}, '{}', '{}')".format(member.id, member.name, "0"))
            c.execute("INSERT INTO temp VALUES ({}, '{}', '{}')".format(member.id, member.name, "0"))
        
        # add new values
        # c.execute(
        #     """
        #     INSERT INTO alias (id, name, disorder_id)
        #     SELECT * from temp
        #     EXCEPT
        #     SELECT * from alias
        #     """)
        # saved just in case * causes problems later
        c.execute(
            """
            INSERT INTO alias (id, name, disorder_id)
            SELECT id, name, disorder_id from temp
            EXCEPT
            SELECT id, name, disorder_id from alias
            """)


        # commits changes and prints debug message
        conn.commit()

        c.execute("SELECT * FROM alias")
        print("output of c.fetchall()")
        print(c.fetchall())
        conn.commit()
        conn.close()
        
        
    @commands.command()
    async def alias(self, ctx):
        """TODO"""
        await ctx.send("Alias test")
        

        # await ctx.send(memlistname)
    @commands.command()
    async def editalias(self, ctx, arg):
        """TODO"""
        await ctx.send("Alias test")