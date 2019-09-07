
from collections import defaultdict
import matplotlib.pyplot as plt
import pymysql
from psw import psw
from enum import Enum
import matplotlib.dates as mdates
from datetime import datetime

linkedin = "linkedin"
kijiji = "kijiji"
careerjet = "careerjet"

class Source(Enum):
    LINKEDIN = "b"
    CAREER = "r"
    KIJIJI = "y"


def get_data(datalist ,pk):
    for ds in datalist:
        if ds[0] == pk:
            return ds[1]
    return None

def get_all_data():
    cursor = db.cursor()
    cursor.execute("SELECT id, source, time, data FROM myDashboard_data_dump order by time desc")
    res = cursor.fetchall()
    return res

def map_source(link):
    if linkedin in link:
        return Source.LINKEDIN.value
    elif careerjet in link:
        return Source.CAREER.value
    elif kijiji in link:
        return Source.KIJIJI.value
    else:
        return 0


def enumerate_link(link):
    if not link in links:
        links.append(link)


def load_data_dump():
    res = defaultdict(list)
    cursor = db.cursor()
    cursor.execute("SELECT id, source, time from myDashboard_data_dump")
    dump = cursor.fetchall()

    for ds in dump:
        enumerate_link(ds[1])

    count = 0
    for ds in dump:
        link = ds[1]
        source = map_source(link)
        res["pk"].append( ds[0] )
        res["link"].append( links.index(link) )
        res["timesaved"].append( ds[2] )
        res["source"].append( map_source(link) )
        res["label"].append( Source(map_source(link)).name )
        count += 1
    print(str(count) + " lines loaded \n")
    return res

print( "connecting to server...\n")
db = pymysql.connect("colarietitosti.info" ,"cola", psw() ,"dashDB" )
print("connected!\n")
links = []

print("downloading data...")
start = datetime.now()
data = get_all_data()
# dd = load_data_dump()
end = datetime.now()
print("data loaded in ", end="")
print(end -start)

print( "\ndisconnecting from server.. ")
db.close()

import nltk
import re
from bs4 import BeautifulSoup
import mechanicalsoup


stopwords_ita = ["é", "io", "noi", "voi", "il", "lo", "la", "i", "gli", "le", "di",
                 "in", "e", "and", "a", "per", "\\xc2\\xa0", "the", "del", "con", "della", "of", "to", "al", "o",
                 "ad", "ai", "-", "dei", "un", "delle", "si", "lavoro", "una", "che", "sensi", "with",
                 "ricerca", "ed", "nella", "alla", "la", "di", "si", "su", "is", "a", "nel", "sul", "da", "(bo)",
                 "e/o", "lingua", "for", "lavoro", "tempo", "\\xc3\\xa8", "buona", "azienda", "conoscenza",
                 "esperienza", "settore","team"]
known_sources = []
emails = {}
brow = mechanicalsoup.StatefulBrowser()
ret = ""
for j in data:
    source = j[1]
    time = j[2]
    data = j[3]

    if source in known_sources:
        continue
    else:
        known_sources.append(source)

    datasoup = BeautifulSoup(data, "html.parser")
    if "career" in source:
        description = datasoup.find("div", class_="advertise_compact").text
    elif "linkedin" in source:
        description = datasoup.find("div", class_="description__text").text
    else:
        description = ""

    ret += description

print("preparing ...")
tokens = [t.lower() for t in ret.split()]
clean_tokens = tokens[:]
for token in tokens:
    if token in stopwords_ita:
        clean_tokens.remove(token)

freq = nltk.FreqDist(clean_tokens)
for key,val in freq.items():
    print(str(key) + ':' + str(val))

print("plotting ...")
freq.plot(20, cumulative=False)
