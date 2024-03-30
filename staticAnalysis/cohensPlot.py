import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parameters for the distributions
mean1, mean2 = 0, 2
std1, std2 = 1, 1

# Generating points on the x axis between -3 and 5
x = np.linspace(-3, 5, 1000)

# The normal distribution for both sets of parameters
y1 = norm.pdf(x, mean1, std1)
y2 = norm.pdf(x, mean2, std2)

# Plotting the normal distributions without gridlines and x-axis tick labels
plt.figure(figsize=(8, 6))
plt.fill_between(x, y1, color='lightgrey', alpha=0.5)
plt.fill_between(x, y2, color='lightgrey', alpha=0.5)

# Adding the dashed lines
plt.axvline(mean1, color='purple', linestyle='dashed', linewidth=2)
plt.axvline(mean2, color='purple', linestyle='dashed', linewidth=2)

# Adding the double-headed arrow
plt.annotate('', xy=(mean1, max(y1)/3), xytext=(mean2, max(y2)/3),
             arrowprops=dict(arrowstyle='<->', color='purple', lw=2))

# Label 'd' for the distance between the means, placed above the arrow
plt.text((mean1 + mean2) / 2, max(y1)/3 + 0.05, 'd', ha='center', va='center', color='purple', fontsize=25)

# Remove x-axis and y-axis ticks and labels
plt.xticks([])
plt.yticks([])

# Remove the box around the plot
plt.box(False)

# Show the plot
plt.show()
