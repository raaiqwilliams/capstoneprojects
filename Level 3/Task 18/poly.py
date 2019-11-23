# For my polynomial regression, I have chosen to regress the results of Temperature of water (in Celsius) on
# their respective pressures (in Pascals)
import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# Training set
x_train = [[0],[20],[40],[60],[80],[100]] #Temperature values
y_train = [[0.0002],[0.0012],[0.0060],[0.0300],[0.0900],[0.2700]] #Pressure values

# Fitting Linear Regression to the data set
regressor = LinearRegression()
regressor.fit(x_train, y_train)

# Fitting Polynomial Regression to the data set
quadratic_featurizer = PolynomialFeatures(degree = 2)
X_poly = quadratic_featurizer.fit_transform(x_train)

quadratic_featurizer.fit(X_poly, y_train)
regressor2 = LinearRegression()
regressor2.fit(X_poly, y_train)

#Visualizing Regression results
plt.scatter(x_train, y_train, color ='b')
plt.plot(x_train, regressor.predict(x_train))
plt.plot(x_train, regressor2.predict(quadratic_featurizer.fit_transform(x_train)), color = 'r', linestyle='--')
plt.title('Temperature regressed on pressure')
plt.xlabel('Temperature (in Celsius)')
plt.ylabel('Pressure (in Pascals)')
plt.show()
