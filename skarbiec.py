from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
import webbrowser

URL = "https://www.skarbiec.pl/notowania/?type=1&cat=-1"
links = []


driver = webdriver.Chrome(service=Service("C:\Development\chromedriver.exe"))
driver.get(URL)
all_links = driver.find_elements(By.CSS_SELECTOR, "a[href*='download-csv']")
for link in all_links:
    links.append(link.get_attribute("href"))

for link in links:
    webbrowser.open(link)



