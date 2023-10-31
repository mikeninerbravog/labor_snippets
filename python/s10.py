# pip install mplfinance yfinance

# You can see a lot of Stock Name on this URL: https://www.nasdaqtrader.com/dynamic/symdir/nasdaqlisted.txt
# Use only the symbol, eg.: WTER or VECO

import yfinance as yf
import mplfinance as mpf

# Define the stock symbol and data range:
symbol = input("Enter Stock Name: ")
start_date = '2022-01-01'
end_date = '2023-10-30'

# Fetch stock data
stock_data = yf.download(symbol, start=start_date, end=end_date)

# Create the candlestick chart
mpf.plot(stock_data, type='candle', style='yahoo', title=f'{symbol} Candlestick Chart')