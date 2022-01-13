#Aufgabe6_a:
# Wochentage=['Montag','Dienstag','Mittwoch','Donnerstag','Freitag','Samstag','Sonntag']
# colors = ['gray', 'light gray', 'dark gray', 'almost white', 'black', 'light black', 'grayish White']
# #colors.sort()
# for i in Wochentage:
#     k = Wochentage.index(i)
    #print('Meine Lieblingfarbe für',i,'ist',colors[k])
#Aufgabe6_b:
Wochentage = ['Montag','Dienstag','Mittwoch','Donnerstag','Freitag']
kz = {} #defining an empty dictionary
i=0
while i<5:
    Tag = Wochentage[i]
    Kaffeezeit = input(f"Wann möchtest du am {Tag} deinen Frühstückskaffee trinken? Bitte nur Zahlen zwischen 0 und 2400 eingeben,zbs 0730,0800 usw..")
    if Kaffeezeit.isdigit():
        Kaffeezeit = int(Kaffeezeit)
        if 0 <Kaffeezeit<2401:
            kz[Tag] = Kaffeezeit
            i = i+1
        else:
            print('Bitte nur Zahlen zwischen 0 und 2400 eingeben,zbs 0730,0800 usw..')
    else:
        print('Bitte nur Zahlen zwischen 0 und 2400 eingeben,zbs 0730,0800 usw..')

late = max(kz.values()) # when do I have the coffee the latest
#print(f"Am {Tag} trinkst du deinen Frühstückskaffee spät")
i = 0
late_days = []
for Tag, Zeit in kz.items(): #writing a loop to output my late coffee day
     if Zeit == late:
         i = i+1
         late_days.append(Tag)
print(i)
print(late_days)
if i == 1:
    print(f"Am {late_days[0]} trinkst du deinen Frühstückskaffee spät")
else:
    j =1
    while j<i:
        name = ' und ' + late_days[j]
        j = j+1
    print(f"Am {late_days[0]+name} trinkst du deinen Frühstückskaffee spät")
#Aufgabe6_c
