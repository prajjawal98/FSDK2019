
"""
Code Challenge: Simple Linear Regression

  Name: 
    Box Office Collection Prediction Tool
  Filename: 
    Bahubali2vsDangal.py
  Dataset:
    Bahubali2vsDangal.csv
  Problem Statement:
    It contains Data of Day wise collections of the movies Bahubali 2 and Dangal 
    (in crores) for the first 9 days.
    
    Now, you have to write a python code to predict which movie would collect 
    more on the 10th day.
  Hint:
    First Approach - Create two models, one for Bahubali and another for Dangal
    Second Approach - Create one model with two labels
"""

import pandas as pd  



#imports the CSV dataset using pandas

dataset = pd.read_csv('Bahubali2_vs_Dangal.csv')  
print(dataset)

#for bahubali 

features = dataset.iloc[:, :-2].values  
labels = dataset.iloc[:, 1:2].values 


from sklearn.linear_model import LinearRegression  
regressor = LinearRegression()  
regressor.fit(features, labels) 

print(regressor.intercept_)  
print (regressor.coef_)

print( regressor.predict(10))


#for dangal


features = dataset.iloc[:, :-2].values  
labels = dataset.iloc[:, 2:].values 


from sklearn.linear_model import LinearRegression  
regressor = LinearRegression()  
regressor.fit(features, labels) 

print(regressor.intercept_)  
print (regressor.coef_)

print( regressor.predict(10))


#for on model to two labels

features = dataset.iloc[:, :-2].values  
labels = dataset.iloc[:, 1:3].values 


from sklearn.linear_model import LinearRegression  
regressor = LinearRegression()  
regressor.fit(features, labels) 

print(regressor.intercept_)  
print (regressor.coef_)

print( regressor.predict(10))
"""
print(" for bahubali ",regressor.predict(10)[0][0])
print(" for bahubali ",regressor.predict(10)[0][1])


"""







