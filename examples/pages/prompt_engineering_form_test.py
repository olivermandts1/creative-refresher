import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

# Display Title and Description
st.title("Data Submission Form")
st.markdown("Enter your data below.")

# Establishing a Google Sheets connection
conn = st.experimental_connection("gsheets", type=GSheetsConnection)

# Fetch existing data
worksheet_name = "https://docs.google.com/spreadsheets/d/1tqm7G0yzckwSCKXdPcGcWNH6y5nMj68rhpMQZlcO2wU/edit#gid=0"
existing_data = conn.read(spreadsheet=worksheet_name, usecols=[0], ttl=5)
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
            new_data = pd.DataFrame(
                [
                    {
                        "Test Field": test_field
                    }
                ]
            )

            # Add the new data to the existing data
            updated_df = pd.concat([existing_data, new_data], ignore_index=True)

            # Update Google Sheets with the new data
            conn.update(worksheet=worksheet_name, data=updated_df)

            st.success("Data successfully submitted!")
