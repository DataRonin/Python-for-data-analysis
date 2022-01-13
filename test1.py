# # my_dict = {698:'Phani','Age':28,'Occupation':'Jobless','Interests':'Flying'}
# # age=my_dict[698]
# # agenow=age+'10'
# # #print(agenow)
# # my_dict['Residence']='Berlin'
# # my_dict['Occupation']='Dreaming'
# # del my_dict[698]
# # # print(my_dict)
# # ur_dict={'Skillset':'Systems engineering','Programming':['C++','Python'],'Location':'Berlin'}
# # print(ur_dict)
# # print(my_dict)
# # for me,mine in sorted(my_dict.items()):
# #     print(f'{me:<10}:{mine:<10}')
# large_dict = {'my_dict':{'Age': 28, 'Occupation': 'Dreaming', 'Interests': 'Flying', 'Residence': 'Berlin'},
#                'ur_dict':{'Skillset': 'Systems engineering', 'Programming': ['C++', 'Python'], 'Location': 'Berlin'}}
# # print(large_dict)
#
# # colors = ['green','red','yellow','blue']
# # for color in colors:
# #     if color=='red':
# #         print(color)
# ALIEN_COLOR = {'green':85, 'yellow':'56', 'red':'67'}
# # #print(ALIEN_COLOR.get('gre','Not there dude'))
# # for x,y in ALIEN_COLOR.items():
# #     print(f"{x}'s favorite number is {y}")
# # size = 20
# # minsize = 12
# # print(size >= minsize)
#
# favorite_languages = {'jen': 'python','sarah': 'c','edward': 'ruby','phil': 'python',}
# #friends = ['phil', 'sarah']
# # for name in favorite_languages:
# #     print(name)
# #     if name in friends:
# #         print(f"{name}, I see you love {favorite_languages[name]}")
#
#
# # Namen={}
# # if Namen:
# #     print('not empty')
# # elif len(Namen) == 0:
# #     print('bruh, empty af')
# #
#
# # a = 6
# # b = 'bananas'
# # c = 1.268986
# # print('%d %s costs $ %.3f' %(a,b,c))
#
# # name = 'Fred'
# # #print(f"He said his name is {name!r}")
# # print(f"He said his name is {name}")
#
# # width = 10
# # precision=4
# # value=decimal.Decimal('')
# print(ALIEN_COLOR,'\t ',favorite_languages)
# kz = {'Montag': 360, 'Dienstag': 560, 'Mittwoch': 780, 'Donnerstag': 9810, 'Freitag': 558}
# #kzsorted = sorted(kz.values())
# print(kz[360])
# i =2
# while i in range(2,11):
#     i+=1
#     if i%2==0:
#         continue
#     print(i)
# AT = []
# WT = ['mo','di','mi','do','fr','sa','so']
#
# while WT:
#     day = WT.pop()
#     res = input('Do you work on '+ day+' ?(y or n)')
#     if res == 'y':
#         AT.append(day)
# print(AT)
# print(WT)
# from _datetime import date, time, datetime
# today = date.today()
# print(today)
# now = datetime.now()
# current_time = time(now.hour,now.minute, now.second)
# print(current_time)
# print(now)
Wochentage = ['Montag','Dienstag','Mittwoch','Donnerstag','Freitag']
kz = {} #defining an empty dictionary
i=0
while i<5:
    Tag = Wochentage[i]
    Kaffeezeit = input(f"Wann möchtest du am {Tag} deinen Frühstückskaffee trinken? Bitte nur Zahlen zwischen 0 und 2400 eingeben,zbs 0730,0800 usw..")