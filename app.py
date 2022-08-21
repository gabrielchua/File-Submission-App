import streamlit as st
import pandas as pd
import numpy as np
import time

st.set_page_config(page_title="Test")

st.info('Hello - this is a prototype')

st.title("Please submit your report here.")

st.selectbox("Step 1: Pick the programme", ["Programme 1", "Programme 2"])

uploaded_file = st.file_uploader("Step 2: Upload the report.")

if uploaded_file is not None:
	
	with st.spinner('Checking File'):

		df = pd.read_excel(uploaded_file)
		num_rows, num_columns = df.shape
		columns_received = list(df.columns)
		columns_expected = ["ID", "Date_Of_Visit", "Claim"]
		dup_rows = df.duplicated(keep=False)
		dup_rows_index = np.array(df.index[dup_rows]) + 1
		time.sleep(1)

	# check columns
	if not np.array_equal(columns_received, columns_expected):
		st.error('Do not modify the name and sequence of the columns of the template, and do not add new columns.  \n  \n Expected: {}   \n Received: {}'.format(columns_expected, columns_received), icon = "🚨")

	# check for empty datasets
	elif num_rows == 0:
		st.error('No entries detected.', icon="🚨")

	# validate ID column
	elif not np.array_equal(df['ID'], df['ID'].astype(int)):
		st.error('Invalid IDs detected.', icon="🚨")

	# validate DOV column
	elif np.sum(pd.to_datetime(df['Date_Of_Visit'], errors='coerce').isna()):
		st.error('Invalid dates detected.', icon="🚨")

	# validate Claims column
	elif np.sum(df['Claim'].astype(np.float) < 0):
		st.error('Negative claims detected.', icon="🚨")

	# check for duplicates
	elif np.sum(dup_rows):
		st.error('Duplicate entries detected.  \n  \n Please check rows {}'.format(np.array2string(dup_rows_index, separator=', ')), icon="🚨")

	# success
	else: 
		st.success("Thank you for submitting the report!", icon = "✅")
		st.balloons()
