from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
import webbrowser

TICKER = "RIO.L"
URL = "https://gpwcatalyst.pl/notowania-obligacji-obligacje-skarbowe"
price = {}

driver = webdriver.Chrome(service=Service("C:\Development\chromedriver.exe"))
driver.get(URL)

driver.find_element(By.CLASS_NAME, 'col10')

name = driver.find_elements(By.CSS_SELECTOR, "a[href*='o-instrumentach-instrument']")
segment = driver.find_elements(By.CLASS_NAME, 'col2')
last_close = driver.find_elements(By.CLASS_NAME, 'col4')
current_price = driver.find_elements(By.CLASS_NAME, 'col10')
bid_price = driver.find_elements(By.CLASS_NAME, 'col12')
offer_price = driver.find_elements(By.CLASS_NAME, 'col13')
b = 0
bond_quotes = {}


segment_length = len(segment)
for a in range(0, segment_length):
    if segment[a].text == "GPW ASO" or segment[a].text == "GPW RR":
        bond_quotes[name[b+1].text] = {"current_price": current_price[a].text, "segment": segment[a].text, "last_close":last_close[a].text}
        b += 1

bond_tickers = []
for a in name:
    bond_tickers.append(a.text)
