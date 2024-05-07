from python_EDA import search_fred
from crawling import search_country
import time
import streamlit as st

key_word = input("원하는 나라를 입력하세요 : ")
country_df = search_country(key_word)
N = len(country_df)

st.dataframe(country_df,
    column_config={
        "title": "Indicator Name",
        "series_id": st.column_config.NumberColumn("Series ID"),
        "url": st.column_config.LinkColumn("FRED url")},
    hide_index=True
    )

for i in range(0,N):
    series_id = country_df.loc[i]['series_id']
    title = country_df.loc[i]['title']
    st.write(title)
    st.line_chart(search_fred(series_id))


    