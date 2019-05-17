"""import random
names = ['Mary', 'Isla', 'Sam']
code_names = ['Mr. Pink', 'Mr. Orange', 'Mr. Blonde']

for i in range(len(names)):
    names[i] = random.choice(code_names)

print (names)"""

import random
code_names = ['Mr. Pink', 'Mr. Orange', 'Mr. Blonde']
a = ['Mary', 'Isla', 'Sam']


s=list(map(lambda x:random.choice(code_names),a))

print(list(s))



#............................

list1 = ['2001', '121', '922']
list2 = []
list3 = []

for number in list1:
    if number == number[::-1]:
        list2.append('True')
    else:
        list2.append('False')

for number in list1:
    if int(number) > 0:
        list3.append('True')
        
    else:
        list3.append('False')

if 'True' in list2 and 'False' not in list3:
   print('True')
else:
    print('False')
    
#.....................................


names = ['Mary', 'Isla', 'Sam']
s=list(map(lambda x:hash(x),names))
print(s)
    
#...................................
from functools import reduce
people = [{'name': 'Mary', 'height': 160},
          {'name': 'Isla', 'height': 80},
          {'name': 'Sam'}]
height_total = 0
height_count = 0

def f(x):
    if 'height' in x:
        return x
filter_list=filter(f,people)

map_list=list(map(lambda x:x['height'],filter_list))
sum1=reduce(lambda x,y:x+y,map_list)
average=sum1/(len(list2))
print(average)

#...................................


order = [[34587,'Learning Python','Mark Lutz',4,40.95],
         [98762,'Programming Python','Mark Lutz',5,56.80],
         [77226,'Head First Python','Paul Barry',3,32.95],
         [88112,'EinfÃ¼hrung in Python3','Bernd Klein',3,24.99]
        ]

#without using lambda,map,list comprehension

lists = []
for item in order:
    if item[-1]*item[-2] < 100:
        lists.append((item[0],item[-1]*item[-2]+10))
    else:
        lists.append((item[0],item[-1]*item[-2]))

print("Order Summary: ",lists)

#now lambda, map, reduce
print("Order Summary: ",list(map(lambda x: (x[0],x[-1]) if x[-1]*x[-2] > 100 else x[-1]*x[-2]+10, order)))

#using list comprehension

print("Order Summary: ",[(item[0],item[-1]) if item[-1]*item[-2] > 100 else (item[0],item[-1]*item[-2]+10) for item in order])






    

    

