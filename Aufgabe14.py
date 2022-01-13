import json
import numpy as np
import tkinter as tk
import matplotlib
from matplotlib import pyplot as plt
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
matplotlib.use('TkAgg')

root = tk.Tk()

#Data gathering and analysis
chemnitzweather = 'tk/Project/weather_hist.json'
with open(chemnitzweather) as f:
    weatherdata = json.load(f)

chemnitzweather = weatherdata['forecast']['forecastday'][0]['hour']


temp_c, wind_kph, hours, humidity = [], [], [] , []
for eachhour in range(len(chemnitzweather)):
    t_c = int(chemnitzweather[eachhour]['temp_c'])
    temp_c.append(t_c)
    w_kh = int(chemnitzweather[eachhour]['wind_kph'])
    wind_kph.append(w_kh)
    h = int(chemnitzweather[eachhour]['time'][-6:-3])
    hours.append(h)
    hum = int(chemnitzweather[eachhour]['humidity'])
    humidity.append(hum)
#print(len(temp_c) ,len(wind_kph), len(hours), len(humidity))

## Visualization
fig = plt.figure(1)
plt.ion()
plt.plot(hours,temp_c, label = 'Temperature', marker = 'x')
plt.title('Wetterverlauf in Chemnitz am 17.06.2021')
plt.legend()

canvas = FigureCanvasTkAgg(fig, master=root)
plot_widget = canvas.get_tk_widget()

#fig, ax = plt.subplots()
#ax.plot(hours,temp_c, label = 'Temperature', marker = 'x')
# ax.plot(hours,wind_kph, label = 'Wind',marker = 'o')
# ax.plot(hours,humidity, label='Humidity',marker = 'd')
# ax.legend()
# plt.show()
#print(hours)

def update():
    plt.plot(hours,wind_kph, label = 'Wind',marker = 'o')
    #d[0].set_ydata(s)
    plt.plot(hours,humidity, label='Humidity',marker = 'd')
    plt.legend()
    fig.canvas.draw()

plot_widget.grid(row=0, column=0)
tk.Button(root,text="Update",command=update).grid(row=1, column=0)
root.mainloop()