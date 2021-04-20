# VISUALISATIONS

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import csv

# this seems to get rid of an 'unused variable' warning I was getting!
# pylint: disable=unused-variable

iris = pd.read_csv("/Users/caoimhinvallely/Desktop/Programming/Programming2021/pands-project2021/iris_dataset.csv")

# sets global background style, and colour palettes
sns.set_style("darkgrid")
color_theme1 = ['yellowgreen','teal','tomato']
color_theme2 = ['yellowgreen','teal','tomato', 'plum']

# Creates a heatmap based on correlation
def heatmap():
    iris_hm = iris.corr()
    sns.heatmap(iris_hm, annot=True, cmap="cubehelix") # my color_themes weren't really appropriate here unfortunately!
    x = input("Enter (1) to view the heatmap or (2) to save to file? ")
    if x == '1':
        plt.show()
    elif x == '2':
        plt.savefig('/Users/caoimhinvallely/Desktop/Programming/Programming2021/pands-project2021/Images/heatmap.png')
    else:
        print("Invalid selection!")
        heatmap()

# creates a boxplot of all elements
def boxplot_overall():
    b = sns.boxplot(data=iris, linewidth=0.5, fliersize=3, palette=color_theme2) # creates a boxplot, with linesize, outlier
                                                                                # marker size (fliersize), and colour palette defined
    plt.tick_params(axis='both', which='major', labelsize=7) # formats ticks on each axis
    b.set_ylabel("(cm)", fontsize=7, fontname='fantasy') # sets y label with font and fontsize
    plt.suptitle('Boxplot (all classes)', fontsize=15, fontname='fantasy') # prints title and sets font and fontsize
    x = input("Enter (1) to view the boxplot or (2) to save to file? ")
    if x == '1':
        plt.show()
    elif x == '2':
        plt.savefig('/Users/caoimhinvallely/Desktop/Programming/Programming2021/pands-project2021/Images/boxplot.png')
    else:
        print("Invalid selection!")
        boxplot_overall()

# boxplot grid separating out each species
def boxplot_species_separated():
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
    plt.suptitle('Boxplots (classes separated)', fontsize=15, fontname='fantasy')
    plt.tight_layout()
    x = input("Enter (1) to view the boxplots or (2) to save to file? ")
    if x == '1':
        plt.show()
    elif x == '2':
        plt.savefig('/Users/caoimhinvallely/Desktop/Programming/Programming2021/pands-project2021/Images/boxplot1.png')
    else:
        print("Invalid selection!")
        boxplot_species_separated()

# creating violin plots
# firstly with all irises
def violinplot_all_species():
    b = sns.violinplot(data=iris, linewidth=0.5, fliersize=6, inner='point', palette=color_theme2) # creates plot with formatting
    plt.tick_params(axis='both', which='major', labelsize=7) # sets ticks
    b.set_ylabel("(cm)", fontsize=7, fontname='fantasy') # sets y label with formatting
    plt.suptitle('Violinplot (all classes)', fontsize=15, fontname='fantasy') # sets title with formatting
    x = input("Enter (1) to view the violinplot or (2) to save to file? ")
    if x == '1':
        plt.show()
    elif x == '2':
        plt.savefig('/Users/caoimhinvallely/Desktop/Programming/Programming2021/pands-project2021/Images/violinplot.png')
    else:
        print("Invalid selection!")
        violinplot_all_species()
    
# Stripplots
# each class separated out. data points scattered violin plots.
def violin_strip_plots():
    f, axes = plt.subplots(2,2) # creats a 2x2 grid
    # creates 4 violin plots
    sns.violinplot(x = 'species', y='sepal_length', data = iris, ax=axes[0,0], linewidth=0.5, palette=color_theme1)
    sns.violinplot(x = 'species', y='sepal_width', data = iris, ax=axes[0,1], linewidth=0.5, palette=color_theme1)
    sns.violinplot(x = 'species', y='petal_length', data = iris, ax=axes[1,0], linewidth=0.5, palette=color_theme1)
    sns.violinplot(x = 'species', y='petal_width', data = iris, ax=axes[1,1], linewidth=0.5, palette=color_theme1)
    # creates stipplots, i.e. data markers added to violin plots
    sns.stripplot(x = 'species', y='sepal_length', data = iris, ax=axes[0,0], size=2, color='white', edgecolor='black', linewidth=.5)
    sns.stripplot(x = 'species', y='sepal_width', data = iris, ax=axes[0,1], size=2, color='white', edgecolor='black', linewidth=.5)
    sns.stripplot(x = 'species', y='petal_length', data = iris, ax=axes[1,0], size=2, color='white', edgecolor='black', linewidth=.5)
    sns.stripplot(x = 'species', y='petal_width', data = iris, ax=axes[1,1], size=2, color='white', edgecolor='black', linewidth=.5)
    # sets x and y lables with formatting
    axes[0,0].set_xlabel(" ", fontsize=7)
    axes[0,0].set_ylabel("sepal_length (cm)", fontsize=7, fontname='fantasy')
    axes[0,1].set_xlabel(" ", fontsize=7)
    axes[0,1].set_ylabel("sepal_width (cm)", fontsize=7, fontname='fantasy')
    axes[1,0].set_xlabel(" ", fontsize=7)
    axes[1,0].set_ylabel("petal_length (cm)", fontsize=7, fontname='fantasy')
    axes[1,1].set_xlabel(" ", fontsize=7)
    axes[1,1].set_ylabel("petal_width (cm)", fontsize=7, fontname='fantasy')
    # format x,y ticks
    axes[0,0].tick_params(axis='both', which='major', labelsize=6)
    axes[0,1].tick_params(axis='both', which='major', labelsize=6)
    axes[1,0].tick_params(axis='both', which='major', labelsize=6)
    axes[1,1].tick_params(axis='both', which='major', labelsize=6)
    # sets title with formatting
    plt.suptitle('Strip plots (classes separated and data points scattered)', fontsize=13, fontname='fantasy')
    plt.tight_layout()
    x = input("Enter (1) to view the stripplots or (2) to save to file? ")
    if x == '1':
        plt.show()
    elif x == '2':
        plt.savefig('/Users/caoimhinvallely/Desktop/Programming/Programming2021/pands-project2021/Images/stripplot.png')
    else:
        print("Invalid selection!")
        violin_strip_plots()
    
# histograms to show distribution of each variable
# sets up 4 plots - 2x2.
def histograms():
    fig, axs = plt.subplots(2,2)
    # creates 4 histograms with formatting, including KDE curve. Alpha (transparency) set to 0.5 so we can see the patterns more clearly
    SP1 = sns.histplot(data=iris, x='sepal_length', binwidth=0.1, hue='species', kde=True, palette=color_theme1, alpha=0.5, legend=False, ax=axs[0,0])
    SP2 = sns.histplot(data=iris, x='sepal_width', binwidth=0.1, hue='species', kde=True, palette=color_theme1, alpha=0.5, legend=False, ax=axs[0,1])
    SP3 = sns.histplot(data=iris, x='petal_length', binwidth=0.1, hue='species', kde=True, palette=color_theme1, alpha=0.5, legend=False, ax=axs[1,0])
    SP4 = sns.histplot(data=iris, x='petal_width', binwidth=0.1, hue='species', kde=True, palette=color_theme1, alpha=0.5, ax=axs[1,1])
    # sets x, y labels with formatting. substituing title for x label for clarity (looks cluttered positioned below)
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
    # sets ticks
    SP1.tick_params(axis='both', which='major', labelsize=5)
    SP2.tick_params(axis='both', which='major', labelsize=5)
    SP3.tick_params(axis='both', which='major', labelsize=5)
    SP4.tick_params(axis='both', which='major', labelsize=5)
    # sets title with formatting
    plt.suptitle('Histograms (distribution frequency per variable)', fontsize=13, fontname='fantasy')
    plt.tight_layout()
    x = input("Enter (1) to view the histograms or (2) to save to file? ")
    if x == '1':
        plt.show()
    elif x == '2':
        plt.savefig('/Users/caoimhinvallely/Desktop/Programming/Programming2021/pands-project2021/Images/histogram.png')
    else:
        print("Invalid selection!")
        histograms()
    
# creating a pairplot for all the variables
def pairplot():
    pp_1 = sns.pairplot(iris, hue = 'species', palette=color_theme1)
    pp_1.map_diag(plt.hist, alpha=0.5) # creates histogram on the diagonal
    plt.subplots_adjust(top=.95) # creates space above the plot for the title
    plt.tick_params(axis='both', which='major', labelsize=5) # sets ticks
    # sets title with formatting
    plt.suptitle('Pairplot (scatterplots and histograms)', fontsize=15, fontname='fantasy')
    # removes default legend which I couldn't get to move?
    pp_1._legend.remove()
    # creates a new legend which I can position in a more suitable place
    pp_1.add_legend(bbox_to_anchor=(0.98, 0.2))
    plt.tight_layout()
    x = input("Enter (1) to view the pairplot or (2) to save to file? ")
    if x == '1':
        plt.show()
    elif x == '2':
        plt.savefig('/Users/caoimhinvallely/Desktop/Programming/Programming2021/pands-project2021/Images/pairplot.png')
    else:
        print("Invalid selection!")
        pairplot()

# pairgrid with KDE this time
def pairgrid():
    pg_2 = sns.PairGrid(iris, hue = 'species', palette=color_theme1)
    pg_2.map_upper(sns.kdeplot, shade=True, alpha=0.5) # creates KDE above and below the diagonal. aplha set to 
                                                                           # so we can see through
    pg_2.map_lower(sns.kdeplot, alpha=0.5)
    pg_2.map_diag(sns.kdeplot, shade=True, alpha=0.5) # KDE histogram on the diagonal
    plt.subplots_adjust(top=.95) # creates apce above the plot for the title
    plt.tick_params(axis='both', which='major', labelsize=5) # sets ticks
    # sets title and formatting
    plt.suptitle('Pair Grid (KDE scatterplots and histograms)', fontsize=13, fontname='fantasy')
    pg_2.add_legend(bbox_to_anchor=(0.98, 0.22))
    plt.tight_layout()
    x = input("Enter (1) to view the pairgrid or (2) to save to file? ")
    if x == '1':
        plt.show()
    elif x == '2':
        plt.savefig('/Users/caoimhinvallely/Desktop/Programming/Programming2021/pands-project2021/Images/pairgrid.png')
    else:
        print("Invalid selection!")
        pairgrid()