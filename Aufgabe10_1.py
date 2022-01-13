workfile = 'Aufgabe10_1.txt'
f = open(workfile, 'w')
j = 1
k = 1
for i in range(1,101):
    f.write("%3.0f,%3.0f,%3.0f\n" %(i,j,k))
    j = j+2
    k = k+3
f.close()
## printing lines in f
# f = open(workfile, 'r')
# lines = f.readlines()
# for line in lines:
#     print(line)
#f.close()

## Aufgabe 10_2
workfile2 = 'Aufgabe10_2.txt'
f2 = open(workfile2, 'w')
g = open(workfile, 'r')
lines = g.read().splitlines()
for line in lines:
    values = str.split(line, ",")
    ##empefehlung Ronny : line.split(',')
    sumofvalues = 0
    for item in values:
        sumofvalues = sumofvalues + int(item)
    f2.write("%3.1f,%3.1f,%3.1f,%3.1f \n"%(int(values[0]),int(values[1]),int(values[2]),sumofvalues))
f2.close()
g.close()

# printing lines in aufgabe 2
f3 = open(workfile2, 'r')
lines = f3.readlines()
for line in lines:
     print(line)
f3.close()

