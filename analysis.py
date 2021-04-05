# this is an analysis script on Fisher's iris dataset as part of 
# a project for the Programming and scripting module of HDIP in Data
# Analytics at GMIT (2021)

# Author: Caoimhin Vallely

# importing pandas, matplotlib.pyplot, and seaborn libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# reads in the dataset
iris = pd.read_csv("/Users/caoimhinvallely/Desktop/Programming/Programming2021/pands-project2021/iris_dataset.csv")

# this is an initial exploration of the data
I1 = ("----------\nInitial data exploration\n----------\n")
I2 = ("SIZE() - the total number of entries in the dataset:\n" + str(iris.size) + "\n----------\n")
I3 = ("SHAPE() - the number of rows and columns:\n" + str(iris.shape) + "\n----------\n")
I4 = ("COLUMNS() - these are the column labels and the data type:\n" + str(iris.columns) + "\n----------\n")
I5 = ("HEAD() - this is a printout of the first five rows of the dataset:\n" + str(iris.head()) + "\n----------\n")
I6 = ("TAIL() - this is a printout of the last five rows of the dataset:\n" + str(iris.tail()) + "\n----------\n")
I7 = ("SAMPLE() - this is a printout of a random five rows of the dataset:\n" + str(iris.sample(5)) + "\n----------\n")
iris_des = iris.describe()
I8 = ("DESCRIBE() - this is a statistical overview of the dataset:\n" + str(iris_des.transpose()) + "\n----------\n")
set_des = iris.loc[iris['species'] == "setosa"].describe()
ver_des = iris.loc[iris['species'] == "versicolor"].describe()
vir_des = iris.loc[iris['species'] == "virginica"].describe()
I9 = ("DESCRIBE() by species - same overview but with each species isolated\n")
I10 = "--setosa--\n" + str(set_des.transpose()) + "\n\n"
I11 = "--versicolor--\n" + str(ver_des.transpose()) + "\n\n"
I12 = "--virginica--\n" + str(vir_des.transpose()) + "\n"

# prints all of the above info to a text file - outputted_iris_data.txt
with open('outputted_iris_data_textfile.txt','w') as d_a:
    d_a.writelines([I1, I2, I3, I4, I5, I6, I7, I8, I9, I10, I11, I12])

# Visualisations

# sets global background style, and colour palettes
sns.set_style("darkgrid")
color_theme1 = ['yellowgreen','teal','tomato']
color_theme2 = ['yellowgreen','teal','tomato', 'plum']

# creates a boxplot of all elements
b = sns.boxplot(data=iris, linewidth=0.5, fliersize=3, palette=color_theme2) # creates a boxplot, with linesize, outlier
                                                                            # marker size (fliersize), and colour palette defined
plt.tick_params(axis='both', which='major', labelsize=7) # formats ticks on each axis
b.set_ylabel("(cm)", fontsize=7, fontname='fantasy') # sets y label with font and fontsize
plt.suptitle('Boxplot (all irises)', fontsize=15, fontname='fantasy') # prints title and sets font and fontsize
plt.show()

# boxplot grid separating out each species
f, axes = plt.subplots(2,2) # this produces a 2x2 grid of boxplots

# 4 boxplots - axes[0,0] regfers to position on grid [row, column]
# linesize, outlier marker size (fliersize), and colour palette defined
sns.boxplot(x = 'species', y='sepal_length', data = iris, ax=axes[0,0], fliersize=3, linewidth=0.5, palette=color_theme1)
sns.boxplot(x = 'species', y='sepal_width', data = iris, ax=axes[0,1], fliersize=3, linewidth=0.5, palette=color_theme1)
sns.boxplot(x = 'species', y='petal_length', data = iris, ax=axes[1,0], fliersize=3, linewidth=0.5, palette=color_theme1)
sns.boxplot(x = 'species', y='petal_width', data = iris, ax=axes[1,1], fliersize=3, linewidth=0.5, palette=color_theme1)
# setting x and y labels. Don't think anything necessary on x axis so left as blank i.e. " "
axes[0,0].set_xlabel(" ", fontsize=7)
axes[0,0].set_ylabel("sepal_length (cm)", fontsize=7, fontname='fantasy')
axes[0,1].set_xlabel(" ", fontsize=7)
axes[0,1].set_ylabel("sepal_width (cm)", fontsize=7, fontname='fantasy')
axes[1,0].set_xlabel(" ", fontsize=7)
axes[1,0].set_ylabel("petal_Length (cm)", fontsize=7, fontname='fantasy')
axes[1,1].set_xlabel(" ", fontsize=7)
axes[1,1].set_ylabel("petal_width (cm)", fontsize=7, fontname='fantasy')
# format x,y ticks
axes[0,0].tick_params(axis='both', which='major', labelsize=6)
axes[0,1].tick_params(axis='both', which='major', labelsize=6)
axes[1,0].tick_params(axis='both', which='major', labelsize=6)
axes[1,1].tick_params(axis='both', which='major', labelsize=6)
# prints title and formatting
plt.suptitle('Boxplots (species separated)', fontsize=15, fontname='fantasy')
plt.show()

# creating violin plots
# firstly with all irises
b = sns.violinplot(data=iris, linewidth=0.5, fliersize=6, inner='point', palette=color_theme2) # creates plot with formatting
plt.tick_params(axis='both', which='major', labelsize=7) # sets ticks
b.set_ylabel("(cm)", fontsize=7, fontname='fantasy') # sets y label with formatting
plt.suptitle('Violinplot (all irises)', fontsize=15, fontname='fantasy') # sets title with formatting
plt.show()

# # Stripplots
# # each class separated out. data points scattered violin plots.
# f, axes = plt.subplots(2,2) # creats a 2x2 grid
# # creates 4 violin plots
# sns.violinplot(x = 'species', y='sepal_length', data = iris, ax=axes[0,0], linewidth=0.5, palette=color_theme1)
# sns.violinplot(x = 'species', y='sepal_width', data = iris, ax=axes[0,1], linewidth=0.5, palette=color_theme1)
# sns.violinplot(x = 'species', y='petal_length', data = iris, ax=axes[1,0], linewidth=0.5, palette=color_theme1)
# sns.violinplot(x = 'species', y='petal_width', data = iris, ax=axes[1,1], linewidth=0.5, palette=color_theme1)
# # creates stipplots, i.e. data markers added to violin plots
# sns.stripplot(x = 'species', y='sepal_length', data = iris, ax=axes[0,0], size=2, color='white', edgecolor='black', linewidth=.5)
# sns.stripplot(x = 'species', y='sepal_width', data = iris, ax=axes[0,1], size=2, color='white', edgecolor='black', linewidth=.5)
# sns.stripplot(x = 'species', y='petal_length', data = iris, ax=axes[1,0], size=2, color='white', edgecolor='black', linewidth=.5)
# sns.stripplot(x = 'species', y='petal_width', data = iris, ax=axes[1,1], size=2, color='white', edgecolor='black', linewidth=.5)
# # sets x and y lables with formatting
# axes[0,0].set_xlabel(" ", fontsize=7)
# axes[0,0].set_ylabel("sepal_length (cm)", fontsize=7, fontname='fantasy')
# axes[0,1].set_xlabel(" ", fontsize=7)
# axes[0,1].set_ylabel("sepal_width (cm)", fontsize=7, fontname='fantasy')
# axes[1,0].set_xlabel(" ", fontsize=7)
# axes[1,0].set_ylabel("petal_length (cm)", fontsize=7, fontname='fantasy')
# axes[1,1].set_xlabel(" ", fontsize=7)
# axes[1,1].set_ylabel("petal_width (cm)", fontsize=7, fontname='fantasy')
# # format x,y ticks
# axes[0,0].tick_params(axis='both', which='major', labelsize=6)
# axes[0,1].tick_params(axis='both', which='major', labelsize=6)
# axes[1,0].tick_params(axis='both', which='major', labelsize=6)
# axes[1,1].tick_params(axis='both', which='major', labelsize=6)
# # sets title with formatting
# plt.suptitle('Strip plots (species separated and data points scattered)', fontsize=13, fontname='fantasy')
# plt.show()

# # histograms to show distribution of each variable
# # sets up 4 plots - 2x2.
# fig, axes = plt.subplots(2,2)
# # creates 4 histograms with formatting, including KDE curve. Alpha (transparency) set to 0.5 so we can see the patterns more clearly
# SP1 = sns.histplot(data=iris, x='sepal_length', binwidth=0.1, hue='species', kde=True, palette=color_theme1, alpha=0.5, legend=False, ax=axes[0,0])
# SP2 = sns.histplot(data=iris, x='sepal_width', binwidth=0.1, hue='species', kde=True, palette=color_theme1, alpha=0.5, legend=False, ax=axes[0,1])
# SP3 = sns.histplot(data=iris, x='petal_length', binwidth=0.1, hue='species', kde=True, palette=color_theme1, alpha=0.5, legend=False, ax=axes[1,0])
# SP4 = sns.histplot(data=iris, x='petal_width', binwidth=0.1, hue='species', kde=True, palette=color_theme1, alpha=0.5, ax=axes[1,1])
# # sets x, y labels with formatting. substituing title for x label for clarity (looks cluttered below)
# SP1.set_title("sepal_length (cm)", fontsize=7, fontname='fantasy')
# SP1.set_xlabel(" ", fontsize=7)
# SP1.set_ylabel("count", fontsize=7, fontname='fantasy')
# SP2.set_title("sepal_width (cm)", fontsize=7, fontname='fantasy')
# SP2.set_xlabel(" ", fontsize=7)
# SP2.set_ylabel("count", fontsize=7, fontname='fantasy')
# SP3.set_xlabel("petal_length (cm)", fontsize=7, fontname='fantasy')
# SP3.set_ylabel("count", fontsize=7)
# SP4.set_xlabel("petal_width (cm)", fontsize=7, fontname='fantasy')
# SP4.set_ylabel("count", fontsize=7)
# # sets ticks
# SP1.tick_params(axis='both', which='major', labelsize=5)
# SP2.tick_params(axis='both', which='major', labelsize=5)
# SP3.tick_params(axis='both', which='major', labelsize=5)
# SP4.tick_params(axis='both', which='major', labelsize=5)
# # sets title with formatting
# plt.suptitle('Histograms (distribution frequency per variable)', fontsize=13, fontname='fantasy')
# plt.show()

# # creating a pairgrid for all the variables
# pg_1 = sns.PairGrid(iris, hue = 'species', palette=color_theme1)
# pg_1.map_upper(sns.scatterplot) # above and below the diagonal will be scatter plots
# pg_1.map_lower(sns.scatterplot)
# pg_1.map_diag(plt.hist, stacked=True) # creates histogram on the diagonal
# plt.subplots_adjust(top=.95) # creates apce above the plot for the title
# plt.tick_params(axis='both', which='major', labelsize=5) # sets ticks
# # sets title with formatting
# plt.suptitle('Pair Grid (scatterplots and histograms)', fontsize=15, fontname='fantasy')
# plt.show()

# # another pairplot with KDE this time
# pg_2 = sns.PairGrid(iris, hue = 'species', palette=color_theme1)
# pg_2.map_upper(sns.kdeplot, shade=True, alpha=0.5) # creates KDE above and below the diagonal. aplha set to 
#                                                     # so we can see through
# pg_2.map_lower(sns.kdeplot, shade=True, alpha=0.5)
# pg_2.map_diag(sns.kdeplot, shade=True, alpha=0.5) # KDE histogram on the diagonal
# plt.subplots_adjust(top=.95) # creates apce above the plot for the title
# plt.tick_params(axis='both', which='major', labelsize=5) # sets ticks
# # sets title and formatting
# plt.suptitle('Pair Grid (KDE scatterplots and histograms)', fontsize=13, fontname='fantasy')
# plt.show()