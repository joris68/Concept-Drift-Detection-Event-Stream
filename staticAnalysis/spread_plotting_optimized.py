import pandas as pd
import statistics as s
import matplotlib.pyplot as plt

df = pd.read_csv("ExecutionTimesOptimized/gradualOptimized.csv")

startEvent = "F"
endEvent = "D"

#filter for the F and D line
new_df = df[(df["start"] == startEvent) & (df["end"] == endEvent)]

#print(new_df)

window_size = 5
spread_list = new_df['timeSpread'].to_list()


windows = range(0, 100 ,5)

averages = []
stds = []

for win in windows:
     x = spread_list[win:win+4]
     #print(x)
     avg = s.mean(x)
     std = s.stdev(x)
     averages.append(avg)
     stds.append(std)

print(averages)
print(str(len(averages)))
print(stds)
print(str(len(stds)))

# Example data (assuming 'averages' and 'std' are defined elsewhere)
#x = list(range(1, 21))

# Plotting the data
#plt.figure()
#plt.plot(x, averages, label='Average')  # Plotting averages with a label
#plt.plot(x, stds, label='Standard Deviation')  # Plotting std with a label

# Label the axes and add a title
#plt.xlabel('# of static window')
#plt.ylabel('AVG/STD in MS')
#plt.title("AVG and STD of time spreads between two random directly followed activities")

# Adding a legend
#plt.legend()

# Save the plot
#plt.savefig("OptimizedMetrics/recurringDriftSpreads.png")

# Show the plot
#plt.show()
