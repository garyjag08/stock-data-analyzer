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
