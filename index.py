from flask import Flask, render_template, url_for, request, jsonify, json
import setStockData as gsd #gsd for get stock data 
app = Flask(__name__)

'''
  * Method to map route to plot-closing-prices url
  * 
'''
@app.route('/plot-closing-prices')
def plot_closing_prices():
    stock_name = request.args.get("stock")
    start_date = request.args.get("start-date")
    end_date = request.args.get("end-date")
    
    if not stock_name or not start_date or not end_date:
        return "<h2>Please enter a valid stock name, start date and end date (format: YYYY-MM-DD)</h2>"
    data = gsd.getClosingPrices(stock_name, start_date, end_date)
    if data == "Sorry there was an error, please enter a valid ticker symbol":
        return data
    title = f"Chart of closing prices for {stock_name}"
    chart_label = f"Chart of {stock_name}"
    chartOf = title
    return render_template("charts.html", data=data, title=title,chart_label=chart_label)
