import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("Automobile.csv")

series = df["make"].value_counts()

print (series.index[0:11])
print (series.values[0:11])

explode = (0.5,0,0,0,0,0,0,0,0,0,0)

plt.pie(series.values[0:11], explode = explode, labels=series.index[0:11], autopct='%2.2f%%')
plt.axis('equal')

plt.show()


#.....................................



from selenium import webdriver
import matplotlib.pyplot as plt

lsstate=[]
lsshare=[]
url="https://en.wikipedia.org/wiki/List_of_states_and_union_territories_of_India_by_area"
browser = webdriver.Chrome(r"C:\FSDK2019\chromedriver.exe")
browser.get(url)
for x in range (1,7):
    state=browser.find_element_by_xpath('//*[@id="mw-content-text"]/div/table[2]/tbody/tr['+str(x)+']/td[2]/a')
    share=browser.find_element_by_xpath('//*[@id="mw-content-text"]/div/table[2]/tbody/tr['+str(x)+']/td[5]')
    lsstate.append(state.text)
    lsshare.append(share.text)
colors=['red','blue','green','yellow','black','white'] 
explode=(0.2,0,0,0,0,0)
plt.pie(lsshare,labels=lsstate,colors=colors,explode=explode,autopct='%1.1f%%',shadow=True,startangle=90)   



#..............................................................

import pandas as pd
import matplotlib.pyplot as plt
df1=pd.DataFrame(columns=["name","sex","number","year"])
for i in range(1880,2018):
    filename="yob"+str(i)+".txt"
    df2=pd.read_csv(filename,header=None)
    df2.columns=["name","sex","number"]
    df2["year"]=i
    df2.sort_values(by=["number"],ascending=False)
    df1=pd.concat([df1,df2])

print("top 5 male in 2010\n",df1[(df1['sex']=='male') & (df1['year']=='2010')].head())    
print("top 5 female in 2010\n",df1[(df1['sex']=='female') & (df1['year']=='2010')].head()) 
df=df1.groupby(["year","sex"])["number"].aggregate("sum").unstack()
df.plot()


#........................................




import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv("Baltimore_City_Employee_Salaries_FY2014.csv")
df




