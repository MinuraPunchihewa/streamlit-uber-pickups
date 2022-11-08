from db import SQLiteConnectionManager
import streamlit as st
import pandas as pd

DB_FILE = 'C:/Users/minurap/PycharmProjects/streamlit-uber-pickups/uber_pickups.db'

st.title('Uber Pickups in NYC')


@st.cache
def load_data():
    with SQLiteConnectionManager(DB_FILE) as connection:
        return pd.read_sql(
            "SELECT * FROM pickups",
            connection,
            index_col=""
        )


# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data()
# Notify the reader that the data was successfully loaded.
data_load_state.text('Loading data...done!')

st.subheader('Raw data')
st.dataframe(data)