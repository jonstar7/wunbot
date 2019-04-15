# wunbot

wunbot is an unfinished Discord bot written in [Python](https://www.python.org "Python homepage").
Everything is in flux and it's great.

![](gluten-free)
<img src="https://forthebadge.com/images/badges/gluten-free.svg"> ![](not-an-issue)<img src="https://forthebadge.com/images/badges/not-an-issue.svg">
### How do I set it up?

Get that Python 3 virtual environment set up in Linux with a quick 
```bash
python3 -m virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```
And of course for Windows instead of `source venv/bin/activate` use `.\venv\Scripts\activate`

Or you could simply replace the apikey variable inside wunbot.py with your Discord bot's apikey and run like any other Python program `python3 wunbot.py` 

On Windows, I like to make a .bat with the contents. For Linux replace "SET" with "export" and add quotes around the api key.
```
SET apikey=YOUR_ACTUAL_API_KEY
python FILENAME_TO_RUN.py
pause
```

Powered by [Discord.py](https://github.com/Rapptz/discord.py)

### Commands
#### No longer accurate, will be updating when stable. 
wunbot_LaunchFile.py:
`???launch [filename]`
launches files on the host computer in "bot directory/files"

wunbot_SendFileOnceDaily.py:
`!dayn` sends message with day/365
`!potd` sends pictures of the day

### Configuration

Add your bot's channelID for the posting of images in the designated location in wunbot.py
