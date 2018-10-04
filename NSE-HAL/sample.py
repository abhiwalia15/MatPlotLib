import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

a = pd.read_csv('NSE-HAL.csv')
x = np.arange(117)

plt.plot(x, a['Open'])
plt.show()
