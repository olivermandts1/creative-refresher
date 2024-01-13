import streamlit as st   
import pandas as pd
import numpy as np
   
   
# Editable DataFrame Section using st.data_editor
st.subheader("📥 Clipboard")
st.caption("This is a demo of the `st.data_editor`.")

# Create an empty grid
empty_grid = pd.DataFrame(np.zeros((20, 4))).replace(0, "").astype(str)

# Use st.data_editor for an editable DataFrame
df = st.data_editor(empty_grid, use_container_width=True, height=600)
