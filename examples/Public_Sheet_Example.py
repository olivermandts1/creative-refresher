import streamlit as st

st.subheader("📗 Google Sheets st.connection using Public URLs")

url = "https://docs.google.com/spreadsheets/d/1BkD450mJ4MJA7xuMi0MFrb79_bXsS_9HaSLTykKRccE/edit?usp=sharing"

st.write("#### 1. Read public Google Worksheet as Pandas")

with st.echo():
    import streamlit as st

    from streamlit_gsheets import GSheetsConnection

    conn = st.experimental_connection("gsheets", type=GSheetsConnection)

    df = conn.read(worksheet="Sheet2", usecols=[0])
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
