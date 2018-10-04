import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pygal
from pygal import *

a = pd.read_csv('NSE-HAL.csv')
Open = a.iloc[:,1]
High = a.iloc[:,2]
Low = a.iloc[:,3]
Last = a.iloc[:,4]
Close = a.iloc[:,5]
TotalTradeQuantity = a.iloc[:,6]
Turnover(Lacks) = a.iloc[:,7]

chart_style = LightGreenStyle()
chart_style.plot_background = '#505051'
chart_style.major_label_font_size = 20
chart_style.label_font_size = 15
chart_style.title_font_size = 25

my_config = pygal.Config()
my_config.width = 1000
my_config.height = 720
#my_config.dots_size = 5
my_config.show_y_guides = False
my_config.show_legend = False

chart = pygal.Line(style= chart_style,config= my_config, fill=True, zero=1)
chart.force_uri_protocol = 'http'

x = np.arange(117)

chart.title = 'NSE-HAL STOCKS'
chart.x_labels = x
chart.y_title = 'Stock Details'

chart.add('Open',Open)
chart.add('High', High)
chart.add('Low',Low)
chart.add('Last',Last)
chart.add('Close',Close)
chart.add('TotalTradeQuantity',TotalTradeQuantity)
chart.add('Turnover(Lacks)',Turnover(Lacks))

chart.render_to_file('nsehal.svg')
