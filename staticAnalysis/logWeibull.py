import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import lognorm, weibull_min

# Parameters
mu = 0  # mean for the log-normal
sigma = 1  # standard deviation for the log-normal
lambd = 1  # scale parameter for the Weibull
k = 1.5  # shape parameter for the Weibull

# Generating data for log-normal distribution
#x = np.linspace(0.01, 5, 400)
#log_normal_pdf = lognorm.pdf(x, sigma, scale=np.exp(mu))

# Generating data for Weibull distribution
#weibull_pdf = weibull_min.pdf(x, k, scale=lambd)

# Plotting both distributions
#plt.figure(figsize=(8, 5))
#plt.plot(x, log_normal_pdf, label='Log-Normal Distribution (μ=0, σ=1)', color='purple')
#plt.plot(x, weibull_pdf, label='Weibull Distribution (λ=1, k=1.5)', color='black')
#plt.title('Log-Normal vs Weibull Distribution')
#plt.xlabel('Value')
#plt.ylabel('Probability Density')
#plt.legend()
#plt.grid(True)
#plt.show()



# Generating data for log-normal distribution
x = np.linspace(0.01, 5, 400)
log_normal_cdf = lognorm.cdf(x, sigma, scale=np.exp(mu))

# Generating data for Weibull distribution
weibull_cdf = weibull_min.cdf(x, k, scale=lambd)

# Plotting both distributions
plt.figure(figsize=(8, 5))
plt.plot(x, log_normal_cdf, label='Log-Normal Distribution (μ=0, σ=1)', color='purple')
plt.plot(x, weibull_cdf, label='Weibull Distribution (λ=1, k=1.5)', color='black')
#plt.title('CDF of Log-Normal vs Weibull Distribution')
plt.xlabel('Value')
plt.ylabel('Cumulative Probability')
plt.legend()
plt.grid(False)
plt.show()
