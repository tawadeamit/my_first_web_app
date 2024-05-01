import streamlit as st
#import plotly.express as px



# import modules 
from datetime import datetime 
import yfinance as yf 
import matplotlib.pyplot as plt 
import pandas as pd

import XlsxWriter

# initialize parameters 
start_date = datetime(2007, 1, 1) 
end_date = datetime(2024, 4, 26) 
  
# get the data 
# SPY
# ^NSEI = NIFTY 50
''' Nifty Index='^NSEI,  
'''
stock='^NSEI'

data = yf.download(stock, start = start_date, 
                   end = end_date) 

data.head(5)

# display 
plt.figure(figsize = (20,10)) 
plt.title('Opening Prices from {} to {}'.format(start_date, 
                                                end_date)) 
plt.plot(data['Close']) 
plt.show()


df = pd.DataFrame(data)
# Long term - no filter
# Short term - apply date filter
# df = df.loc[df.index > '2024-1-1']

df['SMA09'] = data['Close'].rolling(9).mean()
df['SMA20'] = data['Close'].rolling(20).mean()
df['SMA50'] = data['Close'].rolling(50).mean()
df['SMA200'] = data['Close'].rolling(200).mean()


# Generate signals based on moving average crossover
df['Signal'] = 0  # 0 indicates no signal
df.loc[df['SMA50'] > df['SMA200'], 'Signal'] = 1  # 1 indicates buy signal
df.loc[df['SMA50'] < df['SMA200'], 'Signal'] = -1  # -1 indicates sell signal

df['Prev_Close'] = df['Close'].shift()
df['Close_Singnal'] = df['Close'] - df['Prev_Close']


print(df)

st.set_page_config(page_title="My First Web App", page_icon=":tada:", layout="wide") 

#display dataframe
st.subheader("wlcm")
st.write("streamlit is best")

#display dataframe
st.subheader("Nifty50")
st.dataframe(df)


