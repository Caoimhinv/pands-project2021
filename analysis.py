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
str1 = ("----------\nInitial data exploration\n----------\n")
str2 = ("SIZE() - the total number of entries in the dataframe\n" + str(iris.size) + "\n----------\n")
str3 = ("SHAPE() - the number of rows and columns\n" + str(iris.shape) + "\n----------\n")
str4 = ("COLUMNS() - these are the column labels and the data tyoe\n" + str(iris.columns) + "\n----------\n")
str5 = ("COUNT() - the number of entries per column\n" + str(iris.count()) + "\n----------\n")
str6 = ("HEAD() - this is a printout of the first five rows of the dataframe\n" + str(iris.head()) + "\n----------\n")
str7 = ("MAX() - this is the highest value per column\n" + str(iris.max()) + "\n----------\n")
str8 = ("MIN() - this is the lowest value per column\n" + str(iris.min()) + "\n----------\n")
str9 = ("MEAN() - this is the mean value per column\n" + str(iris.mean()) + "\n----------\n")
str10 = ("MEDIAN() - this the median value per column\n" + str(iris.median()) + "\n----------\n")
str11 = ("MODE() - this is the mode per column\n" + str(iris.mode()) + "\n----------\n")
str12 = ("STD() - this is the standard deviation per column\n" + str(iris.std()) + "\n----------\n----------\n")
str13 = ("DESCRIBE() - this is an overview of the dataframe (including a lot of the above again)\n" + str(iris.describe()) + "\n----------\n")
str14 = ("CORR() - this is the correlation among the data\n" + str(iris.corr()) + "\n----------\n")

# prints all of the above info to a text file - iris_data.txt
with open('iris_data.txt','w') as out:
    out.writelines([str1, str2, str3, str4, str5, str6, str7, str8, str9, str10, str11, str12, str13, str14])

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
sns.boxplot(x = 'species', y='sepal_length', data = iris, ax=axes[0,0], linewidth=0.5, palette=color_theme)
sns.boxplot(x = 'species', y='sepal_width', data = iris, ax=axes[0,1], linewidth=0.5, palette=color_theme)
sns.boxplot(x = 'species', y='petal_length', data = iris, ax=axes[1,0], linewidth=0.5, palette=color_theme)
sns.boxplot(x = 'species', y='petal_width', data = iris, ax=axes[1,1], linewidth=0.5, palette=color_theme)
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

sns.boxplot(data=iris, orient="h", linewidth=0.5, palette=color_theme)
plt.suptitle('Overall boxplot of individual element values', fontsize=15, fontname='fantasy')
plt.show()

# the same as violin plots
f, axes = plt.subplots(2,2)
sns.violinplot(x = 'species', y='sepal_length', data = iris, ax=axes[0,0], linewidth=0.5, palette=color_theme)
sns.violinplot(x = 'species', y='sepal_width', data = iris, ax=axes[0,1], linewidth=0.5, palette=color_theme)
sns.violinplot(x = 'species', y='petal_length', data = iris, ax=axes[1,0], linewidth=0.5, palette=color_theme)
sns.violinplot(x = 'species', y='petal_width', data = iris, ax=axes[1,1], linewidth=0.5, palette=color_theme)
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
plt.suptitle('Violin plots', fontsize=15, fontname='fantasy')
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
