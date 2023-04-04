# Importing libraries

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import datetime as dt

def LinearRegression(X,Y):
	# mean of our inputs and outputs
	x_mean = np.mean(X)
	global y_mean
	y_mean = np.mean(Y)
	#total number of values
	global n
	n = len(X)
	# using the formula to calculate the m and c
	numerator = 0
	denominator = 0
	for i in range(n):
		numerator += (X[i] - x_mean) * (Y[i] - y_mean)
		denominator += (X[i] - x_mean) ** 2
		
	b1 = numerator / denominator
	b0 = y_mean - (b1 * x_mean)
	return b1, b0
def main() :
	# Importing dataset
	df = pd.read_csv( "depthvtemperature.csv",delim_whitespace=True)
	# print(df.head())
	# print(df.info())
	# plt.scatter( df['DEPTH_m'],df['DHAT_degC'],  color = 'blue' )
	# plt.title( 'Depth vs Temperature' )
	# plt.ylabel( 'Depth' )
	# plt.xlabel( 'Temperature' )
	# plt.show()
	X = df['DEPTH_m']
	Y = df['DHAT_degC']
	Y= Y.values.reshape(-1, 1)
	X= X.values.reshape(-1, 1)
	# # Model training
	m,c = LinearRegression(X,Y)
	print('Temperature ={}Depth + {}'.format(m,c))
	#plotting values 
	x_max = np.max(X) + 100
	x_min = np.min(X) - 100
	#calculating line values of x and y
	x = np.linspace(x_min, x_max, 1000)
	y = c + m * x
	#plotting line 
	plt.plot(x, y, color='#00ff00', label='Linear Regression')
	#plot the data point
	plt.scatter(X, Y, color='#ff0000', label='Data Point')
	# x-axis label
	plt.xlabel('Depth (m)')
	#y-axis label
	plt.ylabel('Temperature (degC)')
	plt.legend()
	plt.show()
	# Results
	rmse = 0
	for i in range(n):
		y_pred=  c + m* X[i]
		rmse += (Y[i] - y_pred) ** 2
    
	rmse = np.sqrt(rmse/n)
	print('RMSE: ',rmse)

	sumofsquares = 0
	sumofresiduals = 0
	for i in range(n) :
		y_pred = c + m * X[i]
		sumofsquares += (Y[i] - y_mean) ** 2
		sumofresiduals += (Y[i] - y_pred) **2
		
	score  = 1 - (sumofresiduals/sumofsquares)
	print('Score: ',score)
	
if __name__ == "__main__" :
	main()
