# few simple calculations on overall dataset
# Author: Caoimhin Vallely

import pandas as pd
import matplotlib.pyplot as plt

# overall overview
# some borrowed from https://medium.com/@avulurivenkatasaireddy/exploratory-data-analysis-of-iris-data-set-using-python-823e54110d2d
iris = pd.read_csv("/Users/caoimhinvallely/Desktop/Programming/Programming2021/pands-project2021/irisDataset.csv")

print("First five rows")
print(iris.head())
print("*********")
print("columns",iris.columns)
print("*********")
print("shape:",iris.shape)
print("*********")
print("Size:",iris.size)
print("*********")
print("*********")
print(iris.describe())

iris_sepal_length = iris['sepal_length']
iris_sepal_width = iris['sepal_width']
iris_petal_length = iris['petal_length']
iris_petal_width = iris['petal_width']
species = iris['species']

iris_stats = iris.describe()
# print(iris_stats)
iris_correlation = iris.corr()
# print(iris_correlation)

# setosa species overview
setosa = iris[0:50]
setosa_stats = setosa.describe()
# print(setosa_stats)

setosa_sepal_length = iris_sepal_length[0:50]
setosa_sepal_width = iris_sepal_width[0:50]
setosa_petal_length = iris_petal_length[0:50]
setosa_petal_width = iris_petal_width[0:50]

# versicolor species overview
versicolor = iris[50:100]
versicolor_stats = versicolor.describe()
# print(versicolor_stats)

versicolor_sepal_length = iris_sepal_length[50:100]
versicolor_sepal_width = iris_sepal_width[50:100]
versicolor_petal_length = iris_petal_length[50:100]
versicolor_petal_width = iris_petal_width[50:100]

# virginica species overview
virginica = iris[100:150]
virginica_stats = virginica.describe()
# print(virginica_stats)

virginica_sepal_length = iris_sepal_length[100:150]
virginica_sepal_width = iris_sepal_width[100:150]
virginica_petal_length = iris_petal_length[100:150]
virginica_petal_width = iris_petal_width[100:150]
x = range(0,50)

# plt.scatter(x, virginica_sepal_length, color = 'r')
# plt.scatter(x, versicolor_sepal_length, color = 'b')
# plt.scatter(x, setosa_sepal_length, color = 'y')
# plt.show()

# plt.scatter(x, virginica_sepal_width, color = 'r')
# plt.scatter(x, versicolor_sepal_width, color = 'b')
# plt.scatter(x, setosa_sepal_width, color = 'y')
# plt.show()

# plt.scatter(x, virginica_petal_width, color = 'r')
# plt.scatter(x, versicolor_petal_width, color = 'b')
# plt.scatter(x, setosa_petal_width, color = 'y')
# plt.show()

# plt.scatter(x, virginica_petal_width, color = 'r')
# plt.scatter(x, versicolor_petal_width, color = 'b')
# plt.scatter(x, setosa_petal_width, color = 'y')
# plt.show()

# creating multiple plots on the same window/page - https://chris35wills.github.io/courses/PythonPackages_matplotlib/matplotlib_multiple_figs/

fig = plt.figure()
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

ax1.scatter(virginica_sepal_width, virginica_sepal_length, color = 'r', label='virginica')
ax1.scatter(versicolor_sepal_width, versicolor_sepal_length, color = 'b', label='versicolor')
ax1.scatter(setosa_sepal_width, setosa_sepal_length, color = 'y', label='setosa')

ax2.scatter(virginica_petal_width, virginica_petal_length, color = 'r',label='virginica')
ax2.scatter(versicolor_petal_width, versicolor_petal_length, color = 'b', label='versicolor')
ax2.scatter(setosa_petal_width, setosa_petal_length, color = 'y', label='setosa')

ax1.set_title('Sepal')
ax1.set_xlabel('Width in cm')
ax1.set_ylabel('Length in cm')
plt.legend()

ax2.set_title('Petal')
ax2.set_xlabel('Width in cm')
ax2.set_ylabel('Length in cm')
plt.legend()
plt.show()