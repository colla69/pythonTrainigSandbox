"""This is my new NesterFunction"""
from collections import defaultdict
import os
import eyed3

eyed3.log.setLevel("ERROR")


def normalize_filename(filename):
    return filename.encode("utf-8", "replace").decode("utf-8", "escape")


def get_data_from_dir(rootdir):
    files_dict = defaultdict(list)
    f_count = 0
    artists = defaultdict
    titles = defaultdict

    for dirName, subdirList, fileList in os.walk(rootdir):
        for f_name in fileList:
            try:
                if 'mp3' in f_name or 'wav' in f_name or 'flac' in f_name:
                    files_dict[dirName].append(f_name)
                    file = dirName + '/' + f_name
                    audiofile = eyed3.load(path=file)
                    artist = audiofile.tag.artist
                    artists[artist] = 0

                    title = audiofile.tag.title
                    titles[tilte] = 0
                    f_count += 1
            except:
                continue
    return files_dict, f_count, artists, titles


def print_lol(the_list, spacing=0):
    # print(type(the_list))
    if isinstance(the_list, list):
        for each_item in the_list:
            print_lol(each_item)
    elif isinstance(the_list, defaultdict):
        for key in the_list:
            print('%s' % normalize_filename(key))
            print_lol(the_list[key], spacing+1)
    else:
        print('\t' + normalize_filename(the_list))


def print_tag(file):
    audiofile = eyed3.load(normalize_filename(file))

    print('')
    try:
        print( "artist: " + audiofile.tag.artist )
    except:
        print("artist: none" )
    try:
        print("title: " + audiofile._tag.title)
    except:
        print("artist: none" )
    try:
        print("album: " + audiofile._tag.album)
    except:
        print("artist: none" )
    try:
        print("genre: " + audiofile._tag.genre.name)
    except:
        print("artist: none" )