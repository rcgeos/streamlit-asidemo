import streamlit as st
import pandas as pd

APP_TITLE = "Agriculture Stress Index"
APP_SUB_TITLE = "ASI DEKADAL"

def display_metric_facts(df,year, month, dekade, landcover, season, country_name, isMedian=False):
    df=df[(df['Year']==year) & (df['Month']==month) & (df['Dekad']==dekade) &(df['Land_Type']==landcover) & (df['Season']==season)]
    if country_name:
        df=df[df['ISO3']==country_name]
    if isMedian:
        calc = df[avg_data].sum() / len(df) if len(df) else 0
    else:
        calc = df[avg_data].sum()
    #average_asid = df[avg_data].mean()
    st.metric(metric_title, '{:,}'.format(round(calc)))

def main():
    st.set_page_config(APP_TITLE)
    st.title(APP_TITLE)
    st.caption(APP_SUB_TITLE)
    url_path='https://raw.githubusercontent.com/rcgeos/streamlit-asidemo/main/data/data_sample.csv'
    df=pd.read_csv(url_path, encoding='ISO-8859-1')
    df['Year']=df['Year'].astype(int)
    # ADD Data
    #@st.cache_data
    frequency = "Dekadal"
    year = 2022 
    month = 8
    dekade = 3
    landcover = 'Crop Area'
    season = 'Season 1'
    country_name = 'Guatemala'
    avg_data = 'Data'
    metric_title = f"Average {frequency} ASI"

    col1, col2 = st.columns(2)
    with col1:
        display_metric_facts(df, year, month, dekade, landcover, season, country_name,isMedian=False)
    with col2:
        display_metric_facts(df, year, month, dekade, landcover, season, country_name,isMedian=True)

    #st.write(df.shape)
    #st.write(df)
    #st.write(df.columns)

    # Display Filters and map 

    # Display metrics 

if __name__ == "__main__":
    main()