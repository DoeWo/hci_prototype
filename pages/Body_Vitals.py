import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.header("Body Vitals Analysis")

# Mock data for demonstration
data = pd.DataFrame({
'Heart Rate': np.random.randint(60, 100, 100),
'Blood Pressure': np.random.randint(110, 140, 100),
'Oxygen Saturation': np.random.randint(94, 100, 100)
})

# Sidebar controls for filtering or adjustments
metric_to_view = st.sidebar.selectbox("Select a metric to view", data.columns)

# Display the selected metric
st.write(f"Data for {metric_to_view}:")
st.line_chart(data[metric_to_view])

# Metrics and visuals
st.subheader("Summary Metrics")
st.write(data.describe())