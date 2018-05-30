import datetime
import glob
# import os


today = datetime.datetime.now()
day_of_year = (today - datetime.datetime(today.year, 1, 1)).days + 1

filenames = glob.glob('pictures/*.png')
file = open("sendtracker.txt", "r") 
contents = file.read()
file.close()
print(contents)
print(day_of_year)

if int(contents) == day_of_year:
    print("It's equal")
else:
    print("false")
    file = open("sendtracker.txt","w+") 
    file.write(str(day_of_year))
    file.close() 
