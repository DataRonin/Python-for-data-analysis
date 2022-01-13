
# printing lines in aufgabe 2

f3 = open('Aufgabe10_1.txt', 'r')
# lines = f3.readlines()
# for line in lines:
#       print(line)
# f3.close()
#Aufgabe11_1
#Teil a)

lines = f3.read().splitlines()
x = []
y1 = []
y2 = []
for line in lines:
    values = str.split(line, ",")
    x.append(int(values[0]))
    y1.append(int(values[1]))
    y2.append(int(values[2]))
f3.close()
import matplotlib.pyplot as plt
def newfigure(a,b,name,labelx,labely):
    fig, ax = plt.subplots()
    ax.plot(a,b, label = name)
    ax.set_xlabel(labelx)
    ax.set_ylabel(labely)
    ax.legend()
    plt.show()
newfigure(x,y1,'Increment 2','Real numbers','Odd numbers')
newfigure(x,y2,'Increment 3','Real numbers','Inkrement 3')
