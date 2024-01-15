import streamlit as st
from streamlit_gsheets import GSheetsConnection

st.subheader("📗 Google Sheets Connection using Public URLs")

url = "https://docs.google.com/spreadsheets/d/1BkD450mJ4MJA7xuMi0MFrb79_bXsS_9HaSLTykKRccE/edit?usp=sharing"

st.write("#### Read Specific Worksheet as Pandas DataFrame")

with st.echo():
    # Create a connection using Streamlit's experimental connection feature
    conn = st.experimental_connection("gsheets", type=GSheetsConnection)

    # Read a specific worksheet from the Google Sheet
    df = conn.read(

    )
    st.dataframe(df)

st.write("#### 2. Query public Google Worksheet using SQL")
st.info(
    "Mutation SQL queries are in-memory only and do not results in the Worksheet update.",
    icon="ℹ️",
)
st.warning(
    """You can query only one Worksheet in provided public Spreadsheet,
        use Worksheet name as target in from SQL queries.
        The worksheet, which you query is defined by GID query parameter or GID parameters to query method.""",
    icon="⚠️",
)


with st.echo():
    import streamlit as st

    from streamlit_gsheets import GSheetsConnection

    conn = st.experimental_connection("gsheets", type=GSheetsConnection)

    df = conn.query('select births from "Example 2" limit 10', spreadsheet=url)
    st.dataframe(df)
