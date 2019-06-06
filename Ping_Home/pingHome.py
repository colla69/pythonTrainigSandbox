
import schedule
import mechanicalsoup
import time

def ping_dash(*args, **kwargs):
    print('pinging dashboard..')
    link = "https://dash.colarietitosti.info/ip/"
    browser = mechanicalsoup.StatefulBrowser()
    browser.open(link)
    browser.get_current_page()


schedule.every(60).seconds.do(ping_dash)

while True:
    schedule.run_pending()
    time.sleep(1)
