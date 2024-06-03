import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates  # Import for handling date formatting

file_path = 'ExperimentsDocker/cases_itree_monthly.csv'
df = pd.read_csv(file_path)

# Convert "Time Period" to datetime by extracting just the start date
df['Start Date'] = pd.to_datetime(df['Time Period'].str.split(' to ').str[0])

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(df['Start Date'], df['Daily Average No. of Cases in Progress'], marker='o', linestyle='-', color='purple')
#plt.title('Daily Average Number of Case Arrivals Over Time')
#plt.xlabel('Time Period')
plt.ylabel('Daily Average Number of Cases')

# Set x-axis major locator to only show ticks at the beginning of each year
plt.gca().xaxis.set_major_locator(mdates.YearLocator())
# Set x-axis major formatter to only show the year
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y'))

plt.xticks(rotation=45)
#plt.grid(True)
plt.tight_layout()
plt.show()
