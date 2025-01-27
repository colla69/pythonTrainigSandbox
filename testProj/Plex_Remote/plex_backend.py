from collections import defaultdict
from json import load, dump
from plexapi.myplex import MyPlexAccount
from plexapi.server import PlexServer


token = "y9pLd6uPWXpwbw14sRYf"
plexurl = "http://plex.colarietitosti.info:32400"
libname = "music"
data_path = "data.json"

class PlexBackend():
            
    def __init__(self, plexurl, token, libname, data_path):
        self.token = token
        self.plexurl = plexurl
        self.lib_name = libname
        self.data_path = data_path
        self.plex = PlexServer(self.plexurl, self.token)
        self.music = self.plex.library.section(self.lib_name)
                       
    def down_plex_lib(self):                
        songs = {}
        try:
            playlists = self.plex.playlists()
            songs["playlist"] = {}
            for p in playlists:
                p_name = p.title                
                songs["playlist"][p_name] = []
                for track in p.items():
                    title = track.title   
                    file_key = self.get_file(track)
                    file = self.get_tokenized_uri( file_key )
                    songs["playlist"][p_name].append([title, file])
            root = self.music.all()
            artists = defaultdict(list)
            albums = defaultdict(list)
            titles = defaultdict(list)
            count = 0    
            for artist in root:
                artist_title = artist.title
                songs[artist_title] = {}
                print(artist_title)
                for album in artist.albums():
                    album_title = album.title
                    songs[artist_title][album_title] = []                    
                    for track in album.tracks():                                                
                        title = track.title                        
                        file_key = self.get_file(track)
                        file = self.get_tokenized_uri( file_key )
                        try:
                            print("""%d 
            %s -- %s 
            %s
            %s

                            """ % (count, artist_title, album_title, title,file_key))
                            songs[artist_title][album_title].append([title, file])
                            count += 1                                  
                        except Exception as ex:
                            print(ex)
            self.json_save(songs, self.data_path)
            print("done loading library")
        finally:
            #self.refreshing_lib = False
            return songs
    
    def json_save(self, data, fname):
        with open(fname, 'w') as fp:
            dump(data, fp)

    def json_load(self, fname):
        with open(fname, 'r') as fp:
            return load(fp)
        
    def get_tokenized_uri(self, uri):
        return plexurl+uri+"?X-Plex-Token="+token

    def get_file(self,track):
        for media in track.media:
            for p in media.parts:
                return p.key