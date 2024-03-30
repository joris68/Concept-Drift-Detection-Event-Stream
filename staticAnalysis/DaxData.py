#import yfinance as yf
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as mdates



def get_the_data():
     # Define the ticker symbol for the DAX index
     dax_ticker = '^GDAXI'

     # Calculate the date 3 years ago from today
     three_years_ago = (datetime.now() - timedelta(days=3*365)).strftime('%Y-%m-%d')

     # Today's date
     today = datetime.now().strftime('%Y-%m-%d')

     # Retrieve historical data for the DAX index
     dax_data = yf.download(dax_ticker, start=three_years_ago, end=today)
     # Display the first few rows of the dataframe
     print(dax_data.head())
     # Save the data to a CSV file
     dax_data.to_csv('dax_index_data.csv')


def plot_data():
    # Load the data, setting the 'Date' column as the index and parsing the dates
    dax_data = pd.read_csv('dax_index_data.csv', index_col='Date', parse_dates=True)

    # Plotting the data
    plt.figure(figsize=(14, 7))
    plt.plot(dax_data.index, dax_data['Adj Close'], label='Adjusted Close (€)', color='purple')

    # Setting the date formatter and locator
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=6)) 
    plt.gca().xaxis.set_minor_locator(mdates.MonthLocator()) # Every month

    #plt.title('DAX Index - Adjusted Close Last Three Years')
    #plt.xlabel('Date')
    #plt.ylabel('Adjusted Close Price (€)')
    plt.legend()

    # Improving the date display
    plt.gcf().autofmt_xdate()  # Rotation
    plt.xlim([pd.Timestamp('2021-03-22'), pd.Timestamp('2024-03-18')])  # Set x-axis range

    plt.show()

plot_data()




