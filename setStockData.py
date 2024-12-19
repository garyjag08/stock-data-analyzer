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
    stock_df = yf.download(self.ticker, start=self.start_date, end=self.end_date)
    df_reset = stock_df.reset_index(drop=True)
     return df_reset

 def getMinuteData(self, pre_post):
  data = yf.download(self.ticker, 
    period='1d',        # Period of data (can be '1d', '5d', '1mo', '1y', etc.)
    interval='1m',      # Interval set to 1 minute
    prepost=pre_post) 
  df_reset = data.reset_index(drop=True)
  last_index = df_reset.index[-1]
  return df_reset.iloc[last_index]["Close"]
