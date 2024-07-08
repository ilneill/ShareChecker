# #!/usr/bin/python
# Filename: shareTracker.py
# A simple Stock Market share price checker using Yahoo! Finance.
# 
# (c) Ian Neill 2024
# With thanks to all the Internet inspiration!
# 
# https://github.com/ranaroussi/yfinance
# https://www.makeuseof.com/stock-price-data-using-python/
# https://erikjohnsonlibrary.com/2023/12/29/navigating-financial-markets-with-python-building-a-stock-price-tracker/

import yfinance as yf
import pprint   as pp

def main():
    print("\nStock Market Data CLI Query Tool")
    print("================================\n")

    # "Nvidia" = NVDA "National Grid" = NG.L "Deutsche Bank" = DB ~ there are many more!
    stock_symbol = input("Enter the Stock Market symbol: ")

    # Get the Market details from Yahoo! Finance.
    tickerInfo = yf.Ticker(stock_symbol).info
    #pp.pprint(tickerInfo) # Pretty print all of the information that we have!
    # Period can be one of ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max']
    tickerHistory = yf.Ticker(stock_symbol).history(period="5d")
     
    # Show some of the Stock Market Data.
    try:
        print("\nStock Market Details for %s (%s)\n" % (tickerInfo['shortName'], tickerInfo['symbol']))
    except:
        print("Problem getting the Market data from Yahoo!")
        print("  ...Try again later...")
        quit()
    
    print("History - Last 5 Market Days...")
    pp.pprint(tickerHistory)
    print()
    print("Current Market Price    : %08.3f (%s)" % (tickerInfo['currentPrice'], tickerInfo['financialCurrency']))
    print(" ->Market Open Price    : %08.3f (%s)" % (tickerInfo['regularMarketOpen'], tickerInfo['financialCurrency']))
    print(" ->Previous Close Price : %08.3f (%s)" % (tickerInfo['regularMarketPreviousClose'], tickerInfo['financialCurrency']))
    print("Today Lowest Price      : %08.3f (%s)" % (tickerInfo['regularMarketDayLow'], tickerInfo['financialCurrency']))
    print("Today Highest Price     : %08.3f (%s)" % (tickerInfo['regularMarketDayHigh'], tickerInfo['financialCurrency']))
    print("50 Day Average Price    : %08.3f (%s)" % (tickerInfo['fiftyDayAverage'], tickerInfo['financialCurrency']))
    print("200 Day Average Price   : %08.3f (%s)" % (tickerInfo['twoHundredDayAverage'], tickerInfo['financialCurrency']))
    print("1 Year Lowest Price     : %08.3f (%s)" % (tickerInfo['fiftyTwoWeekLow'], tickerInfo['financialCurrency']))
    print("1 Year Highest Price    : %08.3f (%s)" % (tickerInfo['fiftyTwoWeekHigh'], tickerInfo['financialCurrency']))
    print()
    print("Market Recommendataion  :   ** %s **" % (tickerInfo['recommendationKey'].upper()))
    print()

if __name__ == "__main__":
   main()

# EOF