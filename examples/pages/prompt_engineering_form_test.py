import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection

# Function to append data to Google Sheet
def append_data_to_sheet(data, worksheet_name, spreadsheet_url):
    conn = st.experimental_connection("gsheets", type=GSheetsConnection)
    df = pd.DataFrame([data])
    conn.update(spreadsheet=spreadsheet_url, worksheet=worksheet_name, dataframe=df)

# Streamlit form
with st.form("my_form"):
    test_field = st.text_input("Test Field")
    submitted = st.form_submit_button("Submit")

    if submitted:
        spreadsheet_url = "https://docs.google.com/spreadsheets/d/1tqm7G0yzckwSCKXdPcGcWNH6y5nMj68rhpMQZlcO2wU/edit?usp=sharing"
        worksheet_name = "Prompt Chains"
        append_data_to_sheet({"Test Field": test_field}, worksheet_name, spreadsheet_url)
        st.success("Data submitted!")

# Note: Replace "YOUR_SPREADSHEET_URL" with the URL of your Google Sheet.
