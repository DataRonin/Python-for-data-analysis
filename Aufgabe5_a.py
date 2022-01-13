#a
my_dict = {'Name':'Phanindra','Age':'28','Occupation':'Dreaming','Interests':'Flying','Residence': 'Berlin','Skillset': 'Systems engineering',
           'Programming': 'C++,Matlab,Python','Passion':'Sustainability Engineering'}

for skill,me in my_dict.items():
     print(f'{skill:<12}:{me:<12}')
#b
for me in sorted(my_dict.values()):
    print(me)

#c
op =''
for me in my_dict.values():
     op+=me+' '
print(op)

#d

print(my_dict)
print(sorted(my_dict.values()))
for skill,me in sorted(my_dict.items(), key =lambda item:item[1]):
    print(f'{skill:<12}:{me:<12}')