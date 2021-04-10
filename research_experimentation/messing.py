# few simple calculations on overall dataset
# Author: Caoimhin Vallely

import pandas as pd
import matplotlib.pyplot as plt
import csv

# overall overview
# some borrowed from https://medium.com/@avulurivenkatasaireddy/exploratory-data-analysis-of-iris-data-set-using-python-823e54110d2d
iris = pd.read_csv("/Users/caoimhinvallely/Desktop/Programming/Programming2021/pands-project2021/iris_dataset.csv")

# print("----------")
# print("Initial data parsing")
# print("----------")
# print("COUNT - entries per column\n", iris.count())
# print("----------")
# print("MAX - highest value per column\n", iris.max())
# print("----------")
# print("MIN - lowest value per column\n", iris.min())
# print("----------")
# print("MEAN - mean value per column\n", iris.mean())
# print("----------")
# print("MEDIAN - median value per column\n", iris.median())
# print("----------")
# print("MODE - mode value per column\n", iris.mode())
# print("----------")
# print("STD - standard deviation per column\n", iris.std())
# print("----------")
# print("HEAD - first five rows of the dataframe\n", iris.head())
# print("----------")
# print("COLUMN - column labels - \n",iris.columns)
# print("----------")
# print("SHAPE - number of rows and columns\n",iris.shape)
# print("----------")
# print("SIZE - number of entries\n",iris.size)
# print("----------")
# print("DESCRIBE - overall desrciption including most of the information from above", iris.describe())
# print("----------")
# print("INFO - more info on dataframe\n", iris.info())
# print("----------")

iris_sepal_length = iris['sepal_length']
iris_sepal_width = iris['sepal_width']
iris_petal_length = iris['petal_length']
iris_petal_width = iris['petal_width']
species = iris['species']

# iris_stats = iris.describe()
# # print(iris_stats)
# iris_correlation = iris.corr()
# # print(iris_correlation)

# # setosa species overview
# setosa = iris[0:50]
# setosa_stats = setosa.describe()
# # print(setosa_stats)

# setosa_sepal_length = iris_sepal_length[0:50]
# setosa_sepal_width = iris_sepal_width[0:50]
# setosa_petal_length = iris_petal_length[0:50]
# setosa_petal_width = iris_petal_width[0:50]

# # versicolor species overview
# versicolor = iris[50:100]
# versicolor_stats = versicolor.describe()
# # print(versicolor_stats)

# versicolor_sepal_length = iris_sepal_length[50:100]
# versicolor_sepal_width = iris_sepal_width[50:100]
# versicolor_petal_length = iris_petal_length[50:100]
# versicolor_petal_width = iris_petal_width[50:100]

# # virginica species overview
# virginica = iris[100:150]
# virginica_stats = virginica.describe()
# # print(virginica_stats)

# virginica_sepal_length = iris_sepal_length[100:150]
# virginica_sepal_width = iris_sepal_width[100:150]
# virginica_petal_length = iris_petal_length[100:150]
# virginica_petal_width = iris_petal_width[100:150]
# x = range(0,50)

# # plt.scatter(x, virginica_sepal_length, color = 'r')
# # plt.scatter(x, versicolor_sepal_length, color = 'b')
# # plt.scatter(x, setosa_sepal_length, color = 'y')
# # plt.show()

# # plt.scatter(x, virginica_sepal_width, color = 'r')
# # plt.scatter(x, versicolor_sepal_width, color = 'b')
# # plt.scatter(x, setosa_sepal_width, color = 'y')
# # plt.show()

# # plt.scatter(x, virginica_petal_width, color = 'r')
# # plt.scatter(x, versicolor_petal_width, color = 'b')
# # plt.scatter(x, setosa_petal_width, color = 'y')
# # plt.show()

# # plt.scatter(x, virginica_petal_width, color = 'r')
# # plt.scatter(x, versicolor_petal_width, color = 'b')
# # plt.scatter(x, setosa_petal_width, color = 'y')
# # plt.show()

# # creating multiple plots on the same window/page - https://chris35wills.github.io/courses/PythonPackages_matplotlib/matplotlib_multiple_figs/

# fig = plt.figure()
# ax1 = fig.add_subplot(121)
# ax2 = fig.add_subplot(122)

# ax1.scatter(virginica_sepal_width, virginica_sepal_length, color = 'r', label='virginica')
# ax1.scatter(versicolor_sepal_width, versicolor_sepal_length, color = 'b', label='versicolor')
# ax1.scatter(setosa_sepal_width, setosa_sepal_length, color = 'y', label='setosa')

# ax2.scatter(virginica_petal_width, virginica_petal_length, color = 'r',label='virginica')
# ax2.scatter(versicolor_petal_width, versicolor_petal_length, color = 'b', label='versicolor')
# ax2.scatter(setosa_petal_width, setosa_petal_length, color = 'y', label='setosa')

# ax1.set_title('Sepal')
# ax1.set_xlabel('Width in cm')
# ax1.set_ylabel('Length in cm')
# plt.legend()

# ax2.set_title('Petal')
# ax2.set_xlabel('Width in cm')
# ax2.set_ylabel('Length in cm')
# plt.legend()
# # plt.show()

cols = iris.columns
# # it will print the list of column names.
# print(cols)
  
# # we will take that columns which have integer values.
# cols = cols[0:5]
original_columns = iris[cols[0:5]]
iris["totals"] = original_columns.sum(axis=1)
iris["mean"] = original_columns.mean(axis=1)

# setosa = iris.loc[iris["species"] == "setosa"]
# versicolor = iris.loc[iris["species"] == "versicolor"]
# virginica = iris.loc[iris["species"] == "virginica"]

# print(setosa.head())
# print(versicolor.head())
# print(virginica.head())

# print(setosa[["totals"]].mean())
# print(versicolor[["totals"]].mean())
# print(virginica[["totals"]].mean())

# print(setosa[["totals"]].std())
# print(versicolor[["totals"]].std())
# print(virginica[["totals"]].std())

# # print(setosa[["totals"]].var())
# # print(versicolor[["totals"]].var())
# # print(virginica[["totals"]].var())
# # iris.round(decimals=1)
# # iris.to_csv('iris_dataset_with_totals.csv')
# # print(iris.describe())
# # print(iris.head())
totals = iris[["totals"]]
print (totals)  
print(iris.head(10))
iris.to_csv('itest.csv', float_format='%.2f')

# # print(setosa.describe())
# # print(versicolor.describe())
# # print(virginica.describe())

# # print(iris.isnull())
# # print(iris["species"].value_counts())

# # print(setosa_totals.var())
# # print(versicolor_totals.var())
# # print(virginica_totals.var())

import csv

nms = [[1, 2, 3], [7, 8, 9], [10, 11, 12]]

f = open('numbers3.csv', 'w')

with f:

    writer = csv.writer(f)
    writer.writerows(nms)