import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

a = pd.read_csv('NSE-HAL.csv')
x = np.arange(117)

plt.title("NSE-HAL STOCKS", fontsize=24)
plt.xlabel("Value", fontsize=18)
plt.ylabel("Stock Values", fontsize=18) 
plt.tick_params(axis='both',which='major', labelsize=15)

plt.scatter(x, a['Open'], c='blue', edgecolor='none', s=20)
plt.scatter(x, a['High'], c='red', edgecolor='none', s=20)
plt.scatter(x, a['Low'], c='green', edgecolor='none', s=20)
plt.scatter(x, a['Last'], c='yellow', edgecolor='none', s=20)
plt.scatter(x, a['Close'], c='black', edgecolor='none', s=20)

fig, axarr = plt.subplots(2, 1, sharex=True) 

axarr[0].scatter(x,a['Total Trade Quantity'], c='purple', edgecolor='none', s=20)
axarr[0].set_title('Quantity')
axarr[1].scatter(x, a['Turnover (Lacs)'], c='skyblue', edgecolor='none', s=20)
axarr[1].set_title('Turnover')

plt.savefig('Nse-Hal.png', bbox_inches='tight') 
