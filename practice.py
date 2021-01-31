# atplotlib inline
from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-3, 3, 0.01)

plt.plot(x, norm.pdf(x))
plt.savefig("yeet.png")

x = np.arange(-6, 6, 0.01)

plt.plot(x, norm.pdf(x))
plt.savefig("temp.png")