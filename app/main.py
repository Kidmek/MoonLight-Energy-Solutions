
import sys
import os
import streamlit as st

# Add the root directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scripts import analysis,visualization,data_loading,data_cleaning

# Title of the Streamlit app
st.title("EDA Dashboard")

# Sidebar for loading data
data_load_state = st.text('Loading data...')
data = data_loading.load_data('data/*.csv')
data_load_state.text('Data loaded successfully!')

# Show the raw data
if st.checkbox('Show raw data'):
    chunk_size = 100
    num_chunks = len(data) // chunk_size + 1

    chunk = st.selectbox('Select data chunk:', range(1,num_chunks))

    start_row = (chunk-1) * chunk_size
    end_row = start_row + chunk_size
    st.write(data.iloc[start_row:end_row])

# Summary Statistics
st.header("Summary Statistics")
if st.button('Generate Summary Statistics'):
    summary_stats = analysis.summary_statistics(data)
    st.write(summary_stats)

# Data Quality Check
st.header("Data Quality Check")
if st.button('Perform Data Quality Check'):
    quality_check = analysis.data_quality_check(data)
    st.write(quality_check)

# Z-Score Analysis
st.header("Z-Score Analysis")
if st.button('Perform Z-Score Analysis'):
    outliers = analysis.z_score_analysis(data)
    st.write(outliers)

# Time Series Analysis
st.header("Time Series Analysis")
selected_columns = st.multiselect('Select columns for time series analysis', data.columns.tolist(), default=['GHI', 'DNI', 'DHI', 'Tamb'])
if st.button('Plot Time Series'):
    visualization.plot_time_series(data, selected_columns,st=True)

# Correlation Analysis
st.header("Correlation Analysis")
if st.button('Perform Correlation Analysis'):
    visualization.correlation_analysis(data,st=True)

# Wind Analysis
st.header("Wind Analysis")
if st.button('Perform Wind Analysis'):
    visualization.wind_analysis(data,st=True)

# Temperature Analysis
st.header("Temperature Analysis")
if st.button('Perform Temperature Analysis'):
    visualization.temp_analysis(data,st=True)

# Histograms
st.header("Histograms")
if st.button('Plot Histograms'):
    visualization.histogram(data,st=True)

# Bubble Chart
st.header("Bubble Chart")
x_var = st.selectbox('Select X variable', data.columns.tolist(), index=data.columns.tolist().index('GHI'))
y_var = st.selectbox('Select Y variable', data.columns.tolist(), index=data.columns.tolist().index('Tamb'))
size_var = st.selectbox('Select size variable', data.columns.tolist(), index=data.columns.tolist().index('RH'))
color_var = st.selectbox('Select color variable (optional)', ['None'] + data.columns.tolist(), index=0)
if st.button('Create Bubble Chart'):
    visualization.bubble_chart(data, x_var, y_var, size_var, color_var if color_var != 'None' else None,st=True)

# Footer
