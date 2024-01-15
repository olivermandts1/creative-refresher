import streamlit as st
from streamlit_gsheets import GSheetsConnection

st.subheader("📗 Google Sheets Connection using Public URLs")

url = "https://docs.google.com/spreadsheets/d/141YaOszXibklI2qqRiyGdox3mpyCioFK5eJMtD78iJE/edit#gid=962857946"

st.write("#### 1. Read public Google Worksheet as Pandas")

with st.echo():
    # Create a connection using Streamlit's experimental connection feature
    conn = st.experimental_connection("gsheets", type=GSheetsConnection)

    # Read data from the Google Sheet
    df = conn.read(spreadsheet=url)
    desired_range = df.iloc[99:124, 0:2]  # Rows 100-124 and columns A-B (0-indexed)

    # Hardcoding specific values in column A
    desired_range.iloc[0:5, 0] = 'Headlines'      # Rows 100-104
    desired_range.iloc[6:11, 0] = 'Primary Text'  # Rows 106-110
    desired_range.iloc[12:17, 0] = 'Description'  # Rows 112-116
    desired_range.iloc[19:24, 0] = 'Forcekeys'    # Rows 119-123
    
    # Replace NaN values with an empty string
    desired_range.fillna('', inplace=True)

# Use st.markdown with HTML and CSS to enable text wrapping
st.markdown("""
<style>
.dataframe th, .dataframe td {
    white-space: nowrap;
    text-align: left;
    border: 1px solid black;
    padding: 5px;
}
.dataframe th {
    background-color: #f0f0f0;
}
.dataframe td {
    min-width: 50px;
    max-width: 700px;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: normal;
}
</style>
""", unsafe_allow_html=True)

# Display the DataFrame with text wrapping
st.markdown(desired_range.to_html(escape=False, index=False), unsafe_allow_html=True)



with st.echo():
    import streamlit as st

    from streamlit_gsheets import GSheetsConnection

    conn = st.experimental_connection("gsheets", type=GSheetsConnection)

    df = conn.query('select births from "Example 2" limit 10', spreadsheet=url)
    st.dataframe(df)
