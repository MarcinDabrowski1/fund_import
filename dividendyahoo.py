from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
import webbrowser

TICKER = "RIO.L"
URL = "https://finance.yahoo.com/quote/" + TICKER + "?p=" + TICKER + "&.tsrc=fin-srch"
payments = {}

driver = webdriver.Chrome(service=Service("C:\Development\chromedriver.exe"))
driver.get(URL)

driver.find_element(By.XPATH, '//*[@id="consent-page"]/div/div/div/form/div[2]/div[2]/button').click()

div_date = driver.find_element(By.XPATH, '//*[@id="quote-summary"]/div[2]/table/tbody/tr[7]/td[2]/span')
div_nominal = driver.find_element(By.XPATH, '//*[@id="quote-summary"]/div[2]/table/tbody/tr[6]/td[2]')

payments[div_date.text] = div_nominal.text.split(" (")[0]

print(payments)

