import pandas as pd
df = pd.read_csv("training_titanic.csv")
df
x=df['Survived'].value_counts()
print("Survived is ",x[1])
print("dead is",x[0])
a=df['Survived'].value_counts(normalize = True)[1]
print("percentage of survived",a)
b=df['Survived'][df["Sex"]=="male"].value_counts(normalize = True)[1]
print("percentage of male",b)
c=df['Survived'][df["Sex"]=="female"].value_counts(normalize = True)[0]
print("percentage of male",c)


df['Age'] = df['Age'].fillna(df['Age'].mean())
df["child"] = df["Age"].map(lambda x: 1 if x<18 else 0 )
df

#........................................

import numpy as np
import pandas as pd
df = pd.read_csv("Automobile.csv")
df
df['price'] = df['price'].fillna(df['price'].mean())
ar=np.array(df['price'])
defi=df["price"].describe()
print("max is", defi[7])
print("min is",defi[3])
print("mean is",defi[1])
print("std is",defi[2])


#......................................

import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv("Telecom_churn.csv")
df
df1= df.loc[(df['voice mail plan']=='yes') & (df['international plan']=='yes') & (df["churn"]==True)]
count=df1.count()[4]
print("customers on both voice mail plan and international plan",count)
s=df["total intl charge"].loc[(df["churn"]==True)]
s1=df["total intl charge"].loc[(df["churn"]==False)]
churn=s.sum()
nchurn=s1.sum()
labels='CHURN','NONCHURN'
sizes=[churn,nchurn]
colors=["blue","red"]
explode=(0,0)
plt.pie(sizes,labels=labels,colors=colors,explode=explode,autopct='%1.1f%%',shadow=True,startangle=0)

d1=df.loc[(df["churn"]==True)]
max1=d1["total night minute"].max()
print(d1["state"].loc(d1["total night minute"]==max1))






