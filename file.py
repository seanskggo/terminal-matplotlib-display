# Demo
from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-3, 3, 0.01)

plt.plot(x, norm.pdf(x))
## First graph
plt.savefig("temp1.png")

x = np.arange(-6, 6, 0.01)

## Second graph
plt.plot(x, norm.pdf(x))
plt.savefig("temp2.png")