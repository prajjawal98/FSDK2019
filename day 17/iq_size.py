"""
Q. (Create a program that fulfills the following specification.)
iq_size.csv

Are a person's brain size and body size (Height and weight) predictive of his or her intelligence?

 

Import the iq_size.csv file

It Contains the details of 38 students, where

Column 1: The intelligence (PIQ) of students

Column 2:  The brain size (MRI) of students (given as count/10,000).

Column 3: The height (Height) of students (inches)

Column 4: The weight (Weight) of student (pounds)

    What is the IQ of an individual with a given brain size of 90, height of 70 inches, and weight 150 pounds ? 
    Build an optimal model and conclude which is more useful in predicting intelligence Height, Weight or brain size.


"""



import matplotlib.pyplot as plt
import pandas as pd 

#imports the CSV dataset using pandas

dataset = pd.read_csv('iq_size.csv')  
print(dataset)

features=dataset.iloc[:,1:4].values
labels=dataset.iloc[:,0:1].values



import statsmodels.api as sm

features = sm.add_constant(features)




features_opt = features[:,:4]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()





features_opt = features[:,:3]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()


features_opt = features[:,1:3]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()


features_opt = features[:,1:2]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()



from sklearn.preprocessing import PolynomialFeatures
poly_object = PolynomialFeatures(degree = 5)
features_poly = poly_object.fit_transform(features)


from sklearn.linear_model import LinearRegression

lin_reg_2 = LinearRegression()
lin_reg_2.fit(features_poly, labels)


import numpy as np
x = np.array([90,65,117])
x=x.reshape(1,-1)

print( lin_reg_2.predict(poly_object.transform(x)))























