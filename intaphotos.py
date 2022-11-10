from bs4 import BeautifulSoup as soup
import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service("C:\chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get("https://www.instagram.com/mblogger123456789/")

sp = soup(driver.page_source, "html.parser")
img=sp.find("img", class_="FFVAD")
img_url = img["src"]


r = requests.get(img_url)
with open("instagram"+str(time.time())+".png", "wb") as f:
    f.write(r.content)
print("success")



