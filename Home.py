import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

APP_TITLE = "Agriculture Stress Index"
APP_SUB_TITLE = "ASI DEKADAL"

def display_metric_facts(df,year, month, dekade, landcover, season, country_name, avg_data, metric_title, isMedian=False):
    df=df[(df['Year']==year) & (df['Month']==month) & (df['Dekad']==dekade) &(df['Land_Type']==landcover) & (df['Season']==season)]
    if country_name:
        df=df[df['ISO3']==country_name]
    if isMedian:
        calc = df[avg_data].mean()
        #calc = df[avg_data].sum() / len(df) if len(df) else 0

    else:
        calc = df[avg_data].sum()
    #average_asid = df[avg_data].mean()
    st.metric(metric_title, '{:,}'.format(calc))

def display_map(df, year, month, dekade, landcover, season):
    df=df[(df['Year']==year) & (df['Month']==month) & (df['Dekad']==dekade) &(df['Land_Type']==landcover) & (df['Season']==season)]
    
    map = folium.Map(location=[38,-96.5], zoom_start=4,scrollWheelZoom=False, tiles="CartoDB positron")
    # Code to open a .geojson file and store its contents in a variable
    with open ('https://raw.githubusercontent.com/rcgeos/streamlit-asidemo/main/data/countries.geojson', 'r') as jsonFile:
        geo_data = json.load(jsonFile)
    
    folium.Choropleth(
        geo_data=geo_data,
        name="choropleth",
        data=df,
        columns=['ISO3','Data'],
        key_on='features.properties.name',
        line_opacity=0.7
    ).add_to(map)
    folium.LayerControl().add_to(map)
    #choropleth.geojson.add_to(map)

    st_map = st_folium(map, width=700, height=450)
    
    st.write(df.shape)
    st.write(df.head())
    st.write(df.columns)

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

 
    #st.write(df.shape)
    #st.write(df)
    #st.write(df.columns)

    # Display Filters and map 
    display_map(df, year, month, dekade, landcover,season)

    # Display metrics 
    st.subheader(f'{country_name} {frequency} ASI')
    col1, col2 = st.columns(2)
    with col1:
        display_metric_facts(df, year, month, dekade, landcover, season, country_name, avg_data,metric_title)
    with col2:
        display_metric_facts(df, year, month, dekade, landcover, season, country_name, avg_data,metric_title, isMedian=True)


if __name__ == "__main__":
    main()