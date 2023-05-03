import streamlit as st
import pandas as pd

APP_TITLE = "Agriculture Stress Index"
APP_SUB_TITLE = "ASI DEKADAL"

def main():
    st.set_page_config(APP_TITLE)
    st.title(APP_TITLE)
    st.caption(APP_SUB_TITLE)

    # ADD Data
    @st.cache_data
    url_path="https://raw.githubusercontent.com/rcgeos/streamlit-asidemo/main/data/data_sample.csv, encoding='utf-8'"
    df=pd.read_csv(url_path)
    st.write(df)

    # Display Filters and map 

    # Display metrics 

if __name__ == "__main__":
    main()