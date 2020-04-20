import discord
from discord.ext import commands
import asyncio
import datetime
import sqlite3

# sql variables
aliasDB = "aliases.db"
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
        
        # creates temp table to compare changes
        c.execute("""CREATE TEMPORARY TABLE temp (
        id integer PRIMARY KEY, 
        name text,
        disorder_id text
        )""")

        # iterate through all members and add to temp table
        members = bot.get_all_members()
        for member in members:
            c.execute("INSERT INTO temp VALUES ({},'{}','{}')".format(member.id, member.name, "0"))
        
        # compare temp with alias and Insert Where Not Exists 
        c.execute("""
        INSERT INTO alias (id, name, disorder_id)
        SELECT id, name, disorder_id
        FROM temp
        WHERE NOT EXISTS (Select id, name, disorder_id From alias WHERE alias.id = temp.id)
        """)

        # commits changes and prints debug message
        conn.commit()
        c.execute("SELECT * FROM alias")
        print("output of c.fetchall()")
        print(c.fetchall())
        
    @commands.command()
    async def alias(self, ctx):
        """TODO"""
        await ctx.send("Alias test")
        

        # await ctx.send(memlistname)
    @commands.command()
    async def editalias(self, ctx, arg):
        """TODO"""
        await ctx.send("Alias test")