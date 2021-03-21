# few simple calculations on overall dataset
# Author: Caoimhin Vallely

import pandas as pd

iris = pd.read_csv("/Users/caoimhinvallely/Desktop/Programming/Programming2021/pands-project2021/irisDataset.csv")
sepalLength = iris['sepal_length']
sepalWidth = iris['sepal_width']
petalLength = iris['petal_length']
petalWidth = iris['petal_width']
species = iris['species']

# average sepal length
x = sum(iris['sepal_length'])
y = len(iris['sepal_length'])
averageSepalLength = round(x / y, 2)
print(str(averageSepalLength) + 'cm')

# average sepal width
x = sum(iris['sepal_width'])
y = len(iris['sepal_width'])
averageSepalLength = round(x / y, 2)
print(str(averageSepalLength) +'cm')

# average patel length
x = sum(iris['petal_length'])
y = len(iris['petal_length'])
averageSepalLength = round(x / y, 2)
print(str(averageSepalLength) + 'cm')

# average petal width
x = sum(iris['sepal_length'])
y = len(iris['sepal_length'])
averageSepalLength = round(x / y, 2)
print(str(averageSepalLength) + 'cm')


