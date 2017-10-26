import pafy
from pydub import AudioSegment
import os
os.mkdir("MusiK")
print "ONLY TEKNO ALLOWED"
list = pafy.get_playlist("https://www.youtube.com/playlist?list=PLgLQAHLZtaRrenlDBCkwc2Rc-SR4Q_lQw")
for i in list["items"]:
	print "Downloading and converting..."+i["pafy"].title
	filename = i["pafy"].getbestaudio().download(quiet=False)
	AudioSegment.from_file(filename).export("MusiK/"+i["pafy"].title+".mp3", format="mp3")
	os.remove(filename)
print "Ale, gozatelo!"
