# this is an analysis script for the Fisher iris dataset as part of 
# a project for the Programming and scripting module of HDIP in Data
# Analytics at GMIT (2021)

# Author: Caoimhin Vallely

# importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# sets background style, and colour palette for all the plots
sns.set_style("darkgrid")
color_theme = ['yellowgreen','teal','tomato']

# reads in the dataframe
iris = pd.read_csv("/Users/caoimhinvallely/Desktop/Programming/Programming2021/pands-project2021/iris_dataset.csv")

# this is an initial exploration of the data using all the conventional methods that pandas has to offer
I1 = ("----------\nInitial data exploration\n----------\n")
I2 = ("SIZE() - the total number of entries in the dataset\n" + str(iris.size) + "\n----------\n")
I3 = ("SHAPE() - the number of rows and columns\n" + str(iris.shape) + "\n----------\n")
I4 = ("COLUMNS() - these are the column labels and the data tyoe\n" + str(iris.columns) + "\n----------\n")
I5 = ("HEAD() - this is a printout of the first five rows of the dataset\n" + str(iris.head()) + "\n----------\n")
I6 = ("DESCRIBE() - this is an overview of the dataset\n" + str(iris.describe()) + "\n----------\n")
I7 = ("GROUPBY.DESCRIBE() - this is an overview of the dataset by species\n" + str(iris.groupby('species').describe()) + "\n----------\n")
I8 = ("CORR() - this is the correlation in the dataset\n" + str(iris.corr()) + "\n----------\n")

# prints all of the above info to a text file - iris_data.txt
with open('outputted_iris_data_textfile.txt','w') as d_a:
    d_a.writelines([I1, I2, I3, I4, I5, I6, I7, I8])

# # creating scatter plots for each combination of variables petal,sepal length and width and vice versa.
# # using subplot() so I can compare them side by side. 2 rows x 2 columns.
f, axes = plt.subplots(2, 2)
sns.scatterplot(data=iris, x='sepal_length', y='sepal_width', hue='species', palette=color_theme, ax=axes[0,0])
sns.scatterplot(data=iris, x='sepal_width', y='sepal_length', hue='species', palette=color_theme, ax=axes[0,1])
sns.scatterplot(data=iris, x='petal_length', y='petal_width', hue='species', palette=color_theme, ax=axes[1,0])
sns.scatterplot(data=iris, x='petal_width', y='petal_length', hue='species', palette=color_theme, ax=axes[1,1])

axes[0,0].set_xlabel(" ", fontsize=7)
axes[0,0].set_ylabel("sepal_width (cm)", fontsize=7, fontname='fantasy')
axes[0,0].set_title("sepal_length (cm)", fontsize=7, fontname='fantasy')
axes[0,1].set_xlabel(" ", fontsize=7)
axes[0,1].set_ylabel("sepal_length (cm)", fontsize=7, fontname='fantasy')
axes[0,1].set_title("sepal_width (cm)", fontsize=7, fontname='fantasy')
axes[1,0].set_xlabel("petal_length (cm)", fontsize=7, fontname='fantasy')
axes[1,0].set_ylabel("petal_width (cm)", fontsize=7, fontname='fantasy')
axes[1,1].set_xlabel("petal_width (cm)", fontsize=7, fontname='fantasy')
axes[1,1].set_ylabel("petal_length (cm)", fontsize=7, fontname='fantasy')
# set tick format
axes[0,0].tick_params(axis='both', which='major', labelsize=5)
axes[0,1].tick_params(axis='both', which='major', labelsize=5)
axes[1,0].tick_params(axis='both', which='major', labelsize=5)
axes[1,1].tick_params(axis='both', which='major', labelsize=5)
# set legends
axes[0,0].legend(fontsize=6, scatterpoints=3)
axes[0,1].legend(fontsize=6, scatterpoints=3)
axes[1,0].legend(fontsize=6, scatterpoints=3)
axes[1,1].legend(fontsize=6, scatterpoints=3)

# prints title
plt.suptitle('Scatter plots', fontsize=15, fontname='fantasy')
plt.show()

# creating histograms for distribution of each variable - sepal length and width, and petal length and width
# sets up 4 plots - 2x2.
fig, axes = plt.subplots(2,2)

SP1 = sns.histplot(data=iris, x='sepal_length', binwidth=0.1, hue='species', kde=True, palette=color_theme, legend=False, ax=axes[0,0])
SP2 = sns.histplot(data=iris, x='sepal_width', binwidth=0.1, hue='species', kde=True, palette=color_theme, legend=False, ax=axes[0,1])
SP3 = sns.histplot(data=iris, x='petal_length', binwidth=0.1, hue='species', kde=True, palette=color_theme, legend=False, ax=axes[1,0])
SP4 = sns.histplot(data=iris, x='petal_width', binwidth=0.1, hue='species', kde=True, palette=color_theme, ax=axes[1,1])

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
plt.suptitle('Histograms', fontsize=15, fontname='fantasy')
plt.show()

# creating a pairplot for all the variables
sns.pairplot(iris, hue="species", palette=color_theme)
plt.subplots_adjust(top=.95)
plt.suptitle('Pair Plot', fontsize=15, fontname='fantasy')
plt.show()

# 2x2 grid of boxplots
f, axes = plt.subplots(2,2)
sns.boxplot(x = 'species', y='sepal_length', data = iris, ax=axes[0,0], fliersize=3, linewidth=0.5, palette=color_theme)
sns.boxplot(x = 'species', y='sepal_width', data = iris, ax=axes[0,1], fliersize=3, linewidth=0.5, palette=color_theme)
sns.boxplot(x = 'species', y='petal_length', data = iris, ax=axes[1,0], fliersize=3, linewidth=0.5, palette=color_theme)
sns.boxplot(x = 'species', y='petal_width', data = iris, ax=axes[1,1], fliersize=3, linewidth=0.5, palette=color_theme)
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

plt.suptitle('Boxplots', fontsize=15, fontname='fantasy')
plt.show()

# violin plot stacked on a violin plot. Stingray!
f, axes = plt.subplots(2,2)
sns.violinplot(x = 'species', y='sepal_length', data = iris, ax=axes[0,0], linewidth=0.5, palette=color_theme)
sns.violinplot(x = 'species', y='sepal_width', data = iris, ax=axes[0,1], linewidth=0.5, palette=color_theme)
sns.violinplot(x = 'species', y='petal_length', data = iris, ax=axes[1,0], linewidth=0.5, palette=color_theme)
sns.violinplot(x = 'species', y='petal_width', data = iris, ax=axes[1,1], linewidth=0.5, palette=color_theme)
sns.swarmplot(x = 'species', y='sepal_length', data = iris, ax=axes[0,0], size=3, color='white', edgecolor='black', linewidth=.5)
sns.swarmplot(x = 'species', y='sepal_width', data = iris, ax=axes[0,1], size=3, color='white', edgecolor='black', linewidth=.5)
sns.swarmplot(x = 'species', y='petal_length', data = iris, ax=axes[1,0], size=3, color='white', edgecolor='black', linewidth=.5)
sns.swarmplot(x = 'species', y='petal_width', data = iris, ax=axes[1,1], size=3, color='white', edgecolor='black', linewidth=.5)
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

plt.suptitle('Swarm plot', fontsize=15, fontname='fantasy')
plt.show()

# kde plots - need to work on transparency
fig, axes = plt.subplots(2,2)
sns.kdeplot(data=iris, x="sepal_length", y="sepal_width", hue="species", legend=False, palette=['yellowgreen','teal','tomato'], fill=True, ax=axes[0,0])
sns.kdeplot(data=iris, x="sepal_width", y="sepal_length", hue="species", legend=False, palette=['yellowgreen','teal','tomato'], fill=True, ax=axes[0,1])
sns.kdeplot(data=iris, x="petal_length", y="petal_width", hue="species", legend=False, palette=['yellowgreen','teal','tomato'], fill=True, ax=axes[1,0])
sns.kdeplot(data=iris, x="petal_length", y="petal_width", hue="species", legend=False, palette=['yellowgreen','teal','tomato'], fill=True, ax=axes[1,1])

axes[0,0].set_title("sepal_length (cm)", fontsize=7, fontname='fantasy')
axes[0,0].set_xlabel(" ", fontsize=7)
axes[0,0].set_ylabel("sepal_width (cm)", fontsize=7, fontname='fantasy')
axes[0,1].set_title("sepal_width (cm)", fontsize=7, fontname='fantasy')
axes[0,1].set_xlabel(" ", fontsize=7)
axes[0,1].set_ylabel("sepal_length (cm)", fontsize=7, fontname='fantasy')
axes[1,0].set_xlabel("petal_length (cm)", fontsize=7, fontname='fantasy')
axes[1,0].set_ylabel("petal_width (cm)", fontsize=7, fontname='fantasy')
axes[1,1].set_xlabel("petal_width (cm)", fontsize=7, fontname='fantasy')
axes[1,1].set_ylabel("petal_length (cm)", fontsize=7, fontname='fantasy')
# set tick format
axes[0,0].tick_params(axis='both', which='major', labelsize=6)
axes[0,1].tick_params(axis='both', which='major', labelsize=6)
axes[1,0].tick_params(axis='both', which='major', labelsize=6)
axes[1,1].tick_params(axis='both', which='major', labelsize=6)

plt.suptitle('KDE plots', fontsize=15, fontname='fantasy')
plt.show()

# heat map based on correlation (all species)
iris_mx = iris.corr()
sns.heatmap(iris_mx, annot=True, cmap="cubehelix", linewidths=1, linecolor='grey')
plt.tick_params(axis='both', which='major', labelsize=7)
plt.suptitle('Heatmap', fontsize=15, fontname='fantasy')
plt.show()
