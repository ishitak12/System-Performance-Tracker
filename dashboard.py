
import streamlit as st
import pandas as pd
from database import fetch_all_metrics, fetch_metrics_between

st.set_page_config(page_title="System Health Monitor", layout="wide")
st.title("🖥️ System Health Monitor Dashboard")

# Load data
data = fetch_all_metrics()
df = pd.DataFrame(data, columns=['Timestamp', 'CPU', 'Memory', 'Disk', 'Network'])
df['Timestamp'] = pd.to_datetime(df['Timestamp'])

# Sidebar filters
st.sidebar.header("🔍 Filters")
start_date = st.sidebar.date_input("Start Date", df['Timestamp'].min().date())
end_date = st.sidebar.date_input("End Date", df['Timestamp'].max().date())
metric = st.sidebar.selectbox("Select Metric", ['CPU', 'Memory', 'Disk', 'Network'])

# Filter data
mask = (df['Timestamp'].dt.date >= start_date) & (df['Timestamp'].dt.date <= end_date)
filtered_df = df.loc[mask]

# Display summary
st.subheader("📊 Summary Statistics")
st.dataframe(filtered_df.describe())

# Interactive line chart
st.subheader(f"📈 {metric} Usage Over Time")
st.line_chart(filtered_df.set_index('Timestamp')[[metric]])

# Compare multiple metrics
st.subheader("📊 Compare Metrics")
st.line_chart(filtered_df.set_index('Timestamp')[['CPU', 'Memory', 'Disk']])

# Latest status
st.subheader("⚡ Latest Snapshot")
latest = filtered_df.iloc[-1]
st.metric("CPU (%)", latest['CPU'])
st.metric("Memory (%)", latest['Memory'])
st.metric("Disk (%)", latest['Disk'])
st.metric("Network (MB)", latest['Network'])
