# class Bike():
#     def __init__(self, name, brand):
#         self.name = name
#         self.brand = brand
#     def ring(self):
#         print('Ringing..')
#     def shift_gear(self):
#         print('Shifting gear..')
# myBike = Bike('Sirrus','Specialized') # ein Neue Instanz der Klasse 'Bike' erstellen
# myBike.ring()
# myBike.shift_gear()
#print(myBike.ring())#
# import matplotlib.pyplot as plt
# # plt.plot ([1,2,3,4],[1,4,9,16],'o-r', label='data')
# # plt.axis([0,5,0,18])
# # plt.ylabel('einige Zahlen')
# # plt.title('Simple plot')
# # plt.legend()
# # plt.show()
# import numpy as np
# # x = np.linspace(0,2,100)
# # fig, ax = plt.subplots() #generated a figure
# # ax.plot(x,x,label = 'linear') # plotting a linear curve
# # ax.plot(x,x**2,label = 'quadratic') # plotting a quadratic curve
# # ax.plot(x,x**3,label = 'cubic') # plotting a cubic curve
# # ax.xlabel('Nummers')
# # ax.set_title('Simple plot')
# years = np.linspace(1900,2017,118)
# indexValues = np.linspace(68,20656,118)
# fig,ax = plt.subplots()
# ax.plot(years, indexValues)
# print(years)
# plt.show()

# with open('kap_12_employee_birthday.txt') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     line_count = 0
#     for row in csv_reader:
#         if line_count == 0:
#             print(f"\tSpaltenname sind: {','.join(row).title()}")
#             line_count+=1
#         else:
#             print(f"\t{row[0]} arbeitet in der {row[1]} Abteilung, und ist im {row[2]} geboren")
#             line_count+=1
# print(f"\tBearbeitet:{line_count} Zeilen.")
# with open('employee_file.csv', mode = 'a',newline='\n') as employee_file:
#     employee_writer = csv.writer(employee_file, delimiter=',',quotechar='"')
#     employee_writer.writerow(['Claus Schmidt','Buchhaltung', 'November'])
#     employee_writer.writerow(['Herta Kleber', 'IT', 'März'])
#     employee_writer.writerow(['Clemens Matulla', 'Engineering', 'Mai'])
# import csv
# import matplotlib.pyplot as plt
# with open('12_Wetter_Daten_1949_2014.txt', 'r') as weatherdata:
#     csv_reader = csv.reader(weatherdata)
#     Titelzeile = next(csv_reader)
#     print(Titelzeile)
#     for index, Spaltentitel in enumerate(Titelzeile):
#         print(index, Spaltentitel)
#     values = []
#     pos = int(input('Enter Column Number to Visualize:'))
#     for row in csv_reader:
#         try:
#             values.append(float(row[pos]))
#         except:
#             continue
# p
# # print(values)
# import matplotlib.pyplot as plt
# import csv
# import json
#
# data = {}
# pos = 0
# max_rows = 20
#
# year = ""
#
# # with open("sitka_weather_2018_simple.csv","r") as datafile:
# with open("12_Wetter_Daten_1949_2014.txt", "r") as datafile:
#     csv_reader = csv.reader(datafile)
#     title_line = next(csv_reader)
#     year = input("Enter year: ")
#     #for index, col_title in enumerate(title_line):
#         #print(index, col_title)
#     # print(title_line[0])
#
#     pos = input("Enter columns number to visualize: ")
#     cols = pos.split(',')
#     for col in cols:
#         data[title_line[int(col)]] = []
#     data["Year"] = year
#     # print(data)
#
#     for row in csv_reader:
#
#         try:
#             if row[0][0:4] == year:
#                 for col in cols:
#                     data[title_line[int(col)]].append(float(row[int(col)]))
#
#                 max_rows -= 1
#                 if max_rows <= 0:
#                     break
#         except:
#             continue
#
# print(json.dumps(data, sort_keys=True, indent=4))
# # print(data)
#
# plt.style.use("seaborn")
#
# for name in data:
#     if name != "Year":
#         x = list(range(0, len(data[name])))
#         plt.plot(x, data[name], "-", label=name)
#
# plt.xlabel("x")
# plt.ylabel("y")
# plt.legend()
#
# plt.show()
import json
# #x='{"name":"Max","alter":"34", "Wohnort":"Buenos Aires" }'
# # x als json string einlesen und verarbeiten
# #res = json.loads(x)
# # Das Ergebnis ist ein Python Dictionary
# #print (res["alter"])
# json_string = '{"first_name": "claus","last_name":"Liebermann","citizenship":"dutch"}'
# parsed_json = json.loads(json_string)
# #print(parsed_json['first_name'])
# gp_json_string = '{"name":"Phanindra","alter":"28", "Wohnort":"Blau Bär Land" }'
# with open('test_file.json','w') as myfile:
#     json.dump(gp_json_string,myfile)
# with open('test_file.json','r') as j:
#     json_data = json.load(j)
# #print(json_data)
# # defining a doc string
# my_json_docstring = """{
# "Report":[
# {
# "id":"04",
# "language": "Data",
# "edition": "first"
# }
# ]
# }
# """
# parsed_json_docstring =json.loads(my_json_docstring)
# new_data = {"id":"05"}
# parsed_json.update(new_data)
# print(parsed_json_docstring,type(parsed_json_docstring))
import plotly.graph_objs
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline
filename = 'data/eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)
all_eq_dicts = all_eq_data['features']
mags, lons, lats, hover_texts = [] , [] , [] , []

for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    title = eq_dict['properties']['title']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_texts.append(title)
print(mags[0:10])
print(lons[0:10])
print(lats[0:10])
#map the earthquakes.

data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size':[5*mag for mag in mags],
        'color': mags,
        'colorscale':'Viridis',
        'reversescale': True,
        'colorbar': {'title':'Magnitude'},
    } ,
}]

my_layout = Layout(title='Global Earthquakes')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')