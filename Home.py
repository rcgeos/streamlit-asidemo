import streamlit as st
import pandas as pd

APP_TITLE = "Agriculture Stress Index"
APP_SUB_TITLE = "ASI DEKADAL"

def main():
    st.set_page_config(APP_TITLE)
    st.title(APP_TITLE)
    st.caption(APP_SUB_TITLE)

    # ADD Data
    df=pd.read_csv("data/ASI_Dekad_Season1_Country_data.csv")
    st.write(df.shape)

    # Display Filters and map 

    # Display metrics 

if __name__ == "__name__":
    main()