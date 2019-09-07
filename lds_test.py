

import dryscrape
from bs4 import BeautifulSoup


link = "https://backstage2.pms.ifi.lmu.de:8080/course/21310807-3b0c-4482-bb76-cda34eb0430c/cm/a39a091e-ac66-4537-9685-a03d054be311/stream/f9ede8d7-c01a-48dd-9c5e-f9a424d1cdc6/8950d321-45a4-40ff-abd3-e3e96ef6ba10/4e36c0b2-1528-404f-9790-83d99268ad46"


session = dryscrape.Session()
session.visit(link)
response = session.body()
page = BeautifulSoup(response)


# execute script to scroll down the page
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")


print(page)