#DAY 49 -50 OF 100 DAYS OF CODE
#PYTHON PROJECT - YOUTUBE VIDEO DOWNLOADER
pip install pytube3
from pytube import YouTube
link =input("Enter the link: ")
vid= Youtube(link)

print("Title: ", yt.title)
print("Length: ", yt.length, "seconds")

hd= yt.stream.get_highest_resolution()
print("downloading")
hd.download()
print("downloaded complete")
