import csv
import matplotlib.pyplot as plt
with open('12_Wetter_Daten_1949_2014.txt', 'r') as weatherdata:
    csv_reader = csv.reader(weatherdata)
    Titelzeile = next(csv_reader)
    #for index, Spaltentitel in enumerate(Titelzeile):
         #print(index, Spaltentitel)
    values = []
    pos = input('Enter Column Number to Visualize:')
    i = 0
    for row in csv_reader:
        print(row[0][0:4])
        i = i+1
    print(i)
    #     try:
    #         values.append(float(row[pos]))
    #     except:
    #         continue
    #for column in csv_reader:
     #   print(column[0])
#print(values)
#
# x=list(range(0,len(values)))
#
# plt.style.use("seaborn")
# plt.plot(x,values,"-",label=title_line[pos])
#
# plt.xlabel("x")
# plt.ylabel("y")
#
# plt.legend()
#
# plt.show()