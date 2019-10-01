import numpy as np
from numpy import mean, dot
import matplotlib.pyplot as plt

def de_mean(x):
    xmean = mean(x)
    return [xi - xmean for xi in x]

def covariance(x, y):
    n = len(x)
    return dot(de_mean(x), de_mean(y)) / (n-1)
    
# there is not real relationship
pageSpeeds = np.random.normal(3.0, 1.0, 1000)
purchaseAmount = np.random.normal(50.0, 10.0, 1000)

plt.scatter(pageSpeeds, purchaseAmount)
plt.show()
print(covariance(pageSpeeds, purchaseAmount))

# create some real relationship
purchaseAmount = np.random.normal(50.0, 10.0, 1000) / pageSpeeds
plt.scatter(pageSpeeds, purchaseAmount)
plt.show()
print(covariance(pageSpeeds, purchaseAmount))

# normalize covariance with SD
def correlation(x, y):
    stddevx = x.std()
    stddevy = y.std()
    return covariance(x, y) / stddevx / stddevy
    
print(correlation(pageSpeeds, purchaseAmount))

# numpy has build-in correlation func
np.corrcoef(pageSpeeds, purchaseAmount)

# fabricate a perfect correlation
purchaseAmount = 100 - pageSpeeds * 3
plt.scatter(pageSpeeds, purchaseAmount)
plt.show()
print(correlation(pageSpeeds, purchaseAmount))