import eyed3

file = "/media/cola/Transfer/Download/SCscrape/sven/Electrica Salsa feat. Sven Väth (Henrik Schwarz Radio Edit).mp3"


def make_tag(file, artist, title, album="", trno="", r_date=""):
	print("penis")
    try:
        audiofile = eyed3.load(normalize_filename(file))
        audiofile.initTag()
        
        tag = audiofile.tag
        tag.artist = artist        
        tag.album = album
        tag.release_date = r_date
        tag.title = title
        #tag.track_num = trno
        
        tag.save()
    except Exception as e:
        print(e)

        
def print_tag(file):
    try:
        audiofile = eyed3.load(normalize_filename(file))
        tag = audiofile.tag
        
        print(tag.artist)
        print(tag.album)
        print(tag.title)
        print(tag.release_date)
        print(tag.track_num)
    except Exception as e:
        print(e)