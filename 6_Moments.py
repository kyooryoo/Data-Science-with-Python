import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sp

vals = np.random.normal(0, 0.5, 10000)
plt.hist(vals, 50)
plt.show()

# 1st and 2nd moment is the mean and variance
# 3rd moment is the skew while pos to right and neg to left
# 4th moment is the kurtosis with normal at 0
print(
np.mean(vals),
np.var(vals),
sp.skew(vals),
sp.kurtosis(vals))
