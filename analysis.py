# this is an analysis script for the Fisher iris dataset as part of 
# a project for the Programming and scripting module of HDIP in Data
# Analytics at GMIT (2021)

# Author: Caoimhin Vallely

# importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

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

# creating scatter plots for each combination of variablea
# there are 16 variables, but subracting the 4 where it's not necesary to compare
# a variable to itself, that leaves 12

# using subplot() so I can compare them all side by side. 4 rows x 3 columns.
# I'm sharing the attributes for all of the axes (sharex and sharey)
fig, axs = plt.subplots(4, 3)

# ax1. They are layed out in the form [0,0] where the first number represents the row and the second the column
# I'm only including titles at the top and bottom, and on the left axes, just to avoid clutter.

axs[0,0].scatter(virginica_sepal_l, virginica_sepal_w, s=2, color = 'r', label='virginica S.L. v virginica S.W.')
axs[0,0].scatter(versicolor_sepal_l, versicolor_sepal_w, s=2, color = 'b', label='versicolor S.L. v versicolor S.W.')
axs[0,0].scatter(setosa_sepal_l, setosa_sepal_w, s=2, color = 'y', label='setosa S.L. v setosa S.W.')
axs[0,0].set_ylabel("sepal length\n (cm)", fontsize=8)
axs[0,0].legend(fontsize=6, loc='upper center', scatterpoints=3)
# axs[0,0].set_xticks([0,1,2,3,4,5,6,7,8])
# axs[0,0].set_yticks([0,1,2,3,4,5,6,7,8])
axs[0,0].tick_params(axis='both', which='major', labelsize=6)
axs[0,0].grid(color='grey', linestyle=':', linewidth=0.5)

axs[0,1].scatter(virginica_sepal_l, virginica_petal_l, s=2, color = 'r', label='virginica S.L v virginica P.L.')
axs[0,1].scatter(versicolor_sepal_l, versicolor_petal_l, s=2, color = 'b', label='versicolor S.L v versicolor P.L.')
axs[0,1].scatter(setosa_sepal_l, setosa_petal_l, s=2, color = 'y', label='setosa S.L v setosa P.L.')
axs[0,1].legend(fontsize=6, loc='lower right', scatterpoints=3)
axs[0,1].grid(color='grey', linestyle=':', linewidth=0.5)
axs[0,1].tick_params(axis='both', which='major', labelsize=6)

axs[0,2].scatter(virginica_sepal_l, virginica_petal_w, s=2, color = 'r', label='virginica S.L v virginica P.W.')
axs[0,2].scatter(versicolor_sepal_l, versicolor_petal_w, s=2, color = 'b', label='versicolor S.L v versicolor P.W.')
axs[0,2].scatter(setosa_sepal_l, setosa_petal_w, s=2, color = 'y', label='setosa S.L v setosa P.W.')
axs[0,2].legend(fontsize=6, loc='lower right', scatterpoints=3)
axs[0,2].grid(color='grey', linestyle=':', linewidth=0.5)
axs[0,2].tick_params(axis='both', which='major', labelsize=6)

axs[1,0].scatter(virginica_sepal_w, virginica_sepal_l, s=2, color = 'r',label='virginica S.W. v virginica S.L')
axs[1,0].scatter(versicolor_sepal_w, versicolor_sepal_l, s=2, color = 'b', label='versicolor S.W. v versicolor S.L')
axs[1,0].scatter(setosa_sepal_w, setosa_sepal_l, s=2, color = 'y', label='setosa S.W. v setosa S.L')
axs[1,0].set_ylabel("sepal width\n (cm)", fontsize=8)
axs[1,0].legend(fontsize=6, loc='lower right', scatterpoints=3)
axs[1,0].tick_params(axis='both', which='major', labelsize=6)
axs[1,0].grid(color='grey', linestyle=':', linewidth=0.5)

axs[1,1].scatter(virginica_sepal_w, virginica_petal_l, s=2, color = 'r',label='virginica S.W. v virginica P.L.')
axs[1,1].scatter(versicolor_sepal_w, versicolor_petal_l, s=2, color = 'b', label='versicolor S.W. v versicolor P.L.')
axs[1,1].scatter(setosa_sepal_w, setosa_petal_l, s=2, color = 'y', label='setosa S.W. v setosa P.L.')
axs[1,1].legend(fontsize=6, loc='center right', scatterpoints=3)
axs[1,1].grid(color='grey', linestyle=':', linewidth=0.5)
axs[1,1].tick_params(axis='both', which='major', labelsize=6)

axs[1,2].scatter(virginica_sepal_w, virginica_petal_w, s=2, color = 'r',label='virginica S.W. v virginica P.W.')
axs[1,2].scatter(versicolor_sepal_w, versicolor_petal_w, s=2, color = 'b', label='versicolor S.W. v versicolor P.W.')
axs[1,2].scatter(setosa_sepal_w, setosa_petal_w, s=2, color = 'y', label='setosa S.W. v setosa P.W.')
axs[1,2].legend(fontsize=6, loc='upper right', scatterpoints=3)
axs[1,2].grid(color='grey', linestyle=':', linewidth=0.5)
axs[1,2].tick_params(axis='both', which='major', labelsize=6)

axs[2,0].scatter(virginica_petal_l, virginica_sepal_l, s=2, color = 'r', label='virginica P.L. v virginica S.L')
axs[2,0].scatter(versicolor_petal_l, versicolor_sepal_l, s=2, color = 'b', label='versicolor P.L. v versicolor S.L')
axs[2,0].scatter(setosa_petal_l, setosa_sepal_l, s=2, color = 'y', label='setosa P.L. v setosa S.L')
axs[2,0].set_ylabel("petal length\n (cm)", fontsize=8)
axs[2,0].legend(fontsize=6, loc='upper left', scatterpoints=3)
axs[2,0].tick_params(axis='both', which='major', labelsize=6)
axs[2,0].grid(color='grey', linestyle=':', linewidth=0.5)

axs[2,1].scatter(virginica_petal_l, virginica_sepal_w, s=2, color = 'r', label='virginica P.L. v virginica S.W.')
axs[2,1].scatter(versicolor_petal_l, versicolor_sepal_w, s=2, color = 'b', label='versicolor P.L. v versicolor S.W.')
axs[2,1].scatter(setosa_petal_l, setosa_sepal_w, s=2, color = 'y', label='setosa P.L. v setosa S.W.')
axs[2,1].legend(fontsize=6, loc='upper right', scatterpoints=3)
axs[2,1].grid(color='grey', linestyle=':', linewidth=0.5)
axs[2,1].tick_params(axis='both', which='major', labelsize=6)

axs[2,2].scatter(virginica_petal_l, virginica_petal_w, s=2, color = 'r', label='virginica P.L. v virginica P.W.')
axs[2,2].scatter(versicolor_petal_l, versicolor_petal_w, s=2, color = 'b', label='versicolor P.L. v versicolor P.W.')
axs[2,2].scatter(setosa_petal_l, setosa_petal_w, s=2, color = 'y', label='setosa P.L. v setosa P.W.')
axs[2,2].legend(fontsize=6, loc='upper left', scatterpoints=3)
axs[2,2].grid(color='grey', linestyle=':', linewidth=0.5)
axs[2,2].tick_params(axis='both', which='major', labelsize=6)

axs[3,0].scatter(virginica_petal_w, virginica_sepal_l, s=2, color = 'r',label='virginica P.W. v virginica S.L')
axs[3,0].scatter(versicolor_petal_w, versicolor_sepal_l, s=2, color = 'b', label='versicolor P.W. v versicolor S.L')
axs[3,0].scatter(setosa_petal_w, setosa_sepal_l, s=2, color = 'y', label='setosa P.W. v setosa S.L')
axs[3,0].set_ylabel('petal width\n (cm)', fontsize=8)
axs[3,0].set_xlabel('(cm)', fontsize=8)
axs[3,0].legend(fontsize=6, loc='upper left', scatterpoints=3)
axs[3,0].tick_params(axis='both', which='major', labelsize=6)
axs[3,0].grid(color='grey', linestyle=':', linewidth=0.5)

axs[3,1].scatter(virginica_petal_w, virginica_sepal_w, s=2, color = 'r',label='virginica P.W. v virginica S.W.')
axs[3,1].scatter(versicolor_petal_w, versicolor_sepal_w, s=2, color = 'b', label='versicolor P.W. v versicolor S.W.')
axs[3,1].scatter(setosa_petal_w, setosa_sepal_w, s=2, color = 'y', label='setosa P.W. v setosa S.W.')
axs[3,1].legend(fontsize=6, loc='upper right', scatterpoints=3)
axs[3,1].grid(color='grey', linestyle=':', linewidth=0.5)
axs[3,1].tick_params(axis='both', which='major', labelsize=6)
axs[3,1].set_xlabel('(cm)', fontsize=8)

axs[3,2].scatter(virginica_petal_w, virginica_petal_l, s=2, color = 'r',label='virginica P.W. v virginica P.L.')
axs[3,2].scatter(versicolor_petal_w, versicolor_petal_l, s=2, color = 'b', label='versicolor P.W. v versicolor P.L.')
axs[3,2].scatter(setosa_petal_w, setosa_petal_l, s=2, color = 'y', label='setosa P.W. v setosa P.L.')
axs[3,2].legend(fontsize=6, loc='upper left', scatterpoints=3)
axs[3,2].grid(color='grey', linestyle=':', linewidth=0.5)
axs[3,2].tick_params(axis='both', which='major', labelsize=6)
axs[3,2].set_xlabel('(cm)', fontsize=8)

# set main title
plt.suptitle('Scatter plots for each pair of variables', fontsize=15, fontname='fantasy')
# plt.show()

# creating histograms for distribution of each variable - sepal length and width, and petal length and width

# sets up 4 plots - 2x2. All sharing the same x and y
fig, axs = plt.subplots(2,2)

axs[0,0].hist(setosa_petal_l, bins=35, color = 'y', label='setosa')
axs[0,0].hist(versicolor_petal_l, bins=35, color = 'b', label='varsicolor')
axs[0,0].hist(virginica_petal_l, bins=35, color = 'r', label='virginica')
axs[0,0].set_ylabel("Frequency", fontsize=8)
axs[0,0].set_xlabel("Petal length (cm)", fontsize=8)
axs[0,0].legend(frameon=False, fontsize=6)
axs[0,0].tick_params(axis='both', which='major', labelsize=4)

axs[0,1].hist(setosa_petal_w, bins=35, color = 'y', label='setosa')
axs[0,1].hist(versicolor_petal_w, bins=35, color = 'b', label='varsicolor')
axs[0,1].hist(virginica_petal_w, bins=35, color = 'r', label='virginica')
axs[0,1].set_xlabel("Petal width (cm)", fontsize=8)
axs[0,1].legend(frameon=False, fontsize=6)
axs[0,1].tick_params(axis='both', which='major', labelsize=4)

axs[1,0].hist(setosa_sepal_l, bins=35, color = 'y', label='setosa')
axs[1,0].hist(versicolor_sepal_l, bins=35, color = 'b', label='varsicolor')
axs[1,0].hist(virginica_sepal_l, bins=35, color = 'r', label='virginica')
axs[1,0].set_ylabel("Frequency", fontsize=7)
axs[1,0].set_xlabel("Sepal length (cm)", fontsize=8)
axs[1,0].legend(frameon=False, fontsize=6)
axs[1,0].tick_params(axis='both', which='major', labelsize=4)

axs[1,1].hist(setosa_sepal_w, bins=35, color = 'y', label='setosa')
axs[1,1].hist(versicolor_sepal_w, bins=35, color = 'b', label='varsicolor')
axs[1,1].hist(virginica_sepal_w, bins=35, color = 'r', label='virginica')
axs[1,1].set_xlabel("Sepal width (cm)", fontsize=8)
axs[1,1].legend(frameon=False, fontsize=6)
axs[1,1].tick_params(axis='both', which='major', labelsize=4)

plt.suptitle('Distribution of each variable', fontsize=15, fontname='fantasy')
plt.show()