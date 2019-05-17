a=int(input("enter the value"))
i=0
while(a>i):
    print("*"*i)
    i=i+1
while(0<i):
    print("*"*i)
    i=i-1
    
#..........................

 


    

#............................

list1 = ['2001', '121', '2003']
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
    print ('True')
else:
    print ('False')
    
    
    
    
 #.................................


   