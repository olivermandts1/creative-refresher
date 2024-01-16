import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

# Display Title and Description
st.title("Data Submission Form")
st.markdown("Enter your data below.")

# Establishing a Google Sheets connection
conn = st.experimental_connection("gsheets", type=GSheetsConnection)

# Define the spreadsheet ID and worksheet name
spreadsheet_id = "1tqm7G0yzckwSCKXdPcGcWNH6y5nMj68rhpMQZlcO2wU"
worksheet_name = "Prompt Chains"

# Fetch existing data
existing_data = conn.read(spreadsheet=spreadsheet_id, worksheet=worksheet_name, usecols=[0], ttl=5)
existing_data = existing_data.dropna(how="all")

# Data Submission Form
with st.form(key="data_form"):
    test_field = st.text_input(label="Test Field")
    submit_button = st.form_submit_button(label="Submit")

    # If the submit button is pressed
    if submit_button:
        # Check if the field is filled
        if not test_field:
            st.warning("Please fill in the test field.")
            st.stop()
        else:
            # Create a new row of data
            new_data = pd.DataFrame([{"Test Field": test_field}])

            # Add the new data to the existing data
            updated_df = pd.concat([existing_data, new_data], ignore_index=True)

            st.success("Data successfully submitted!")
