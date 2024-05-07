from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import pandas as pd
from python_EDA import search_fred
import matplotlib.pyplot as plt

ChromeDriverManager().install()
browser = webdriver.Chrome()

def create_browser():
    ChromeDriverManager().install()
    browser = webdriver.Chrome()
    return browser
'''
1. 연준 url에 접속
2. country를 검색해서 title, url, series_id crawling
3. dataframe 으로 return
'''
def search_country(country):
    result = []
    url = "https://fred.stlouisfed.org/"
    browser.get(url)
    browser.find_element(By.CLASS_NAME, "search-input-homepage").click()
    time.sleep(1)
    browser.find_element(By.CLASS_NAME, "search-input-homepage").send_keys(country)
    time.sleep(1)
    browser.find_element(By.CLASS_NAME, "homepage-search-button").click()
    time.sleep(1)
    country_list = browser.find_elements(By.CLASS_NAME, "search-list-item")
    time.sleep(1)
    for country in country_list:
        title = country.find_element(By.CLASS_NAME, "search-series-title").text
        url = country.find_element(By.CLASS_NAME, "search-series-title-gtm").get_attribute("href")
        series_id = url.split("/")[-1]
        result.append({'title':title,'series_id':series_id,'url':url})
        result_df = pd.DataFrame(result)
    return result_df



# 지표 데이터 가져온 후 plot 그리기
# japan_df = search_country("japan")
# N = len(japan_df)
# for i in range(0,5):
#     series_id = japan_df.loc[i]['series_id']
#     title = japan_df.loc[i]['title']
#     plot_data = search_fred(series_id)
#     time.sleep(1)
#     plt.figure()
#     plot_data.plot()
#     plt.title(title)



