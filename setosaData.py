# ref: https://datacarpentry.org/python-ecology-lesson/03-index-slice-subset/index.html

# bit of experimenting with calculations on the data. Focusing on just the one variety here,
# but will do the same to the others. Will try and work on some visualisation then.

# Author: Caoimhin Vallely

import pandas as pd

iris = pd.read_csv('/Users/caoimhinvallely/Desktop/Programming/Programming2021/pands-project2021/irisDataset.csv')

# isolating the setosa data
setosa = iris[0:50]

# creates a dictionary to store averages in
setosaAverages = {}

# calculations to find average for each dimension
x = sum(setosa['sepal_length'])
y = len(setosa['sepal_length'])
averageSetosaSepalLength = round(x / y, 2)
setosaAverages.update({"sepalLength": averageSetosaSepalLength})
print("The average sepal length of Setosa variety is:", str(averageSetosaSepalLength) + 'cm')

a = sum(setosa['sepal_width'])
b = len(setosa['sepal_width'])
averageSetosaSepalWidth = round(a / b, 2)
setosaAverages.update({"sepalWidth": averageSetosaSepalWidth})
print("The average sepal width of Setosa variety is:", str(averageSetosaSepalWidth) + 'cm')

c = sum(setosa['petal_length'])
d = len(setosa['petal_length'])
averageSetosaPetalLength = round(c / d, 2)
setosaAverages.update({"petalLength": averageSetosaPetalLength})
print("The average petal length of Setosa variety is:", str(averageSetosaPetalLength) + 'cm')

e = sum(setosa['petal_width'])
f = len(setosa['petal_width'])
averageSetosaPetalWidth = round(e / f, 2)
setosaAverages.update({"petalWidth": averageSetosaPetalWidth})
print("The average petal width of Setosa variety is:", str(averageSetosaPetalWidth) + 'cm')

# prints dict of averages
print(setosaAverages)

# or I could have done this which will find the mean amongst a few other things!!!!!!!! :)
setosa_stats = setosa.describe()
print(setosa_stats)
# finds out the data type
print(type(setosa.describe()))
# finds correlation between all of the data
setosa_correlation = setosa.corr()
print (setosa_correlation)
