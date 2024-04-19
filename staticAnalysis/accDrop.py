import matplotlib.pyplot as plt
import numpy as np

# Create a figure and axis
fig, ax = plt.subplots()

# Define the time range for the x-axis
time = np.linspace(0, 10, 100)

# Define the performance function before and after the degradation point
performance_before = np.full(shape=len(time)//2, fill_value=0.79)
degradation_point = 5
# Define the performance function with a negative slope after the degradation point
time_after = time[len(time)//2:]
performance_after = 0.79 - (time_after - degradation_point) * 0.2

# Combine the two halves at the degradation point

performance = np.where(time < degradation_point, performance_before, performance_after)

# Plot the performance curve
ax.plot(time, performance, 'k')

# Add a vertical dashed line at the degradation point
ax.axvline(x=degradation_point, color='r', linestyle='--')

# Annotate the degradation point
#ax.annotate('Degradation point', xy=(degradation_point, 0.5), xytext=(degradation_point+1, 0.6),
#            arrowprops=dict(facecolor='black', shrink=0.05))

# Set the labels for the axes
ax.set_xlabel('Time')
ax.set_ylabel('Predictive performance')

# Set the title of the plot
#ax.set_title('Model Performance Over Time')

# Display the plot
plt.show()
