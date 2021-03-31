# this is an analysis script for the Fisher iris dataset as part of 
# a project for the Programming and scripting module of HDIP in Data
# Analytics at GMIT (2021)

# Author: Caoimhin Vallely

# importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("darkgrid")

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

color_theme = ['yellowgreen','teal','tomato']

# creating scatter plots for each combination of variables petal,sepal length and width and vice versa.
# using subplot() so I can compare them side by side. 2 rows x 2 columns.
f, axes = plt.subplots(2, 2)
sns.scatterplot(data=iris, x='sepal_length', y='sepal_width', hue='species', palette=color_theme, ax=axes[0,0])
sns.scatterplot(data=iris, x='sepal_width', y='sepal_length', hue='species', palette=color_theme, ax=axes[0,1])
sns.scatterplot(data=iris, x='petal_length', y='petal_width', hue='species', palette=color_theme, ax=axes[1,0])
sns.scatterplot(data=iris, x='petal_width', y='petal_length', hue='species', palette=color_theme, ax=axes[1,1])

axes[0,0].set_xlabel("Sepal length (cm)", fontsize=7)
axes[0,0].set_ylabel("Sepal width (cm)", fontsize=7)
axes[0,1].set_xlabel("Sepal width (cm)", fontsize=7)
axes[0,1].set_ylabel("Sepal length (cm)", fontsize=7)
axes[1,0].set_xlabel("Petal length (cm)", fontsize=7)
axes[1,0].set_ylabel("Petal width (cm)", fontsize=7)
axes[1,1].set_xlabel("Petal width (cm)", fontsize=7)
axes[1,1].set_ylabel("Petal length (cm)", fontsize=7)
# set tick format
axes[0,0].tick_params(axis='both', which='major', labelsize=7)
axes[0,1].tick_params(axis='both', which='major', labelsize=7)
axes[1,0].tick_params(axis='both', which='major', labelsize=7)
axes[1,1].tick_params(axis='both', which='major', labelsize=7)

# set legends
axes[0,0].legend(fontsize=7, scatterpoints=3)
axes[0,1].legend(fontsize=7, scatterpoints=3)
axes[1,0].legend(fontsize=7, scatterpoints=3)
axes[1,1].legend(fontsize=7, scatterpoints=3)

plt.suptitle('Scatter plots for each pair of variables', fontsize=15, fontname='fantasy')

# creating histograms for distribution of each variable - sepal length and width, and petal length and width
# sets up 4 plots - 2x2.
fig, axes = plt.subplots(2,2)

sns.histplot(data=iris, x='sepal_length', binwidth=0.1, hue='species', multiple="stack", kde=True, palette=color_theme, ax=axes[0,0])
sns.histplot(data=iris, x='sepal_width', binwidth=0.1, hue='species', multiple="stack", kde=True, palette=color_theme, ax=axes[0,1])
sns.histplot(data=iris, x='petal_length', binwidth=0.1, hue='species', multiple="stack", kde=True, palette=color_theme, ax=axes[1,0])
sns.histplot(data=iris, x='petal_width', binwidth=0.1, hue='species', multiple="stack", kde=True, palette=color_theme, ax=axes[1,1])

axes[0,0].set_xlabel("Sepal length (cm)", fontsize=7)
axes[0,0].set_ylabel("Count", fontsize=7)
axes[0,1].set_xlabel("Sepal width (cm)", fontsize=7)
axes[0,1].set_ylabel("Count", fontsize=7)
axes[1,0].set_xlabel("Petal length (cm)", fontsize=7)
axes[1,0].set_ylabel("Count", fontsize=7)
axes[1,1].set_xlabel("Petal width (cm)", fontsize=7)
axes[1,1].set_ylabel("Count", fontsize=7)

# set tick format
axes[0,0].tick_params(axis='both', which='major', labelsize=7)
axes[0,1].tick_params(axis='both', which='major', labelsize=7)
axes[1,0].tick_params(axis='both', which='major', labelsize=7)
axes[1,1].tick_params(axis='both', which='major', labelsize=7)

plt.suptitle('Distribution histograms of each variable', fontsize=15, fontname='fantasy')
plt.show()

# creating a scatter matrix plot for all the variables

sns.pairplot(iris, hue="species", palette=color_theme)
plt.subplots_adjust(top=.95)
plt.suptitle('Matrix scatter plot', fontsize=15, fontname='fantasy')
plt.show()

# 2x2 grid of boxplots
f, axes = plt.subplots(2,2)
sns.boxplot(x = 'species', y='sepal_length', data = iris, ax=axes[0,0], palette=color_theme)
sns.boxplot(x = 'species', y='sepal_width', data = iris, ax=axes[0,1], palette=color_theme)
sns.boxplot(x = 'species', y='petal_length', data = iris, ax=axes[1,0], palette=color_theme)
sns.boxplot(x = 'species', y='petal_width', data = iris, ax=axes[1,1], palette=color_theme)
axes[0,0].set_xlabel("Species", fontsize=7)
axes[0,0].set_ylabel("Sepal Length (cm)", fontsize=7)
axes[0,1].set_xlabel("Species", fontsize=7)
axes[0,1].set_ylabel("Sepal Width (cm)", fontsize=7)
axes[1,0].set_xlabel("Species", fontsize=7)
axes[1,0].set_ylabel("Petal Length (cm)", fontsize=7)
axes[1,1].set_xlabel("Species", fontsize=7)
axes[1,1].set_ylabel("Petal Width (cm)", fontsize=7)

# format x,y labels
axes[0,0].tick_params(axis='both', which='major', labelsize=7)
axes[0,1].tick_params(axis='both', which='major', labelsize=7)
axes[1,0].tick_params(axis='both', which='major', labelsize=7)
axes[1,1].tick_params(axis='both', which='major', labelsize=7)

plt.suptitle('Boxplots', fontsize=15, fontname='fantasy')
plt.show()


# the same as violin plots
f, axes = plt.subplots(2,2)
sns.violinplot(x = 'species', y='sepal_length', data = iris, ax=axes[0,0], palette=color_theme)
sns.violinplot(x = 'species', y='sepal_width', data = iris, ax=axes[0,1], palette=color_theme)
sns.violinplot(x = 'species', y='petal_length', data = iris, ax=axes[1,0], palette=color_theme)
sns.violinplot(x = 'species', y='petal_width', data = iris, ax=axes[1,1], palette=color_theme)
axes[0,0].set_xlabel("Species", fontsize=7)
axes[0,0].set_ylabel("Sepal Length (cm)", fontsize=7)
axes[0,1].set_xlabel("Species", fontsize=7)
axes[0,1].set_ylabel("Sepal Width (cm)", fontsize=7)
axes[1,0].set_xlabel("Species", fontsize=7)
axes[1,0].set_ylabel("Petal Length (cm)", fontsize=7)
axes[1,1].set_xlabel("Species", fontsize=7)
axes[1,1].set_ylabel("Petal Width (cm)", fontsize=7)

# format x,y labels
axes[0,0].tick_params(axis='both', which='major', labelsize=7)
axes[0,1].tick_params(axis='both', which='major', labelsize=7)
axes[1,0].tick_params(axis='both', which='major', labelsize=7)
axes[1,1].tick_params(axis='both', which='major', labelsize=7)
# format x,y labels
axes[0,0].tick_params(axis='both', which='major', labelsize=7)
axes[0,1].tick_params(axis='both', which='major', labelsize=7)
axes[1,0].tick_params(axis='both', which='major', labelsize=7)
axes[1,1].tick_params(axis='both', which='major', labelsize=7)
plt.suptitle('Violin plots', fontsize=15, fontname='fantasy')
plt.show()

# violin plot stacked on a violin plot. Stingray!
f, axes = plt.subplots(2,2)
sns.violinplot(x = 'species', y='sepal_length', data = iris, ax=axes[0,0], palette=color_theme)
sns.violinplot(x = 'species', y='sepal_width', data = iris, ax=axes[0,1], palette=color_theme)
sns.violinplot(x = 'species', y='petal_length', data = iris, ax=axes[1,0], palette=color_theme)
sns.violinplot(x = 'species', y='petal_width', data = iris, ax=axes[1,1], palette=color_theme)
sns.swarmplot(x = 'species', y='sepal_length', data = iris, ax=axes[0,0], size=3, color='white', edgecolor='black', linewidth=.5)
sns.swarmplot(x = 'species', y='sepal_width', data = iris, ax=axes[0,1], size=3, color='white', edgecolor='black', linewidth=.5)
sns.swarmplot(x = 'species', y='petal_length', data = iris, ax=axes[1,0], size=3, color='white', edgecolor='black', linewidth=.5)
sns.swarmplot(x = 'species', y='petal_width', data = iris, ax=axes[1,1], size=3, color='white', edgecolor='black', linewidth=.5)
axes[0,0].set_xlabel("Species", fontsize=7)
axes[0,0].set_ylabel("Sepal Length (cm)", fontsize=7)
axes[0,1].set_xlabel("Species", fontsize=7)
axes[0,1].set_ylabel("Sepal Width (cm)", fontsize=7)
axes[1,0].set_xlabel("Species", fontsize=7)
axes[1,0].set_ylabel("Petal Length (cm)", fontsize=7)
axes[1,1].set_xlabel("Species", fontsize=7)
axes[1,1].set_ylabel("Petal Width (cm)", fontsize=7)

# format x,y labels
axes[0,0].tick_params(axis='both', which='major', labelsize=7)
axes[0,1].tick_params(axis='both', which='major', labelsize=7)
axes[1,0].tick_params(axis='both', which='major', labelsize=7)
axes[1,1].tick_params(axis='both', which='major', labelsize=7)

plt.suptitle('Swarm plot - scatterplot on violinplot', fontsize=15, fontname='fantasy')
plt.show()

# heat map based on correlation (all species)
iris_mx = iris.corr()
sns.heatmap(iris_mx, annot=True, cmap="cubehelix")
plt.suptitle('Heatmap of correlation', fontsize=15, fontname='fantasy')
plt.show()
