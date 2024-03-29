import numpy as np
import matplotlib.pyplot as plt

# uniform distribution
values = np.random.uniform(-10.0, 10.0, 100000)
plt.hist(values, 50)
plt.show()

from scipy.stats import norm
# probability density function, normal, gaussian
x = np.arange(-3, 3, 0.001)
plt.plot(x, norm.pdf(x))

# Generate some random numbers with a normal distribution.
# "mu" is the desired mean
# "sigma" is the standard deviation
mu = 5.0
sigma = 2.0
values = np.random.normal(mu, sigma, 10000)
plt.hist(values, 50)
plt.show()

# Exponential PDF
from scipy.stats import expon
x = np.arange(0, 10, 0.001)
plt.plot(x, expon.pdf(x))

# Binomial Probability Mass Function
from scipy.stats import binom
n, p = 10, 0.5
x = np.arange(0, 10, 0.001)
plt.plot(x, binom.pmf(x, n, p))

# Poisson PMF
from scipy.stats import poisson
mu = 500
x = np.arange(400, 600, 0.5)
plt.plot(x, poisson.pmf(x, mu))