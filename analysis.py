# this is an analysis script on Fisher's iris dataset as part of 
# a project for the Programming and scripting module of HDIP in Data
# Analytics at GMIT (2021)

# Author: Caoimhin Vallely

# importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# sets background style, and colour palette for all the plots
sns.set_style("darkgrid")
color_theme1 = ['yellowgreen','teal','tomato']
color_theme2 = ['yellowgreen','teal','tomato', 'plum']

# reads in the dataframe
iris = pd.read_csv("/Users/caoimhinvallely/Desktop/Programming/Programming2021/pands-project2021/iris_dataset.csv")

# this is an initial exploration of the data using all the conventional methods that pandas has to offer
I1 = ("----------\nInitial data exploration\n----------\n")
I2 = ("SIZE() - the total number of entries in the dataset:\n" + str(iris.size) + "\n----------\n")
I3 = ("SHAPE() - the number of rows and columns:\n" + str(iris.shape) + "\n----------\n")
I4 = ("COLUMNS() - these are the column labels and the data type:\n" + str(iris.columns) + "\n----------\n")
I5 = ("HEAD() - this is a printout of the first five rows of the dataset:\n" + str(iris.head()) + "\n----------\n")
I6 = ("TAIL() - this is a printout of the last five rows of the dataset:\n" + str(iris.tail()) + "\n----------\n")
I7 = ("SAMPLE() - this is a printout of a random five rows of the dataset:\n" + str(iris.sample(5)) + "\n----------\n")
I8 = ("DESCRIBE() - this is a statistical overview of the dataset:\n" + str(iris.describe()) + "\n----------\n")
I9 = ("GROUPBY.DESCRIBE() - this is an overview of the dataset by species:\n" + str(iris.groupby('species').describe()) + "\n----------\n")
I10 = "As this doesn't fit very clearly onto the page because of the 32 columns,\nthe following separates each out individually:\n\n"
I11 = "--setosa--\n" + str(iris.loc[iris['species'] == "setosa"].describe()) + "\n\n"
I12 = "--versicolor--\n" + str(iris.loc[iris['species'] == "versicolor"].describe()) + "\n\n"
I13 = "--virginica--\n" + str(iris.loc[iris['species'] == "virginica"].describe()) + "\n"

# prints all of the above info to a text file - iris_data.txt
with open('outputted_iris_data_textfile.txt','w') as d_a:
    d_a.writelines([I1, I2, I3, I4, I5, I6, I7, I8, I9, I10, I11, I12, I13])

# boxplot of all elements
b = sns.boxplot(data=iris, linewidth=0.5, fliersize=3, palette=color_theme2)
plt.tick_params(axis='both', which='major', labelsize=7)
b.set_ylabel("(cm)", fontsize=7, fontname='fantasy')
plt.suptitle('Boxplot (all irises)', fontsize=15, fontname='fantasy')
plt.show()

# boxplot grid of separating out each species
# this produces a 2x2 grid of boxplots
f, axes = plt.subplots(2,2)
sns.boxplot(x = 'species', y='sepal_length', data = iris, ax=axes[0,0], fliersize=3, linewidth=0.5, palette=color_theme1)
sns.boxplot(x = 'species', y='sepal_width', data = iris, ax=axes[0,1], fliersize=3, linewidth=0.5, palette=color_theme1)
sns.boxplot(x = 'species', y='petal_length', data = iris, ax=axes[1,0], fliersize=3, linewidth=0.5, palette=color_theme1)
sns.boxplot(x = 'species', y='petal_width', data = iris, ax=axes[1,1], fliersize=3, linewidth=0.5, palette=color_theme1)
axes[0,0].set_xlabel(" ", fontsize=7)
axes[0,0].set_ylabel("sepal_length (cm)", fontsize=7, fontname='fantasy')
axes[0,1].set_xlabel(" ", fontsize=7)
axes[0,1].set_ylabel("sepal_width (cm)", fontsize=7, fontname='fantasy')
axes[1,0].set_xlabel(" ", fontsize=7)
axes[1,0].set_ylabel("petal_Length (cm)", fontsize=7, fontname='fantasy')
axes[1,1].set_xlabel(" ", fontsize=7)
axes[1,1].set_ylabel("petal_width (cm)", fontsize=7, fontname='fantasy')

# format x,y labels
axes[0,0].tick_params(axis='both', which='major', labelsize=6)
axes[0,1].tick_params(axis='both', which='major', labelsize=6)
axes[1,0].tick_params(axis='both', which='major', labelsize=6)
axes[1,1].tick_params(axis='both', which='major', labelsize=6)

plt.suptitle('Boxplots (species separated)', fontsize=15, fontname='fantasy')
plt.show() 

# creating violin plots
# firstly with all irises
b = sns.violinplot(data=iris, linewidth=0.5, fliersize=3, palette=color_theme2)
plt.tick_params(axis='both', which='major', labelsize=7)
b.set_ylabel("(cm)", fontsize=7, fontname='fantasy')
plt.suptitle('Violinplot (all irises)', fontsize=15, fontname='fantasy')
plt.show()

# then each class separated out. violin plot stacked on a violin plot. Stingray!
f, axes = plt.subplots(2,2)
sns.violinplot(x = 'species', y='sepal_length', data = iris, ax=axes[0,0], linewidth=0.5, palette=color_theme1)
sns.violinplot(x = 'species', y='sepal_width', data = iris, ax=axes[0,1], linewidth=0.5, palette=color_theme1)
sns.violinplot(x = 'species', y='petal_length', data = iris, ax=axes[1,0], linewidth=0.5, palette=color_theme1)
sns.violinplot(x = 'species', y='petal_width', data = iris, ax=axes[1,1], linewidth=0.5, palette=color_theme1)
sns.swarmplot(x = 'species', y='sepal_length', data = iris, ax=axes[0,0], size=2, color='white', edgecolor='black', linewidth=.5)
sns.swarmplot(x = 'species', y='sepal_width', data = iris, ax=axes[0,1], size=2, color='white', edgecolor='black', linewidth=.5)
sns.swarmplot(x = 'species', y='petal_length', data = iris, ax=axes[1,0], size=2, color='white', edgecolor='black', linewidth=.5)
sns.swarmplot(x = 'species', y='petal_width', data = iris, ax=axes[1,1], size=2, color='white', edgecolor='black', linewidth=.5)
axes[0,0].set_xlabel(" ", fontsize=7)
axes[0,0].set_ylabel("sepal_length (cm)", fontsize=7, fontname='fantasy')
axes[0,1].set_xlabel(" ", fontsize=7)
axes[0,1].set_ylabel("sepal_width (cm)", fontsize=7, fontname='fantasy')
axes[1,0].set_xlabel(" ", fontsize=7)
axes[1,0].set_ylabel("petal_length (cm)", fontsize=7, fontname='fantasy')
axes[1,1].set_xlabel(" ", fontsize=7)
axes[1,1].set_ylabel("petal_width (cm)", fontsize=7, fontname='fantasy')

# format x,y labels
axes[0,0].tick_params(axis='both', which='major', labelsize=6)
axes[0,1].tick_params(axis='both', which='major', labelsize=6)
axes[1,0].tick_params(axis='both', which='major', labelsize=6)
axes[1,1].tick_params(axis='both', which='major', labelsize=6)

plt.suptitle('Swarm plots (species separated and data points scattered)', fontsize=13, fontname='fantasy')
plt.show()

# creating histograms
# setting up a grid of 4 histograms to show distribution of each variable
# sets up 4 plots - 2x2.
fig, axes = plt.subplots(2,2)

SP1 = sns.histplot(data=iris, x='sepal_length', binwidth=0.1, hue='species', kde=True, palette=color_theme1, alpha=0.5, legend=False, ax=axes[0,0])
SP2 = sns.histplot(data=iris, x='sepal_width', binwidth=0.1, hue='species', kde=True, palette=color_theme1, alpha=0.5, legend=False, ax=axes[0,1])
SP3 = sns.histplot(data=iris, x='petal_length', binwidth=0.1, hue='species', kde=True, palette=color_theme1, alpha=0.5, legend=False, ax=axes[1,0])
SP4 = sns.histplot(data=iris, x='petal_width', binwidth=0.1, hue='species', kde=True, palette=color_theme1, alpha=0.5, ax=axes[1,1])

# formats x/y labels
SP1.set_title("sepal_length (cm)", fontsize=7, fontname='fantasy')
SP1.set_xlabel(" ", fontsize=7)
SP1.set_ylabel("count", fontsize=7, fontname='fantasy')
SP2.set_title("sepal_width (cm)", fontsize=7, fontname='fantasy')
SP2.set_xlabel(" ", fontsize=7)
SP2.set_ylabel("count", fontsize=7, fontname='fantasy')
SP3.set_xlabel("petal_length (cm)", fontsize=7, fontname='fantasy')
SP3.set_ylabel("count", fontsize=7)
SP4.set_xlabel("petal_width (cm)", fontsize=7, fontname='fantasy')
SP4.set_ylabel("count", fontsize=7)

# formats ticks
SP1.tick_params(axis='both', which='major', labelsize=5)
SP2.tick_params(axis='both', which='major', labelsize=5)
SP3.tick_params(axis='both', which='major', labelsize=5)
SP4.tick_params(axis='both', which='major', labelsize=5)

# set title
plt.suptitle('Histograms (distribution frequency per variable)', fontsize=13, fontname='fantasy')
plt.show()

# creating a pairplot for all the variables
pg_1 = sns.PairGrid(iris, hue = 'species', palette=color_theme1)
pg_1.map_upper(sns.scatterplot)
pg_1.map_lower(sns.scatterplot)
pg_1.map_diag(plt.hist, stacked=True)
plt.subplots_adjust(top=.95)
plt.tick_params(axis='both', which='major', labelsize=5)
plt.suptitle('Pair Grid (scatterplots and histograms)', fontsize=15, fontname='fantasy')
plt.show()

# another pairplot with KDE this time
pg_2 = sns.PairGrid(iris, hue = 'species', palette=color_theme1)
pg_2.map_upper(sns.kdeplot, shade=True, alpha=0.5)
pg_2.map_lower(sns.kdeplot, shade=True, alpha=0.5)
pg_2.map_diag(sns.kdeplot, shade=True, alpha=0.5)
plt.subplots_adjust(top=.95)
plt.tick_params(axis='both', which='major', labelsize=5)
plt.suptitle('Pair Grid (KDE scatterplots and histograms)', fontsize=13, fontname='fantasy')
plt.show()