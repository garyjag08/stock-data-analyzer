import pandas as pd
import numpy as np
import yfinance as yf

'''
  * Class to set data from Yahoo Finance
  * Class takes in ticker, start_date, end_date as arguments
  * Method set_stock_data returns a pandas dataframe of stock data
'''
class SetStockData:
  def __init__(self, ticker, start_date, end_date):
    self.ticker = ticker
    self.start_date = start_datae
    self.end_date = end_date
'''
  * Method to retrieve data from Yahoo Finance
  * Ticker = the ticker symbol of the stock of interest
'''
  def set_stock_data(self):
    return yf.download(self.ticker, start=self.start_date, end=self.end_date) # returns the dataframe of stock data

'''
 * Method to get closing prices of a stock
 * This method gets a stock prices from Yahoo Finance and stores them as a dataframe
 * The closing prices are then stored in a list and returned
 * If a symbol is invalid then the invalid message is returned
'''
def getClosingPrices(stock, start, end):
    '''
    ARGS:
      stock symbol
      start date
      end date
      returns a list of closing prices
    '''
    # Start and Ending dates for stock data (format of YYYY-MM-DD)
    start_date = start
    end_date = end
    
    stock_data = SetStockData(stock, start_date, end_date)
    stock_df = stock_data.set_stock_data()
    
    values = []
    for i in range(len(stock_df)):
        values.append(stock_df.iloc[i]["Close"].values[0])
    if len(values) == 0:
        return "Sorry there was an error, please enter a valid ticker symbol" # invalid ticker symbol
    return values
