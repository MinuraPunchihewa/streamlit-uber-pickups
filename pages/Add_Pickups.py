from db import SQLiteConnectionManager
import streamlit as st

DB_FILE = 'uber_pickups.db'

st.title('Add Uber Pickup')


def add_data(lat, lon, base):
   with SQLiteConnectionManager(DB_FILE) as connection:
      connection.execute(
         """
         INSERT INTO pickups(lat, lon, base)
         VALUES
         (?, ?, ?)
         """,
         (lat, lon, base)
      )

      connection.commit()


with st.form("add_pickup_form"):
   lat = st.number_input("Latitude")
   lon = st.number_input("Longitude")
   base = st.text_input("Base")

   submitted = st.form_submit_button("Submit")
   if submitted:
      add_data(lat, lon, base)
      data_load_state = st.text('Pickup Added!')