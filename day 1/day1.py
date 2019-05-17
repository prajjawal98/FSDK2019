travel=float(input("enter the travel value"))
fuel=float(input("enter fuel value"))
avg=float(travel/fuel) 
print(avg)
     
#............................

travel=float(input("enter the travel"))
cost=float(input("enter the cost"))
avg_car=float(input("enter the avg value"))
cost_car=float(travel*avg/cost)
print(cost_car)


#.........................


ass1=float(input("enter the value of ass1"))
ass2=float(input("enter the value of ass2"))
ass3=float(input("enter the value of ass3"))

exam1=float(input("enter the value of exam1"))
exam2=float(input("enter the value of exam2"))

weighted_score = ( ass1 + ass2 + ass3 ) *0.1 + (exam1 + exam2 ) * 0.35
print(weighted_score)


#......................

import math
num=int(input("enter number"))

a=math.factorial(num)
print(a)


#..........................

str=input("enter string")

print(str.upper())
print(str.lower())
print(str.capitalize())


#........................

str=input("enter any string")
index=str.index('R')
a=str[:index+1]+str.replace('R','$')[index+1:]
print(a)

#...........................


str=input("enter any string")
list=str.split()
list1=list[1]+list[0]
print(list1)


#.................


str=input("enter any string")
a=str.split()
b="*".join(a)
print(b)


#...........................

str=input("enter any string")
a="*".join(str)
print(a)

#..............................


a=0
while(a<101):
    a=a+1
    if a%15==0:
        print("fizzbuzz")
        
    elif a%3==0:
        print("fizz")
        
    elif a%5==0:
        print("buzz")
        
    
    else:
        print(a)
        


