import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import datetime

st.title("RFM Segmentation Report", anchor="rfm-segmentation-report")
st.header("RFM Segmentation Report")
st.subheader("RFM Segmentation Report")
st.caption("RFM Segmentation Report")
#st.text("RFM Segmentation is method of customer segmentation that uses three key factors: recency, frequency, and monetary value. Recency is the number of days since the last purchase. Frequency is the number of purchases in a given time period. Monetary value is the total amount of money spent in a given time period.")
st.markdown("RFM Segmentation is method of customer segmentation that uses three key factors: recency, frequency, and monetary value. Recency is the number of days since the last purchase. Frequency is the number of purchases in a given time period. Monetary value is the total amount of money spent in a given time period.")
# Create bullet points
st.markdown(" * R is the number of days since the last purchase.")
st.markdown(" * F is the number of purchases in a given time period.")
st.markdown(" * M is the total amount of money spent in a given time period.")


# Upload file
uploaded_file = st.file_uploader("Please Import Your Transaction Data", type="csv")
if uploaded_file is None:
    df = pd.read_csv("data/data.csv", encoding='latin-1')
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    df['Total'] = df['Quantity'] * df['UnitPrice']
    df['CustomerID'] = df['CustomerID'].astype(str)
    #c = st.empty()
    #st.write("Here is a sample of your Transaction Dataset")
    #c.dataframe(df.head(50))

else:
    df = pd.read_csv(uploaded_file, encoding='latin-1')
    #c = st.empty()
    #st.write("Here is a sample of your Transaction Dataset")
    #c.dataframe(df.head(50))
    
st.write("Here is a sample of your Transaction Dataset")
c = st.empty()
c.dataframe(df.head(50))

# Create sidebar to select date, transaction id, and customer id
st.sidebar.title("Select Date, Transaction ID, and Customer ID")
st.sidebar.header("Date Range")
df['myd'] = df['InvoiceDate'].dt.strftime('%Y-%m-%d')
min = df['myd'].min().split('-')
max = df['myd'].max().split('-')
min_date = datetime.date(int(min[0]), int(min[1]), int(min[2]))
max_date = datetime.date(int(max[0]), int(max[1]), int(max[2]))
date = st.sidebar.date_input("Pick your date range", (min_date, max_date))

# If min and max in range, then filter data
if date[0] >= min_date and date[1] <= max_date:
    df = df[(df['InvoiceDate'] >= pd.to_datetime(date[0])) & (df['InvoiceDate'] <= pd.to_datetime(date[1]))]
    c.dataframe(df)
else:
    st.write("Date Range is not in range")


# Create sidebar to select date, transaction id, and customer id
#st.sidebar.title("Select Date, Transaction ID, and Customer ID")
#st.sidebar.markdown(" * Select Date")

# Select date range adn filter data base on date
#date = st.sidebar.selectbox("Select Date", df.columns)
#st.write("Analyzing your Transaction Dataset")
#st.dataframe(df)
#transaction_id = st.sidebar.selectbox("Select Transaction ID", df.columns)
#customer_id = st.sidebar.selectbox("Select Customer ID", df.columns)




# Filter data base on date
#df['Date'] = pd.to_datetime(df[date])
