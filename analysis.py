# this is an analysis script on Fisher's iris dataset as part of 
# a project for the Programming and scripting module of HDIP in Data
# Analytics at GMIT (2021)

# Author: Caoimhin Vallely

# importing pandas, matplotlib.pyplot, csv, and seaborn libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import csv

# this seems to get rid of an 'unused variable' warning I was getting!
# pylint: disable=unused-variable

# reads in the dataset
iris = pd.read_csv("/Users/caoimhinvallely/Desktop/Programming/Programming2021/pands-project2021/iris_dataset.csv")

# this is an initial exploration of the data
# creating variables to be printed to a txt file and also to be used later in the menu section
I1 = ("-----FISHER'S IRIS DATASET ANALYSIS PROJECT-----\n\n"\
"------------INITIAL DATA EXPLORATION------------\n\n******\n")
I2 = ("\nSIZE() - the total number of entries in the dataset:\n" + str(iris.size) + "\n\n******\n" +\
"\nSHAPE() - the number of rows and columns:\n" + str(iris.shape) + "\n\n******\n"\
"\nCOLUMNS() - these are the column labels and the data type:\n" + str(iris.columns) + "\n\n******\n"\
"\nISNULL() - this returns if there are any null or missing values (FALSE means no null values)\n" + str(iris.isnull().values.any()) + "\n\n******\n")
# head(6) returns the first 6 entries. Default is 5 - guess I'm just demonstrating that I know that1 ;)
I3 = ("\nHEAD() - this is a printout of the first 6 rows of the dataset:\n" + str(iris.head(6)) + "\n\n******\n" +\
"\nTAIL() - this is a printout of the last 6 rows of the dataset:\n" + str(iris.tail(6)) + "\n\n******\n" +\
"\nSAMPLE() - this is a printout of a random 6 rows of the dataset:\n" + str(iris.sample(6)) + "\n\n******\n")
# this returns the number of entries per species
I4 = ("\nVALUE_COUNTS() - this shows how many values for each class/species\n" + str(iris["species"].value_counts()) + "\n\n******\n")
iris_des = iris.describe()
# decribe() gives me a table of overall analysis including count, mean, standard deviation, min, max, and 25/50/75  percentiles
# transpose changes the x and y of the table. I think it's easier to read this way
I5 = ("\nDESCRIBE() - this is a statistical overview of the dataset:\n" + str(iris_des.transpose()) + "\n\n******\n")

# this returns a table/dataframe of the correlation between the attributes
I6 = ("\nCORR() - this shows the correlation between the variables in the data:\n" + str(iris.corr()) + "\n\n******\n")

set_des = iris.loc[iris['species'] == "setosa"].describe()
ver_des = iris.loc[iris['species'] == "versicolor"].describe()
vir_des = iris.loc[iris['species'] == "virginica"].describe()
I7 = ("\nDESCRIBE() by class - overview with each class isolated\n" +\
"--setosa--\n" + str(set_des.transpose()) + "\n\n" +\
"--versicolor--\n" + str(ver_des.transpose()) + "\n\n" +\
"--virginica--\n" + str(vir_des.transpose()) + "\n\n******\n")

# creates a new copy of iris to manipulate
iris2 = iris.copy()
# creates a variable for the columns in the dataset
cols = iris2.columns
# creates a variable for the first 4 columns in the dataset
original_columns = iris2[cols[0:4]]
# adds the total for the first 4 columns in each row and creates a new column for the result
iris2["totals"] = original_columns.sum(axis=1)
# finds the mean for the first 4 columns in each row and creates a new column for the result
iris2["mean"] = original_columns.mean(axis=1)

# reorders columns so we have 'species' last as before
iris2 = iris2[['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'totals', 'mean', 'species']]

# creating variables for individual classes in the new dataset
setosa = iris2.loc[iris2["species"] == "setosa"]
versicolor = iris2.loc[iris2["species"] == "versicolor"]
virginica = iris2.loc[iris2["species"] == "virginica"]

I8 = ("\nThe following are the first 5 rows of each class with totals and means of each row included:\n" +\
"--setosa--\n" + str(setosa.head()) + "\n\n" +\
"--versicolor--\n" + str(versicolor.head()) + "\n\n" +\
"--virginica--\n" + str(virginica.head()) + "\n\n******\n")
# returns the mean for total dimension for each class
I9 = ("\nmean for setosa " + str(setosa[["totals"]].mean()) + "\n" +\
"mean for versicolor " + str(versicolor[["totals"]].mean()) + "\n" +\
"mean for virginica " + str(virginica[["totals"]].mean()) + "\n\n******\n" +\
"\nstandard deviation for setosa " + str(setosa[['totals']].std()) + "\n" +\
"standard deviation for versicolor " + str(versicolor[['totals']].std()) + "\n" +\
"standard deviation for virginica " + str(virginica[['totals']].std()) + "\n\n******\n")

text_analysis = [I1, I2, I3, I4, I5, I6, I7, I8, I9]

# function which prints all of the above info to a txt file - 'outputted_iris_data.txt'
def print_text_file():
    with open('outputted_iris_data_textfile.txt','w') as text_file:
        text_file.writelines(text_analysis)

# reorders columns so we have 'species' last as before
iris2 = iris2[['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'totals', 'mean', 'species']]

# writes updated csv file with totals and means per row
# we were getting lots of decimal places for some of the totals for some reason? 
# But <float_format='%.2f'> seems to correct it
iris2.to_csv('iris_dataset_with_totals.csv', float_format='%.2f')

# VISUALISATIONS

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
        main_menu()

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
        main_menu()

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
        main_menu()

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
        main_menu()
    
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
        main_menu()
    
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
        main_menu()
    
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
        main_menu()

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
        main_menu()

def try_again():
    a = input('do you want to check out more? y/n: ')
    if a == 'y':
        main_menu()
    else:
        print("OK bye! Hope you learned something!")

def main_menu():
    print("Please choose one of the following options:\n")
    x = input("\t\t1) Text analysis\n\
        \t2) Data visualisations\n\
        \t3) Exit\n\t\t")
    if x == '1':
        y = input("\n\tChoose from the following:\n\n\
        \t1) View the size, shape and column names\n\
        \t2) View the 1st and last 5 rows and a random sample of 5 rows\n\
        \t3) View a statistical overview of the dataset\n\
        \t4) View correlation between variables\n\
        \t5) View a statistical overview of each class\n\
        \t6) View data on each class with row totals and means\n\
        \t7) View means and standard deviation for row totals\n\
        \t8) View a complete overview of the data\n\
        \t9) Print text analysis to file\n\
        \t10) Back to main menu\n\
        \t11) Exit\n\t\t")
        if y == '1':
            print(I2)
            try_again()
        elif y == '2':
            print(I3)
            try_again()
        elif y == '3':
            print(I5)
            try_again()
        elif y == '4':
            print(I6)
            try_again()
        elif y == '5':
            print(I7)
            try_again()
        elif y == '6':
            print(I8)
            try_again()
        elif y == '7':
            print(I9)
            try_again()
        elif y == '8':
            print(I2, I3, I5, I6, I7, I8, I9)
            try_again()
        elif y == '9':
            print_text_file()
            try_again()
        elif y == '10':
            main_menu()
        elif y == '11':
            print("OK! Sorry to see you go!")
        else: 
            print('Invalid selection! Try again!')
            main_menu()

    elif x == '2':
        z = input("\nChoose from the following:\n\n\
        \t1) Heatmap\n\
        \t2) Boxplot (all classes)\n\
        \t3) Boxplots (classes separated)\n\
        \t4) Violin Plots (all classes)\n\
        \t5) Strip Plots (classes separated)\n\
        \t6) Histograms\n\
        \t7) Pairplot\n\
        \t8) Pairgrid\n\
        \t9) Back to main menu\n\
        \t10) Quit\n\t\t")
        if z == '1':
            heatmap()
            try_again()
        elif z == '2':
            boxplot_overall()
            try_again()
        elif z == '3':
            boxplot_species_separated()
            try_again()
        elif z == '4':
            violinplot_all_species()
            try_again()
        elif z == '5':
            violin_strip_plots()
            try_again()
        elif z == '6':
            histograms()
            try_again()
        elif z == '7':
            pairplot()
            try_again()
        elif z == '8':
            pairgrid()
            try_again()
        elif z == '9':
            main_menu()
        elif z == '10':
            print("OK! Sorry to see you go!")
        else:
            print('invalid selection! Try again!')
            main_menu()
    elif x == '3':
        print("OK! Sorry to see you go!")
    else:
        print('invalid selection! Try again!')
        main_menu()

print("\n************\n\nFisher's Iris dataset is a multivarate dataset named after the statistician Ronald Fisher who introduced \
it in his 1936 paper 'The Use of Multiple Measurements in Taxonic Problems' which was published in the journal \
'Annals of Eugenics'. The following is an analysis of the dataset through standard statistical methods and visualisations with the dual goal of \
gaining insight into the data and exploring the various tools available in the python language.\n\n************\n")

main_menu()