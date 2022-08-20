import streamlit as st
import pandas as pd
import numpy as np
import time

st.set_page_config(page_title="Test")

st.info('Hello - this is a prototype')

st.title("Please submit your report here.")


uploaded_file = st.file_uploader("Upload the workload report using the provided template.")

if uploaded_file is not None:
	
	with st.spinner('Checking File'):
		df = pd.read_excel(uploaded_file)
		columns_received = list(df.columns)
		columns_expected = ["ID", "Date_Of_Visit", "Claim"]
		duplicate_rows = df.duplicated(keep=False)
		time.sleep(1)
  
	if not np.array_equal(columns_received, columns_expected, equal_nan=False):
		st.error('Do not modify the headers of the template.  \n Received: {}   \n Expected: {}'.format(columns_received, columns_expected), icon = "🚨")

	elif np.sum(duplicate_rows):
		st.error('Duplicate entries detected.  \n Please check rows {}'.format(list(df.index[duplicate_rows].values)), icon="🚨")

	else: 
		st.success("Thank you for submitting the report!", icon = "✅")
		st.balloons()
