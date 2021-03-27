# bit of experimenting with calculations on the data. Focusing on just versicolor here

# Author: Caoimhin Vallely

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

iris = pd.read_csv('/Users/caoimhinvallely/Desktop/Programming/Programming2021/pands-project2021/irisDataset.csv')

# isolating the setosa data
versicolor = iris[50:100]

# creates a dictionary to store averages in
versicolorAverages = {}

# calculations to find average for each dimension
x = sum(versicolor['sepal_length'])
y = len(versicolor['sepal_length'])
averageVersicolorSepalLength = round(x / y, 2)
versicolorAverages.update({"sepalLength": averageVersicolorSepalLength})
print("The average sepal length of versicolor variety is:", str(averageVersicolorSepalLength) + 'cm')

a = sum(versicolor['sepal_width'])
b = len(versicolor['sepal_width'])
averageVersicolorSepalWidth = round(a / b, 2)
versicolorAverages.update({"sepalWidth": averageVersicolorSepalWidth})
print("The average sepal width of versicolor variety is:", str(averageVersicolorSepalWidth) + 'cm')

c = sum(versicolor['petal_length'])
d = len(versicolor['petal_length'])
averageVersicolorPetalLength = round(c / d, 2)
versicolorAverages.update({"petalLength": averageVersicolorPetalLength})
print("The average petal length of versicolor variety is:", str(averageVersicolorPetalLength) + 'cm')

e = sum(versicolor['petal_width'])
f = len(versicolor['petal_width'])
averageVersicolorPetalWidth = round(e / f, 2)
versicolorAverages.update({"petalWidth": averageVersicolorPetalWidth})
print("The average petal width of versicolor variety is:", str(averageVersicolorPetalWidth) + 'cm')

# prints dict of averages
print(versicolorAverages)

# or I could have done this which will find the mean amongst a few other things!!!!!!!! :)
versicolor_stats = versicolor.describe()
print(versicolor_stats)
# finds out the data type
print(type(versicolor.describe()))
# finds correlation between all of the data
versicolor_correlation = versicolor.corr()
print (versicolor_correlation)
