
import mechanicalsoup
from os.path import expanduser, isfile
from json import dump,load
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler, BlockingScheduler

data_path = expanduser("~/kijiji.json")
scheduler = BlockingScheduler()
# scheduler = BackgroundScheduler()
job = None


def json_save(data, fname):
    with open(fname, 'w') as fp:
        dump(data, fp)


def json_load(fname):
    with open(fname, 'r') as fp:
        return load(fp)


def init_data():
    try:
        res = json_load(data_path)
    except FileNotFoundError:
        res = {}
    return res


def sorttime(data_entry):
    return data_entry["time"]


def textify_entry(entry, title, link, description, source, *args, **kwargs):
    out = ""
    entry = """
    -----------------------------------------------------------------------------------------------------------------------
    from: {} title : {}  link : {}            
    -----------------------------------------------------------------------------------------------------------------------
    description :
    {}          
                """.format(source, title, link, description)
    return out


def get_kiji(*args, **kwargs):
    print('getting Jobs from kijiji.. ')

    res = init_data()
    link = "https://www.kijiji.it/offerte-di-lavoro/offerta/annunci-bologna/informatica-e-web/"
    browser = mechanicalsoup.StatefulBrowser()
    browser.open(link)
    searchres = browser.get_current_page().find("ul", id="search-result")
    for li in searchres.find_all("li"):
        loc = li.find("p", class_="locale")
        if loc is None:
            continue
        title = li.find("a", class_="cta").text.strip()
        link = li.find("a", class_="cta")["href"]
        description = li.find("p", class_="description").text
        data_entry = {"title": title,
                      "link": link,
                      "description": description,
                      "source": "kijiji",
                      "location": loc.text.lower(),
                      "time": datetime.now().strftime("%d/%m/%Y, %H:%M:%S")}
        if link not in res.keys():
            res[link] = data_entry
    json_save(res, data_path)
    print("done\n")


def get_sorted_output(*args, **kwargs):
    res = init_data()
    output_list = []
    for k in res:
        output_list.append(res[k])
    output_list.sort(key=sorttime)
    return output_list


def start_job():
    global job
    #job = scheduler.add_job(get_kiji, 'interval', seconds=3600)
    job = scheduler.add_job(get_kiji, 'interval', seconds=10)
    get_kiji()
    try:
        scheduler.start()
    except:
        pass


start_job()
