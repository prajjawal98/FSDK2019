
"""

Code Challenges:
    Name:
        University Admission Prediction Tool
    File Name:
        uni_admin.py
    Dataset:
        University_data.csv
    Problem Statement:
         Perform Linear regression to predict the chance of admission based on all the features given.
         Based on the above trained results, what will be your estimated chance of admission.

"""


import pandas as pd 
from sklearn.preprocessing import OneHotEncoder 



#imports the CSV dataset using pandas

dataset = pd.read_csv('University_data.csv')  
print(dataset)
temp = dataset.values
features = dataset.iloc[:, :-1].values
labels = dataset.iloc[:, -1].values

from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
features[:, 0] = labelencoder.fit_transform(features[:,0 ])



onehotencoder = OneHotEncoder(categorical_features = [0])
features = onehotencoder.fit_transform(features).toarray()
#for dropping
features = features[:, 1:]

from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.2, random_state = 0)


# Fitting Multiple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(features_train, labels_train)


# Predicting the Test set results
Pred = regressor.predict(features_test)
import pandas as pd

print (pd.DataFrame(Pred, labels_test))

import numpy as np
x = [0,0,0,0,0,339,4.6,4.6,9.8,1]
x = np.array(x)
regressor.predict(x.reshape(1, -1))







