# app.py
import streamlit as st
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt


conn = sqlite3.connect('database/bank.db')

st.title("💳 Bank Customer Transaction Dashboard")


df = pd.read_sql_query("SELECT * FROM transactions", conn)


customer_id = st.sidebar.selectbox("Select Customer ID", options=sorted(df['Customer_ID'].unique()))
service_type = st.sidebar.multiselect("Filter by Service Type", options=df['Service_Type'].unique(), default=df['Service_Type'].unique())

filtered_df = df[(df['Customer_ID'] == customer_id) & (df['Service_Type'].isin(service_type))]

st.subheader(f"Transactions for Customer ID: {customer_id}")
st.dataframe(filtered_df)


total_tx = filtered_df.shape[0]
total_amount = filtered_df['Amount'].sum()
st.write(f"**Total Transactions:** {total_tx}")
st.write(f"**Total Transaction Amount:** ${total_amount}")

# Service usage
service_count = filtered_df['Service_Type'].value_counts()
st.subheader("Service Usage")
st.bar_chart(service_count)

# Monthly Trends
df['Date'] = pd.to_datetime(df['Date'])
monthly_trends = df.groupby(df['Date'].dt.to_period('M'))['Transaction_ID'].count()
st.subheader("Monthly Transaction Trends (All Customers)")
st.line_chart(monthly_trends)
