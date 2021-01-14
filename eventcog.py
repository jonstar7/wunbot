from __future__ import print_function
import discord
from discord.ext import commands
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
# from google_auth_oauthlib.flow import InstalledAppFlow
import google_auth_oauthlib.flow
import google.oauth2.credentials

from google.auth.transport.requests import Request
from oauth2client import client
from googleapiclient import sample_tools
import json

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


# def cal_quickstart():



# # if __name__ == '__main__':
# #     main()

class EventCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    async def joined(self, ctx, *, member: discord.Member):
        """Says when a member joined."""
        await ctx.send(f'{member.display_name} joined on {member.joined_at}')

    @commands.command(name='coolbot')
    async def cool_bot(self, ctx):
        """Is the bot cool?"""
        await ctx.send('This bot is cool. :)')

    @commands.command(name='top_role', aliases=['toprole'])
    @commands.guild_only()
    async def show_toprole(self, ctx, *, member: discord.Member=None):
        """Simple command which shows the members Top Role."""

        if member is None:
            member = ctx.author

        await ctx.send(f'The top role for {member.display_name} is {member.top_role.name}')
    
    @commands.command(name='perms', aliases=['perms_for', 'permissions'])
    @commands.guild_only()
    async def check_permissions(self, ctx, *, member: discord.Member=None):
        """A simple command which checks a members Guild Permissions.
        If member is not provided, the author will be checked."""

        if not member:
            member = ctx.author

        # Here we check if the value of each permission is True.
        perms = '\n'.join(perm for perm, value in member.guild_permissions if value)

        # And to make it look nice, we wrap it in an Embed.
        embed = discord.Embed(title='Permissions for:', description=ctx.guild.name, colour=member.colour)
        embed.set_author(icon_url=member.avatar_url, name=str(member))

        # \uFEFF is a Zero-Width Space, which basically allows us to have an empty field name.
        embed.add_field(name='\uFEFF', value=perms)

        await ctx.send(content=None, embed=embed)
        # Thanks to Gio for the Command.

    @commands.command(name='auth', aliases=['auther'])
    @commands.guild_only()
    async def auth(self, ctx, *, member: discord.Member=None):
        """Shows basic usage of the Google Calendar API.
        Prints the start and name of the next 10 events on the user's calendar.
        """
        # creds = None
        # # The file token.pickle stores the user's access and refresh tokens, and is
        # # created automatically when the authorization flow completes for the first
        # # time.
        # if os.path.exists('token.pickle'):
        #     with open('token.pickle', 'rb') as token:
        #         creds = pickle.load(token)
        # # If there are no (valid) credentials available, let the user log in.
        # if not creds or not creds.valid:
        #     if creds and creds.expired and creds.refresh_token:
        #         creds.refresh(Request())
        #     else:
        #         flow = InstalledAppFlow.from_client_secrets_file(
        #             'credentials.json', SCOPES)
        #         creds = flow.run_local_server(port=0)
        #     # Save the credentials for the next run
        #     with open('token.pickle', 'wb') as token:
        #         pickle.dump(creds, token)
        
        flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file('credentials.json', SCOPES)
        flow.redirect_uri = 'https://www.chancey.dev/'

        # Generate URL for request to Google's OAuth 2.0 server. 
        # #https://developers.google.com/identity/protocols/oauth2/web-server#python
        # Use kwargs to set optional request parameters.
        authorization_url, state = flow.authorization_url(
            # Enable offline access so that you can refresh an access token without
            # re-prompting the user for permission. Recommended for web server apps.
            access_type='offline',
            # Enable incremental authorization. Recommended as a best practice.
            include_granted_scopes='true')
        print(authorization_url)
        await ctx.send(f"Authorize here {authorization_url}")



        # with build('calendar', 'v3', credentials=creds) as service:
        #     # Call the Calendar API
        #     now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
        #     print('Getting the upcoming 10 events')
        #     events_result = service.events().list(calendarId='primary', timeMin=now,
        #                                         maxResults=10, singleEvents=True,
        #                                         orderBy='startTime').execute()
        #     events = events_result.get('items', [])

        #     if not events:
        #         print('No upcoming events found.')
        #     for event in events:
        #         start = event['start'].get('dateTime', event['start'].get('date'))
        #         print(start, event['summary'])

        #     if member is None:
        #         member = ctx.author
        


# The setup function below is necessary. Remember we give bot.add_cog() the name of the class in this case MembersCog.
# When we load the cog, we use the name of the file.
def setup(bot):
    bot.add_cog(EventCog(bot))