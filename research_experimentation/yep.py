import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.axes_style("darkgrid")
iris = pd.read_csv("/Users/caoimhinvallely/Desktop/Programming/Programming2021/pands-project2021/iris_dataset.csv")

f, axes = plt.subplots(2, 2)
# ax1. They are layed out in the form [0,0] where the first number represents the row and the second the column
# sns.jointplot(data=iris, x='sepal_length', y='sepal_width', kind='kde', ax=axes[0,0])

# sns.jointplot(data=iris, x='sepal_width', y='sepal_length', kind='kde', ax=axes[0,1])

# sns.jointplot(data=iris, x='petal_length', y='petal_width', kind='kde', ax=axes[1,0])

# sns.jointplot(data=iris, x='petal_width', y='petal_length', kind='kde', ax=axes[1,1])

# plt.show()

# iris_mx = iris.corr()
# sns.heatmap(iris_mx, annot=True, cmap="cubehelix")
# plt.show()

# species = iris.pop('species')
# versicolor = species
# print(versicolor.head())

# species = iris.pop('species')
# sns.clustermap(iris)
# plt.show()

print(iris.info())


# # boxplot of individual elements
# sns.boxplot(data=iris, linewidth=0.5, fliersize=3, palette=color_theme)
# plt.xticks(fontsize=7)
# plt.yticks(fontsize=7)
# plt.suptitle('Overall boxplot of individual element values', fontsize=15, fontname='fantasy')
# plt.show()

# # the same as violin plots
# f, axes = plt.subplots(2,2)
# sns.violinplot(x = 'species', y='sepal_length', data = iris, ax=axes[0,0], linewidth=0.5, palette=color_theme)
# sns.violinplot(x = 'species', y='sepal_width', data = iris, ax=axes[0,1], linewidth=0.5, palette=color_theme)
# sns.violinplot(x = 'species', y='petal_length', data = iris, ax=axes[1,0], linewidth=0.5, palette=color_theme)
# sns.violinplot(x = 'species', y='petal_width', data = iris, ax=axes[1,1], linewidth=0.5, palette=color_theme)
# axes[0,0].set_xlabel("Species", fontsize=7)
# axes[0,0].set_ylabel("Sepal Length (cm)", fontsize=7)
# axes[0,1].set_xlabel("Species", fontsize=7)
# axes[0,1].set_ylabel("Sepal Width (cm)", fontsize=7)
# axes[1,0].set_xlabel("Species", fontsize=7)
# axes[1,0].set_ylabel("Petal Length (cm)", fontsize=7)
# axes[1,1].set_xlabel("Species", fontsize=7)
# axes[1,1].set_ylabel("Petal Width (cm)", fontsize=7)

# # format x,y labels
# axes[0,0].tick_params(axis='both', which='major', labelsize=7)
# axes[0,1].tick_params(axis='both', which='major', labelsize=7)
# axes[1,0].tick_params(axis='both', which='major', labelsize=7)
# axes[1,1].tick_params(axis='both', which='major', labelsize=7)
# plt.suptitle('Violin plots', fontsize=15, fontname='fantasy')
# plt.show()

# # # creating scatter plots for each combination of variables petal,sepal length and width and vice versa.
# # # using subplot() so I can compare them side by side. 2 rows x 2 columns.
# f, axes = plt.subplots(2, 2)
# sns.scatterplot(data=iris, x='sepal_length', y='sepal_width', hue='species', palette=color_theme, ax=axes[0,0])
# sns.scatterplot(data=iris, x='sepal_width', y='sepal_length', hue='species', palette=color_theme, ax=axes[0,1])
# sns.scatterplot(data=iris, x='petal_length', y='petal_width', hue='species', palette=color_theme, ax=axes[1,0])
# sns.scatterplot(data=iris, x='petal_width', y='petal_length', hue='species', palette=color_theme, ax=axes[1,1])

# axes[0,0].set_xlabel(" ", fontsize=7)
# axes[0,0].set_ylabel("sepal_width (cm)", fontsize=7, fontname='fantasy')
# axes[0,0].set_title("sepal_length (cm)", fontsize=7, fontname='fantasy')
# axes[0,1].set_xlabel(" ", fontsize=7)
# axes[0,1].set_ylabel("sepal_length (cm)", fontsize=7, fontname='fantasy')
# axes[0,1].set_title("sepal_width (cm)", fontsize=7, fontname='fantasy')
# axes[1,0].set_xlabel("petal_length (cm)", fontsize=7, fontname='fantasy')
# axes[1,0].set_ylabel("petal_width (cm)", fontsize=7, fontname='fantasy')
# axes[1,1].set_xlabel("petal_width (cm)", fontsize=7, fontname='fantasy')
# axes[1,1].set_ylabel("petal_length (cm)", fontsize=7, fontname='fantasy')
# # set tick format
# axes[0,0].tick_params(axis='both', which='major', labelsize=5)
# axes[0,1].tick_params(axis='both', which='major', labelsize=5)
# axes[1,0].tick_params(axis='both', which='major', labelsize=5)
# axes[1,1].tick_params(axis='both', which='major', labelsize=5)
# # set legends
# axes[0,0].legend(fontsize=6, scatterpoints=3)
# axes[0,1].legend(fontsize=6, scatterpoints=3)
# axes[1,0].legend(fontsize=6, scatterpoints=3)
# axes[1,1].legend(fontsize=6, scatterpoints=3)

# # prints title
# plt.suptitle('Scatter plots', fontsize=15, fontname='fantasy')
# plt.show()


