
import schedule
import mechanicalsoup
import time

def ping_dash(*args, **kwargs):
    print('pinging dashboard..')
    link = "https://dash.colarietitosti.info"
    browser = mechanicalsoup.StatefulBrowser()
    browser.open(link)
    browser.get_current_page()


schedule.every(10).seconds.do(ping_dash)

while True:
    schedule.run_pending()
    time.sleep(1)
