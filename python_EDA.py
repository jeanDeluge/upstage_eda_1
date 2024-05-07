# 한국은행 data 불러오기
# stat_code : 한국은행 API 에서 가져와야됨 -> 자동화 필요

import os
import requests
import json
import pandas as pd

"""
한국은행 정보를 dataframe으로 불러오기
start_year : 시작 년도  
end_year : 끝 년도
stat_code : 통계표 코드
item_code1 : 항목 코드1 # 필수아님
item_code2 : 항목 코드2 # 필수아님
item_code3 : 항목 코드3 # 필수아님
item_code4 : 항목 코드4 # 필수아님
"""


def search_kob(
    start_year,
    end_year,
    stat_code,
    item_code1="",
    item_code2="",
    item_code3="",
    item_code4="",
):
    API_KEY = os.getenv("HJH_BOK_OPENAPI_KEY")
    url = f"https://ecos.bok.or.kr/api/StatisticSearch/{API_KEY}/json/kr/1/10000/{stat_code}/A/{start_year}/{end_year}/{item_code1}/{item_code2}/{item_code3}/{item_code4}"
    response = requests.get(url)
    try:
        content = response.text
        data_dict = json.loads(content)
        data_df = pd.DataFrame(data_dict["StatisticSearch"]["row"])
        return data_df
    except Exception as e:
        print("코드를 확인해주세요")
        return None


# FRED data 불러오기
import pandas as pd
from dotenv import load_dotenv
import os
from fredapi import Fred

"""
연준 데이터(연도별 지표)를 dataframe으로 불러오기
series_id 만 필요
"""


def search_fred(series_id):
    load_dotenv()
    API_KEY = os.getenv("HJH_FRED_OPENAPI_KEY")
    fred = Fred(api_key=API_KEY)
    series_data = fred.get_series(series_id)
    dataframe_data = pd.DataFrame(series_data)
    try:
        dataframe_data = dataframe_data.loc["1998-01-01":]
    except:
        dataframe_data = dataframe_data
    return dataframe_data
