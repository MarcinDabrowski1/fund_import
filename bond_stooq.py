from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import webbrowser

URL = "https://gpwcatalyst.pl/notowania-obligacji-obligacje-skarbowe"
price = {}

driver = webdriver.Chrome(service=Service("C:\Development\chromedriver.exe"))
driver.get(URL)

name = driver.find_elements(By.CSS_SELECTOR, "a[href*='o-instrumentach-instrument']")

LINKS = []
for a in name[1:]:
    LINKS.append("https://stooq.pl/q/d/l/?s="+a.text.lower() + ".pl"+"&i=d")

driver.close()

for link in LINKS:
    try:
        webbrowser.open(link)
    except:
        pass



# for symbol in TICKER[1:]:
#     driver = webdriver.Chrome(service=Service("C:\Development\chromedriver.exe"))
#     URL = "https://stooq.pl/q/d/?s=" + symbol
#     try:
#         driver.get(URL)
#         driver.refresh()
#         time.sleep(5)
#         driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/div[2]/div[2]/button[1]/p").click()
#         time.sleep(5)
#         link = driver.find_element(By.CSS_SELECTOR, "a[href*='q/d/l/?s=']").get_attribute("href")
#         webbrowser.open(link)
#         print(link)
#     except:
#         pass
#
#     driver.close()