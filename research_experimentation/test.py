# experimenting with histograms in seaborn
# Author: Caoimhin Vallely

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("darkgrid")
iris = pd.read_csv("/Users/caoimhinvallely/Desktop/Programming/Programming2021/pands-project2021/iris_dataset.csv")

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

# sns.histplot(data=iris, binwidth=0.1)

# sns.histplot(data=iris, x='sepal_length', binwidth=0.1, hue='species', kde=True)

# sns.histplot(data=iris, x='sepal_length', binwidth=0.1, hue='species', multiple="stack", kde=True, palette=['yellowgreen','teal','tomato'])

# plt.show()

#messing with boxplot.
# sns.violinplot(x = 'species', y='petal_length', data = iris, palette='magma', label='petal_length')
# sns.violinplot(x = 'species', y='petal_width', data = iris, palette='flare', label='petal_width')
# sns.violinplot(x = 'species', y='sepal_length', data = iris, palette='crest', label='sepal_length')
# sns.violinplot(x = 'species', y='sepal_width', data = iris, palette='rocket', label='sepal_width')
# plt.legend()
# sns.boxplot(x = 'species', y='petal_length', data = iris, palette='magma')
# sns.boxplot(x = 'species', y='petal_width', data = iris, palette='flare')
# sns.boxplot(x = 'species', y='sepal_length', data = iris, palette='crest')
# sns.boxplot(x = 'species', y='sepal_width', data = iris, palette='rocket')
# plt.legend()
# # sns.boxplot(x = 'species', y='petal_width', data = iris)
# plt.show()

# violin plot definitely!
# redo scatters maybe\
# set_style - whie, darkgrid
# set_context - paper
# palette= and color maps - check matplotlib documentation
# legend off the plot = bbox_to_anchor


# species = iris.pop('species')
# sns.clustermap(iris)
# plt.show()

# iris_g = sns.PairGrid(iris, hue = 'species')
# iris_g.map_diag(plt.hist)
# # iris_g.map_offdiag(plt.scatter)
# iris_g.map_upper(plt.scatter)
# iris_g.map_lower(sns.kdeplot)

# plt.show()

# so maybe kde or cluster or heat map for matrix?
# f, axes = plt.subplots(2,2)
# sns.boxplot(x = 'species', y='sepal_length', data = iris, ax=axes[0,0])
# sns.boxplot(x = 'species', y='sepal_width', data = iris, ax=axes[0,1])
# sns.boxplot(x = 'species', y='petal_length', data = iris, ax=axes[1,0])
# sns.boxplot(x = 'species', y='petal_width', data = iris, ax=axes[1,1])
# plt.show()


# f, axes = plt.subplots(2,2)
# sns.violinplot(x = 'species', y='sepal_length', data = iris, ax=axes[0,0])
# sns.violinplot(x = 'species', y='sepal_width', data = iris, ax=axes[0,1])
# sns.violinplot(x = 'species', y='petal_length', data = iris, ax=axes[1,0])
# sns.violinplot(x = 'species', y='petal_width', data = iris, ax=axes[1,1])
# plt.show()

# f, axes = plt.subplots(2,2)
# sns.violinplot(x = 'species', y='sepal_length', data = iris, ax=axes[0,0])
# sns.violinplot(x = 'species', y='sepal_width', data = iris, ax=axes[0,1])
# sns.violinplot(x = 'species', y='petal_length', data = iris, ax=axes[1,0])
# sns.violinplot(x = 'species', y='petal_width', data = iris, ax=axes[1,1])
# sns.swarmplot(x = 'species', y='sepal_length', data = iris, ax=axes[0,0], size=3, color='white', edgecolor='b')
# sns.swarmplot(x = 'species', y='sepal_width', data = iris, ax=axes[0,1], size=3, color='white', edgecolor='b')
# sns.swarmplot(x = 'species', y='petal_length', data = iris, ax=axes[1,0], size=3, color='white', edgecolor='b')
# sns.swarmplot(x = 'species', y='petal_width', data = iris, ax=axes[1,1], size=3, color='white', edgecolor='b')
# plt.show()

# iris_mx = iris.corr()
# sns.heatmap(iris_mx, annot=True, cmap='Blues')
# plt.show()

f, axes = plt.subplots(2, 2)
sns.scatterplot(data=iris, x='sepal_length', y='sepal_width', hue='species', palette=['yellowgreen','teal','tomato'], ax=axes[0,0])
sns.scatterplot(data=iris, x='sepal_width', y='sepal_length', hue='species', palette=['yellowgreen','teal','tomato'], ax=axes[0,1])
sns.scatterplot(data=iris, x='petal_length', y='petal_width', hue='species', palette=['yellowgreen','teal','tomato'], ax=axes[1,0])
sns.scatterplot(data=iris, x='petal_width', y='petal_length', hue='species', palette=['yellowgreen','teal','tomato'], ax=axes[1,1])


plt.show()

# f, axes = plt.subplots(2,2)
# sns.violinplot(x = 'species', y='sepal_length', data = iris, ax=axes[0,0], palette=['yellowgreen','teal','tomato'])
# sns.violinplot(x = 'species', y='sepal_width', data = iris, ax=axes[0,1], palette=['yellowgreen','teal','tomato'])
# sns.violinplot(x = 'species', y='petal_length', data = iris, ax=axes[1,0], palette=['yellowgreen','teal','tomato'])
# sns.violinplot(x = 'species', y='petal_width', data = iris, ax=axes[1,1], palette=['yellowgreen','teal','tomato'])
# sns.swarmplot(x = 'species', y='sepal_length', data = iris, ax=axes[0,0], size=3, color='white', edgecolor='black', linewidth=.5)
# sns.swarmplot(x = 'species', y='sepal_width', data = iris, ax=axes[0,1], size=3, color='white', edgecolor='black', linewidth=.5)
# sns.swarmplot(x = 'species', y='petal_length', data = iris, ax=axes[1,0], size=3, color='white', edgecolor='black', linewidth=.5)
# sns.swarmplot(x = 'species', y='petal_width', data = iris, ax=axes[1,1], size=3, color='white', edgecolor='black', linewidth=.5)
# plt.show()