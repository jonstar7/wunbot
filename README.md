# wunbot

wunbot is an unfinished Discord bot written in [Python](https://www.python.org "Python homepage").
Everything is in flux and it's great.

<img src="https://forthebadge.com/images/badges/made-with-python.svg">
<img src="https://forthebadge.com/images/badges/gluten-free.svg"> <img src="https://forthebadge.com/images/badges/uses-badges.svg"> <img src="https://forthebadge.com/images/badges/not-an-issue.svg"> 


### How do I set it up?

Get that Python 3 virtual environment set up in Linux with a quick 
```bash
python3 -m virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

Make sure to set your API_KEY in `.env`

And of course for Windows instead of `source venv/bin/activate` use `.\venv\Scripts\activate`

Or you could simply replace the apikey variable inside wunbot.py with your Discord bot's apikey and run like any other Python program `python3 wunbot.py` 

Powered by [Discord.py](https://github.com/Rapptz/discord.py)
