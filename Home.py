import streamlit as st
import pandas as pd

APP_TITLE = "Agriculture Stress Index"
APP_SUB_TITLE = "ASI DEKADAL"

def main():
    st.set_page_config(APP_TITLE)
    st.title(APP_TITLE)
    st.caption(APP_SUB_TITLE)

    # ADD Data
    #@st.cache_data
    url_path='https://raw.githubusercontent.com/rcgeos/streamlit-asidemo/main/data/data_sample.csv'
    df=pd.read_csv(url_path, encoding='ISO-8859-1')
    df['Year']=df['Year'].astype(int)
    
    frequency = "Dekadal"
    year = 2022 
    month = 8
    landcover = 'Crop Area'
    season = 'Season 1'
    country_name = 'Guatemala'
    avg_data = 'Data'
    metric_title = f"Average {frequency} ASI"
    df=df[(df['Year']==year) & (df['Month']==month) & (df['Land_Type']==landcover) & (df['Season']==season)]
    if country_name:
        df=df[df['ISO3']==country_name]
    average_asid = df[avg_data].mean()
    st.metric(metric_title, '{:,}'.format(average_asid))
    st.write(df.shape)
    st.write(df)
    st.write(df.columns)

    # Display Filters and map 

    # Display metrics 

if __name__ == "__main__":
    main()