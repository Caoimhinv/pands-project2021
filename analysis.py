# this is an analysis script for the Fisher iris dataset as part of 
# a project for the Programming and scripting module of HDIP in Data
# Analytics at GMIT (2021)

# Author: Caoimhin Vallely

# importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# reads in the dataframe
iris = pd.read_csv("/Users/caoimhinvallely/Desktop/Programming/Programming2021/pands-project2021/iris_dataset.csv")

# this is an initial exploration of the data using all the conventional methods that pandas has to offer
print("----------")
print("Initial data exploration")
print("----------")
print("COUNT() - entries per column\n", iris.count())
print("----------")
print("MAX() - highest value per column\n", iris.max())
print("----------")
print("MIN() - lowest value per column\n", iris.min())
print("----------")
print("MEAN() - mean value per column\n", iris.mean())
print("----------")
print("MEDIAN() - median value per column\n", iris.median())
print("----------")
print("MODE() - mode value per column\n", iris.mode())
print("----------")
print("STD() - standard deviation per column\n", iris.std())
print("----------")
print("HEAD() - first five rows of the dataframe\n", iris.head())
print("----------")
print("COLUMNS() - column labels - \n",iris.columns)
print("----------")
print("SHAPE() - number of rows and columns\n",iris.shape)
print("----------")
print("SIZE() - number of entries\n",iris.size)
print("----------")
# in reality, this finds most of the above on it's own!
print("DESCRIBE() - overview of the dataframe\n", iris.describe())
print("----------")
print("INFO() - further info on dataframe")
print(iris.info())
print("----------")
print("CORR() - correlation among the data\n", iris.corr())
print("----------")

# creating variables for each element - petal length and width, and sepal length and width
iris_sepal_length = iris['sepal_length']
iris_sepal_width = iris['sepal_width']
iris_petal_length = iris['petal_length']
iris_petal_width = iris['petal_width']

# creating variables for each species and each element within species
# - petal length and width, and sepal length and width
# setosa
setosa = iris[0:50]
setosa_sepal_l = setosa['sepal_length']
setosa_sepal_w = setosa['sepal_width']
setosa_petal_l = setosa['petal_length']
setosa_petal_w = setosa['petal_width']

# versicolor
versicolor = iris[50:100]
versicolor_sepal_l = versicolor['sepal_length']
versicolor_sepal_w = versicolor['sepal_width']
versicolor_petal_l = versicolor['petal_length']
versicolor_petal_w = versicolor['petal_width']

# virginica
virginica = iris[100:150]
virginica_sepal_l = virginica['sepal_length']
virginica_sepal_w = virginica['sepal_width']
virginica_petal_l = virginica['petal_length']
virginica_petal_w = virginica['petal_width']

# creating scatter plots for each combination of variables petal,sepal length and width and vice versa.
# using subplot() so I can compare them side by side. 2 rows x 2 columns.
fig, axs = plt.subplots(2, 2)

# ax1. They are layed out in the form [0,0] where the first number represents the row and the second the column
axs[0,0].scatter(setosa_sepal_l, setosa_sepal_w, s=12, marker='o', color = 'yellowgreen', label='setosa')
axs[0,0].scatter(versicolor_sepal_l, versicolor_sepal_w, s=12, marker='s', color = 'teal', label='versicolor')
axs[0,0].scatter(virginica_sepal_l, virginica_sepal_w, s=12, marker='D', color = 'tomato', label='virginica')
axs[0,0].set_xlabel("sepal length (cm)", fontsize=6)
axs[0,0].set_ylabel("sepal width (cm)", fontsize=6)
axs[0,0].legend(fontsize=6, scatterpoints=3)
axs[0,0].tick_params(axis='both', which='major', labelsize=6)
axs[0,0].grid(color='grey', linestyle=':', linewidth=0.5)
axs[0,0].set_title("sepal length v width", fontsize=9, loc='left')

axs[0,1].scatter(setosa_sepal_w, setosa_sepal_l, s=12, marker='o', color = 'yellowgreen', label='setosa')
axs[0,1].scatter(versicolor_sepal_w, versicolor_sepal_l, s=12, marker='s', color ='teal', label='versicolor')
axs[0,1].scatter(virginica_sepal_w, virginica_sepal_l, s=12, marker='D', color = 'tomato', label='virginica')
axs[0,1].legend(fontsize=6, scatterpoints=3)
axs[0,1].grid(color='grey', linestyle=':', linewidth=0.5)
axs[0,1].tick_params(axis='both', which='major', labelsize=6)
axs[0,1].set_xlabel("sepal width (cm)", fontsize=6)
axs[0,1].set_ylabel("sepal length (cm)", fontsize=6)
axs[0,1].set_title("sepal width v length", fontsize=9, loc='right')

axs[1,0].scatter(setosa_petal_l, setosa_petal_w, s=12, marker='o', color = 'yellowgreen', label='setosa')
axs[1,0].scatter(versicolor_petal_l, versicolor_petal_w, s=12, marker='s', color = 'teal', label='versicolor')
axs[1,0].scatter(virginica_petal_l, virginica_petal_w, s=12, marker='D', color = 'tomato', label='virginica')
axs[1,0].legend(fontsize=6, scatterpoints=3)
axs[1,0].grid(color='grey', linestyle=':', linewidth=0.5)
axs[1,0].tick_params(axis='both', which='major', labelsize=6)
axs[1,0].set_xlabel("petal length (cm)", fontsize=6)
axs[1,0].set_ylabel("petal width (cm)", fontsize=6)
axs[1,0].set_title("petal length v width", fontsize=9, loc='left')

axs[1,1].scatter(setosa_petal_w, setosa_petal_l, s=12, marker='o', color = 'yellowgreen', label='setosa')
axs[1,1].scatter(versicolor_petal_w, versicolor_petal_l, s=12, marker='s', color = 'teal', label='versicolor')
axs[1,1].scatter(virginica_petal_w, virginica_petal_l, s=12, marker='D', color = 'tomato',label='virginica')
axs[1,1].legend(fontsize=6, scatterpoints=3)
axs[1,1].tick_params(axis='both', which='major', labelsize=6)
axs[1,1].grid(color='grey', linestyle=':', linewidth=0.5)
axs[1,1].set_xlabel("petal width (cm)", fontsize=6)
axs[1,1].set_ylabel("petal length (cm)", fontsize=6)
axs[1,1].set_title("petal width v length", fontsize=9, loc='right')

# set main title
plt.suptitle('Scatter plots for each pair of variables', fontsize=15, fontname='fantasy')
plt.show()

# creating histograms for distribution of each variable - sepal length and width, and petal length and width
# sets up 4 plots - 2x2.
fig, axs = plt.subplots(2,2)

axs[0,0].hist(setosa_petal_l, bins=35, color = 'yellowgreen', label='setosa')
axs[0,0].hist(versicolor_petal_l, bins=35, color = 'teal', label='varsicolor')
axs[0,0].hist(virginica_petal_l, bins=35, color = 'tomato', label='virginica')
axs[0,0].set_ylabel("frequency", fontsize=8)
axs[0,0].set_xlabel("petal length (cm)", fontsize=8)
axs[0,0].legend(frameon=False, fontsize=6)
axs[0,0].tick_params(axis='both', which='both', labelsize=4)

axs[0,1].hist(setosa_petal_w, bins=35, color = 'yellowgreen', label='setosa')
axs[0,1].hist(versicolor_petal_w, bins=35, color = 'teal', label='varsicolor')
axs[0,1].hist(virginica_petal_w, bins=35, color = 'tomato', label='virginica')
axs[0,1].set_xlabel("petal width (cm)", fontsize=8)
axs[0,1].legend(frameon=False, fontsize=6)
axs[0,1].tick_params(axis='both', which='both', labelsize=4)

axs[1,0].hist(setosa_sepal_l, bins=35, color = 'yellowgreen', label='setosa')
axs[1,0].hist(versicolor_sepal_l, bins=35, color = 'teal', label='varsicolor')
axs[1,0].hist(virginica_sepal_l, bins=35, color = 'tomato', label='virginica')
axs[1,0].set_ylabel("frequency", fontsize=7)
axs[1,0].set_xlabel("sepal length (cm)", fontsize=8)
axs[1,0].legend(frameon=False, fontsize=6)
axs[1,0].tick_params(axis='both', which='both', labelsize=4)

axs[1,1].hist(setosa_sepal_w, bins=35, color = 'yellowgreen', label='setosa')
axs[1,1].hist(versicolor_sepal_w, bins=35, color = 'teal', label='varsicolor')
axs[1,1].hist(virginica_sepal_w, bins=35, color = 'tomato', label='virginica')
axs[1,1].set_xlabel("sepal width (cm)", fontsize=8)
axs[1,1].legend(frameon=False, fontsize=6)
axs[1,1].tick_params(axis='both', which='both', labelsize=4)

plt.suptitle('Distribution histogram of each variable', fontsize=15, fontname='fantasy')
plt.show()

# creating a scatter matrix plot for all the variables

sns.pairplot(iris, hue="species",markers=["o", "s", "D"], palette=['yellowgreen','teal','tomato'])
plt.suptitle('Matrix scatter plot', fontsize=15, fontname='fantasy')
plt.show()