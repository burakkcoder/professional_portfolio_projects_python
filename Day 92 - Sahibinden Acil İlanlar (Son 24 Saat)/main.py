from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import pandas as pd

pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 20000)

data_dict = {
    "İlan Numarası": [],
    "Başlık": [],
    "Fiyat": []
}

url = "https://www.sahibinden.com/acil-acil?date=1day&category=3517"
pages = 20
next_urls = f"https://www.sahibinden.com/acil-acil?date=1day&pagingOffset={pages}&category=3517"

chrome_driver_path = Service("C:\chromedriver.exe")

driver = webdriver.Chrome(service=chrome_driver_path)

driver.get(url)

total_page = driver.find_element_by_xpath("//*[@id='searchResultsSearchForm']/div/div[3]/div[4]/p").text.split(" ")[1]
total_page = int(total_page)

for i in range(total_page):
    ilan_numaralari = driver.find_elements_by_css_selector(".searchResultsClassifiedId")
    ilan_basliklari = driver.find_elements_by_css_selector(".classifiedTitle")
    ilan_fiyati = driver.find_elements_by_css_selector(".searchResultsPriceValue")

    for x in ilan_numaralari:
        data_dict["İlan Numarası"].append(x.text)
    for x in ilan_basliklari:
        data_dict["Başlık"].append(x.text)
    for x in ilan_fiyati:
        data_dict["Fiyat"].append(x.text)
    time.sleep(5)
    total_page -= 1
    driver.get(next_urls)

df = pd.DataFrame(data_dict)
df.to_csv("vasita_acil_ilanlar.csv", encoding="utf-8")

print(df)

driver.close()