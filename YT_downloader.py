from pytube import YouTube
from sys import argv

link = argv[0]
yt= YouTube('https://www.youtube.com/watch?v=eFqUUlQSsbo')

print("Title: ", yt.title)

print("View: ", yt.views)

yd = yt.streams.get_highest_resolution()

yd.download('E:/pythonDownloader')