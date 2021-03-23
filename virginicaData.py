# bit of experimenting with calculations on the data. Focusing on just verginico here

# Author: Caoimhin Vallely

import pandas as pd

iris = pd.read_csv('/Users/caoimhinvallely/Desktop/Programming/Programming2021/pands-project2021/irisDataset.csv')

virginica = iris[100:150]

# creates a dictionary to store averages in
virginicaAverages = {}

# calculations to find average for each dimension
x = sum(virginica['sepal_length'])
y = len(virginica['sepal_length'])
averageVirginicaSepalLength = round(x / y, 2)
virginicaAverages.update({"sepalLength": averageVirginicaSepalLength})
print("The average sepal length of virginica variety is:", str(averageVirginicaSepalLength) + 'cm')

a = sum(virginica['sepal_width'])
b = len(virginica['sepal_width'])
averageVirginicaSepalWidth = round(a / b, 2)
virginicaAverages.update({"sepalWidth": averageVirginicaSepalWidth})
print("The average sepal width of virginica variety is:", str(averageVirginicaSepalWidth) + 'cm')

c = sum(virginica['petal_length'])
d = len(virginica['petal_length'])
averageVirginicaPetalLength = round(c / d, 2)
virginicaAverages.update({"petalLength": averageVirginicaPetalLength})
print("The average petal length of virginica variety is:", str(averageVirginicaPetalLength) + 'cm')

e = sum(virginica['petal_width'])
f = len(virginica['petal_width'])
averageVirginicaPetalWidth = round(e / f, 2)
virginicaAverages.update({"petalWidth": averageVirginicaPetalWidth})
print("The average petal width of virginica variety is:", str(averageVirginicaPetalWidth) + 'cm')

# prints dict of averages
print(virginicaAverages)

# or I could have done this which will find the mean amongst a few other things!!!!!!!! :)
virginica_stats = virginica.describe()
print(virginica_stats)
# finds out the data type
print(type(virginica.describe()))
# finds correlation between all of the data
virginica_correlation = virginica.corr()
print (virginica_correlation)

