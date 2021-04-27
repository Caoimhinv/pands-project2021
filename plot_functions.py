# This file contains functions to be used with the analysis.py program in this repositry.
# The functions all create data visualisations on the Iris dataset

# Author: Caoimhin Vallely

# Importing necessary modules
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# reads in the dataset
iris = pd.read_csv("iris_dataset.csv")

# sets global background style, and colour palettes
sns.set_style("darkgrid")
color_theme1 = ['yellowgreen','teal','tomato']
color_theme2 = ['yellowgreen','teal','tomato', 'plum']

# Creates a heatmap based on correlation
def heatmap():
    iris_hm = iris.corr() # method to find correlation and store it in variable 'iris_hm'
    # creates heatmap. annot prints the values on the map.
    # unfortunately my color_themes weren't really appropriate here so I went with a built-in!
    sns.heatmap(iris_hm, annot=True, cmap="cubehelix")
    plt.suptitle("Correlation heatmap", fontsize=15, fontname='fantasy')
    # gives user the option to view or save the file
    x = input("Enter (1) to view the heatmap or (2) to save to file? ")
    if x == '1':
        plt.show()
    elif x == '2':
        plt.savefig('./Images/heatmap.png') # saves to the image folder
    else:
        print("Invalid selection!") # error handling
        heatmap() # gives the user another go!

# creates a parallel coordinates plot
def parallel_coordinates():
    pd.plotting.parallel_coordinates(iris, 'species', color=color_theme1)
    plt.suptitle("Parallel coordinates", fontsize=15, fontname='fantasy')
    plt.xlim(-0.1,3.1) # increases plot dimension slightly so we can see the first and last lines
    plt.ylabel("cm", fontsize=7, fontname='fantasy')
    plt.tick_params(axis='y', which='major', labelsize=6)
    plt.legend(loc='upper center')
    x = input("Enter (1) to view the parallel coordinate plot or (2) to save to file? ")
    if x == '1':
        plt.show()
    elif x == '2':
        plt.savefig('./Images/parallel_coordinates.png') # saves to the image folder
    else:
        print("Invalid selection!") # error handling
        parallel_coordinates() # gives the user another go!

# function to creates a boxplot of all attributes and classes
def boxplot_overall():
    # creates a boxplot, with linesize, fliersize, and colour palette defined
    b = sns.boxplot(data=iris, linewidth=0.5, fliersize=3, palette=color_theme2)                                                                           
    plt.tick_params(axis='both', which='major', labelsize=7) # formats ticks on each axis
    b.set_ylabel("(cm)", fontsize=7, fontname='fantasy') # sets y label with font and fontsize
    plt.suptitle('Boxplot (all classes)', fontsize=15, fontname='fantasy') # prints title and sets font and fontsize
    x = input("Enter (1) to view the boxplot or (2) to save to file? ")
    if x == '1':
        plt.show()
    elif x == '2':
        plt.savefig('./Images/boxplot.png')
    else:
        print("Invalid selection!")
        boxplot_overall()

# pylint: disable=unused-variable #see below!

# function to create boxplot grid separating out each class
def boxplot_species_separated():
    f, axes = plt.subplots(2,2) # this produces a 2x2 grid of boxplots
    # the 'f' above was returning an unused variable warning, but then the plot wouldn't work if it was
    # removed. The code just above seems to solve the issue!
    # 4 boxplots - axes[0,0] refers to position on grid [row, column]
    # linesize, outlier marker size (fliersize), and colour palette defined
    sns.boxplot(x = 'species', y='sepal_length', data = iris, ax=axes[0,0], fliersize=3, linewidth=0.5, palette=color_theme1)
    sns.boxplot(x = 'species', y='sepal_width', data = iris, ax=axes[0,1], fliersize=3, linewidth=0.5, palette=color_theme1)
    sns.boxplot(x = 'species', y='petal_length', data = iris, ax=axes[1,0], fliersize=3, linewidth=0.5, palette=color_theme1)
    sns.boxplot(x = 'species', y='petal_width', data = iris, ax=axes[1,1], fliersize=3, linewidth=0.5, palette=color_theme1)
    # setting x and y labels. Didn't think anything necessary on x axis so left as blank i.e. " "
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
        plt.savefig('./Images/boxplot1.png')
    else:
        print("Invalid selection!")
        boxplot_species_separated()

# function creating violin plots
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
        plt.savefig('./Images/violinplot.png')
    else:
        print("Invalid selection!")
        violinplot_all_species()
    
# Function to create stripplots
# each class separated out. data points scattered on violin plots.
def violin_strip_plots():
    f, axes = plt.subplots(2,2)
    
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
        plt.savefig('./Images/stripplot.png')
    else:
        print("Invalid selection!")
        violin_strip_plots()
    
# function to create histograms to show distribution of each variable
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
        plt.savefig('./Images/histogram.png')
    else:
        print("Invalid selection!")
        histograms()

# function for scatterplot1 - sepal length v width
def scatter1():
    sns.scatterplot(data=iris, x='sepal_length', y='sepal_width', hue='species', edgecolor='black', palette=color_theme1)
    plt.xlabel("sepal_length (cm)", fontsize=7, fontname='fantasy')
    plt.ylabel("sepal_width (cm)", fontsize=7, fontname='fantasy')
    plt.tick_params(axis='both', which='major', labelsize=6)
    plt.suptitle('Scatterplot - sepal length v width', fontsize=13, fontname='fantasy')
    x = input("Enter (1) to view the scatterplot or (2) to save to file? ")
    if x == '1':
        plt.show()
    elif x == '2':
        plt.savefig('./Images/scatter1.png')
    else:
        print("Invalid selection!")
        scatter1()
    
# function for scatterplot2 - petal length v width
def scatter2():
    sns.scatterplot(data=iris, x='petal_length', y='petal_width', hue='species', edgecolor='black', palette=color_theme1)
    plt.xlabel("petal_length (cm)", fontsize=7, fontname='fantasy')
    plt.ylabel("petal_width (cm)", fontsize=7, fontname='fantasy')
    plt.tick_params(axis='both', which='major', labelsize=6)
    plt.suptitle('Scatterplot - petal length v width', fontsize=13, fontname='fantasy')
    x = input("Enter (1) to view the scatterplot or (2) to save to file? ")
    if x == '1':
        plt.show()
    elif x == '2':
        plt.savefig('./Images/scatter2.png')
    else:
        print("Invalid selection!")
        scatter2()

# Function to create a pairplot for all the variables
def pairplot():
    pp_1 = sns.pairplot(iris, hue = 'species', palette=color_theme1)
    pp_1.map_diag(plt.hist, alpha=0.5) # specifies histogram on the diagonal. Alpha is transparency.
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
        plt.savefig('./Images/pairplot.png')
    else:
        print("Invalid selection!")
        pairplot()

# Function to create pairgrid with KDE this time
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
        plt.savefig('./Images/pairgrid.png')
    else:
        print("Invalid selection!")
        pairgrid()