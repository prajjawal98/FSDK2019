str1=input("enter the days of weeks")
tup1=str1.split(",")
print(tup1)
tup2=("monday","tue","wednes","thur","friday","saturday","sunday")
for days in tup2:
    if days in tup1:
        continue
    else:
        tup1.append(days)
tup2=tuple(tup1)        
print(tup2)       


#.......................

def char_frequency(str1):
   dict={}
   for n in str1:
     keys=dict.keys()
     if n in keys:
       dict[n]+=1
     else:
       dict[n]=1
   return dict
print(char_frequency("google.com"))



#..........................

list1=[12,21,34,54,65,45,76,76]
set1=set(list1)
list2=list(set1)
print(list2[::-1])

#............................


s1=[1,3,6,78,35,55]
s2=[12,24,35,24,88,120,155]
s3=set(s2).intersection(set(s1))
print(s3)


#....................

str1=input("enter any string")
count1=0
count2=0
for i in str1:
    if(i.isdigit()):
        count1=count1+1
    elif(i.isalpha()) :   
        count2=count2+1
    else:
        continue
print("number of digits")
print(count1)
print("number of letter")
print(count2)    


#................................


sum=0
dict1={'a':0,'b':0,'c':0}
print("input three values")
dict1['a']=int(input("a"))  
dict1['b']=int(input("b"))
dict1['c']=int(input("c")) 
print(dict1)
for val in dict1.values():
    if val==(15 or 16):
        sum=sum+val
    elif val in range(13,20):
        continue
    else:
        sum=sum+val
print("your sum is",sum)        


#............................



d={}

while True:
    entry=input("enter dict")
    if not entry:
        break
    
    list1=entry.split()
    
    value=int(list1[-1])
    key="".join(list1[:-1])
    if key in d:
      d[key]+=value
    else:
        d[key]=value
        
print(d)        
        
        
    
#......................
old_list=["prjjawal@mac.com",
          "utkrsh@gmail.com"]
new_list=["prahhh@dhs.com",
          "hshdhhs@hf.com"]
for item in old_list:
    if item not in new_list:
      new_list.append(item)
print(new_list)            
            