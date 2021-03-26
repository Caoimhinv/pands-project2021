# overview of the data - overall and by species
# Creating variables
# creating comparison scatter plots

# Author: Caoimhin Vallely

import pandas as pd
import matplotlib.pyplot as plt

# some borrowed from https://medium.com/@avulurivenkatasaireddy/exploratory-data-analysis-of-iris-data-set-using-python-823e54110d2d

iris = pd.read_csv("/Users/caoimhinvallely/Desktop/Programming/Programming2021/pands-project2021/irisDataset.csv")

# overview
# prints 3 rows
print(iris.head(3))
# prints columns titles
print("columns",iris.columns)
# prints the shape of the dataframe
print("shape:",iris.shape)
# prints the size of the dataframe
print("Size:",iris.size)
# decribes the dataframe - min/med/max, mean, SD
print(iris.describe())
# correlaton between elements
print(iris.corr())

# variables for each element
iris_sepal_length = iris['sepal_length']
iris_sepal_width = iris['sepal_width']
iris_petal_length = iris['petal_length']
iris_petal_width = iris['petal_width']
species = iris['species']

# creates a variable for the decribe dataframe
iris_stats = iris.describe()
# creates a variable for the correlation dataframe
iris_correlation = iris.corr()

# By species beginning with setosa
setosa = iris[0:50]
setosa_stats = setosa.describe()

setosa_sepal_length = iris_sepal_length[0:50]
setosa_sepal_width = iris_sepal_width[0:50]
setosa_petal_length = iris_petal_length[0:50]
setosa_petal_width = iris_petal_width[0:50]

# versicolor species overview
versicolor = iris[50:100]
versicolor_stats = versicolor.describe()

versicolor_sepal_length = iris_sepal_length[50:100]
versicolor_sepal_width = iris_sepal_width[50:100]
versicolor_petal_length = iris_petal_length[50:100]
versicolor_petal_width = iris_petal_width[50:100]

# virginica species overview
virginica = iris[100:150]
virginica_stats = virginica.describe()

virginica_sepal_length = iris_sepal_length[100:150]
virginica_sepal_width = iris_sepal_width[100:150]
virginica_petal_length = iris_petal_length[100:150]
virginica_petal_width = iris_petal_width[100:150]

# creating multiple plots on the same window/page - https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplots_demo.html

# Creating scatter plots for each combination of variables - 4 x 4
fig, axs = plt.subplots(4,4, sharex=True, sharey=True)

# this took a bit of messing! Ref: https://stackoverflow.com/questions/27016904/matplotlib-legends-in-subplot
l1 = axs[3,2].scatter(virginica_sepal_width, virginica_sepal_length, s=2, color = 'r',label='virginica')
l2 = axs[3,2].scatter(versicolor_sepal_width, versicolor_sepal_length, s=2, color = 'b', label='versicolor')
l3 = axs[3,2].scatter(setosa_sepal_width, setosa_sepal_length, s=2, color = 'y', label='setosa')

axs[0,0].set_title("Petal length (cm)", fontsize=6)
axs[0,0].set_ylabel('Petal lenth (cm)', fontsize=6)
axs[0,0].legend([l1, l2, l3],['versicolor', 'setosa', 'virginica'], loc='center', mode='expand', frameon=False, scatterpoints=3, markerscale=2)
# https://www.geeksforgeeks.org/matplotlib-pyplot-legend-in-python/
axs[0,1].scatter(virginica_petal_length, virginica_petal_width, s=2, color = 'r', label='virginica')
axs[0,1].scatter(versicolor_petal_length, versicolor_petal_width, s=2, color = 'b', label='versicolor')
axs[0,1].scatter(setosa_petal_length, setosa_petal_width, s=2, color = 'y', label='setosa')
axs[0,1].set_title("Petal width (cm)", fontsize=6)

axs[0,2].scatter(virginica_petal_length, virginica_sepal_length, s=2, color = 'r', label='virginica')
axs[0,2].scatter(versicolor_petal_length, versicolor_sepal_length, s=2, color = 'b', label='versicolor')
axs[0,2].scatter(setosa_petal_length, setosa_sepal_length, s=2, color = 'y', label='setosa')
axs[0,2].set_title("Sepal length (cm)", fontsize=6)

axs[0,3].scatter(virginica_petal_length, virginica_sepal_width, s=2, color = 'r', label='virginica')
axs[0,3].scatter(versicolor_petal_length, versicolor_sepal_width, s=2, color = 'b', label='versicolor')
axs[0,3].scatter(setosa_petal_length, setosa_sepal_width, s=2, color = 'y', label='setosa')
axs[0,3].set_title("Sepal width (cm)", fontsize=6)

axs[1,0].scatter(virginica_petal_width, virginica_petal_length, s=2, color = 'r',label='virginica')
axs[1,0].scatter(versicolor_petal_width, versicolor_petal_length, s=2, color = 'b', label='versicolor')
axs[1,0].scatter(setosa_petal_width, setosa_petal_length, s=2, color = 'y', label='setosa')
axs[1,0].set_ylabel('Petal width (cm)', fontsize=6)

axs[1,1].legend([l1, l2, l3],['versicolor', 'setosa', 'virginica'], loc='center', mode='expand', frameon=False, scatterpoints=3, markerscale=2)

axs[1,2].scatter(virginica_petal_width, virginica_sepal_length, s=2, color = 'r',label='virginica')
axs[1,2].scatter(versicolor_petal_width, versicolor_sepal_length, s=2, color = 'b', label='versicolor')
axs[1,2].scatter(setosa_petal_width, setosa_sepal_length, s=2, color = 'y', label='setosa')

axs[1,3].scatter(virginica_petal_width, virginica_sepal_width, s=2, color = 'r',label='virginica')
axs[1,3].scatter(versicolor_petal_width, versicolor_sepal_width, s=2, color = 'b', label='versicolor')
axs[1,3].scatter(setosa_petal_width, setosa_sepal_width, s=2, color = 'y', label='setosa')

axs[2,0].scatter(virginica_sepal_length, virginica_petal_length, s=2, color = 'r', label='virginica')
axs[2,0].scatter(versicolor_sepal_length, versicolor_petal_length, s=2, color = 'b', label='versicolor')
axs[2,0].scatter(setosa_sepal_length, setosa_petal_length, s=2, color = 'y', label='setosa')
axs[2,0].set_ylabel('Sepal length (cm)',fontsize=6)

axs[2,1].scatter(virginica_sepal_length, virginica_petal_width, s=2, color = 'r', label='virginica')
axs[2,1].scatter(versicolor_sepal_length, versicolor_petal_width, s=2, color = 'b', label='versicolor')
axs[2,1].scatter(setosa_sepal_length, setosa_petal_width, s=2, color = 'y', label='setosa')

axs[2,2].legend([l1, l2, l3],['versicolor', 'setosa', 'virginica'], loc='center', mode='expand', frameon=False, scatterpoints=3, markerscale=2)

axs[2,3].scatter(virginica_sepal_length, virginica_sepal_width, s=2, color = 'r', label='virginica')
axs[2,3].scatter(versicolor_sepal_length, versicolor_sepal_width, s=2, color = 'b', label='versicolor')
axs[2,3].scatter(setosa_sepal_length, setosa_sepal_width, s=2, color = 'y', label='setosa')

axs[3,0].scatter(virginica_sepal_width, virginica_petal_length, s=2, color = 'r',label='virginica')
axs[3,0].scatter(versicolor_sepal_width, versicolor_petal_length, s=2, color = 'b', label='versicolor')
axs[3,0].scatter(setosa_sepal_width, setosa_petal_length, s=2, color = 'y', label='setosa')
axs[3,0].set_ylabel("Sepal width (cm)", fontsize=6)
axs[3,0].set_xlabel("Petal length (cm)", fontsize=6)

axs[3,1].scatter(virginica_sepal_width, virginica_petal_width, s=2, color = 'r',label='virginica')
axs[3,1].scatter(versicolor_sepal_width, versicolor_petal_width, s=2, color = 'b', label='versicolor')
axs[3,1].scatter(setosa_sepal_width, setosa_petal_width, s=2, color = 'y', label='setosa')
axs[3,1].set_xlabel("Petal width (cm)", fontsize=6)

axs[3,2].scatter(virginica_sepal_width, virginica_sepal_length, s=2, color = 'r',label='virginica')
axs[3,2].scatter(versicolor_sepal_width, versicolor_sepal_length, s=2, color = 'b', label='versicolor')
axs[3,2].scatter(setosa_sepal_width, setosa_sepal_length, s=2, color = 'y', label='setosa')
axs[3,2].set_xlabel("Sepal length (cm)", fontsize=6)

axs[3,3].set_xlabel("Sepal width (cm)", fontsize=6)

axs[3,3].legend([l1, l2, l3],['versicolor', 'setosa', 'virginica'], loc='center', mode='expand', frameon=False, scatterpoints=3, markerscale=2)
# set main title - https://www.delftstack.com/howto/matplotlib/how-to-set-a-single-main-title-for-all-the-subplots-in-matplotlib/
plt.suptitle('Variable comparison scatterplots')
plt.show()
# https://stackabuse.com/how-to-set-axis-range-xlim-ylim-in-matplotlib/

# https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplot.html#sphx-glr-gallery-subplots-axes-and-figures-subplot-py


