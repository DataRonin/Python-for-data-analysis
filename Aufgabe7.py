Wochentage = ['Montag','Dienstag','Mittwoch','Donnerstag','Freitag']
j = 1
Woche = {'Montag':1,'Dienstag':2,'Mittwoch':3,'Donnerstag':4,'Freitag':5}
#termin = ('Mittwoch','Freitag')
#difference = 'difference'
while j <= 5:
    i = 0
    while i <= 4:
        k = j%2
        if k == 1:
            termin = Wochentage[2]
        else:
            termin = Wochentage[3]
        heute = Wochentage[i]
        difference = abs(Woche[termin] - Woche[heute])
        print(f"Woche{j}: Heute ist {heute}. Ihr Friseirtermin liegt diese Woche am {termin}, also {difference}")
        i = i+1
    j = j+1
#print(Woche['Montag'])