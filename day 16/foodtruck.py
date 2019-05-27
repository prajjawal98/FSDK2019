

"""
Code Challenge: Simple Linear Regression
  Name: 
    Food Truck Profit Prediction Tool
  Filename: 
    Foodtruck.py
  Dataset:
    Foodtruck.csv
  Problem Statement:
    Suppose you are the CEO of a restaurant franchise and are considering 
    different cities for opening a new outlet. 
    
    The chain already has food-trucks in various cities and you have data for profits 
    and populations from the cities. 
    
    You would like to use this data to help you select which city to expand to next.
    
    Perform Simple Linear regression to predict the profit based on the 
    population observed and visualize the result.
    
    Based on the above trained results, what will be your estimated profit, 
    
    If you set up your outlet in Jaipur? 
    (Current population in Jaipur is 3.073 million)
        
  Hint: 
    You will implement linear regression to predict the profits for a 
    food chain company.
    Foodtruck.csv contains the dataset for our linear regression problem. 
    The first column is the population of a city and the second column is the 
    profit of a food truck in that city. 
    A negative value for profit indicates a loss.
"""













import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  

#imports the CSV dataset using pandas

dataset = pd.read_csv('foodtruck.csv')  
print(dataset)

#explore the dataset
print( dataset.shape)
print( dataset.ndim)
print( dataset.head())

print( dataset.describe())

plt.boxplot(dataset.values)

dataset.plot(x='Population', y='Profit', style='o')  
plt.title('Population vs Profit')  
plt.xlabel('Population')  
plt.ylabel('Profit')  
plt.show()

features = dataset.iloc[:, :-1].values  
labels = dataset.iloc[:, 1].values 



from sklearn.linear_model import LinearRegression  
regressor = LinearRegression()  
regressor.fit(features, labels) 

"""
str1=input("enter the population city")
popul=float(str1)
print("estimated profit",regressor.predict(popul)[0])
"""



print(regressor.intercept_)  
print (regressor.coef_)

print( regressor.predict(3.073))
