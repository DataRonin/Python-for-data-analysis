import datetime # importing the datetime module
t = datetime.datetime.today() #assigning today's date to the variable t
t = str(t) #converting t to a string
t = t.split()
print('Das heutige Datum ist:',t[0])