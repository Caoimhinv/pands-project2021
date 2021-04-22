# This file contains text analysis on the Iris dataset to be used in conjunction the analysis.py program.

# Author: Caoimhin Vallely

# imports necessary modules for analysing the data
import pandas as pd
import csv

# importing my own plot functions module
import plot_functions as pf

# reads in the dataset
iris = pd.read_csv("/Users/caoimhinvallely/Desktop/Programming/Programming2021/pands-project2021/iris_dataset.csv")

# This is the initial text based exploration of the data

# Creating variables which can be saved to a txt file or called in the menu section
text_1 = ("-----FISHER'S IRIS DATASET ANALYSIS PROJECT-----\n\n"\
"------------INITIAL DATA EXPLORATION------------\n\n******\n")

# Returns the size, shape, column names, and whether there are any null values.
text_2 = ("\nSIZE() - the total number of entries in the dataset:\n" + str(iris.size) + "\n\n******\n" +\
"\nSHAPE() - the number of rows and columns:\n" + str(iris.shape) + "\n\n******\n"\
"\nCOLUMNS() - these are the column labels and the data type:\n" + str(iris.columns) + "\n\n******\n"\
"\nISNULL() - this returns if there are any null or missing values (FALSE means no null values)\n" + str(iris.isnull().values.any()) + "\n\n******\n")

# head(), tail(), sample() returns the start, end, and a random section of the dataset.
# I've chosen 6 entries - default is 5 - guess I'm just demonstrating that I know that ;)
text_3 = ("\nHEAD() - this is a printout of the first 6 rows of the dataset:\n" + str(iris.head(6)) + "\n\n******\n" +\
"\nTAIL() - this is a printout of the last 6 rows of the dataset:\n" + str(iris.tail(6)) + "\n\n******\n" +\
"\nSAMPLE() - this is a printout of a random 6 rows of the dataset:\n" + str(iris.sample(6)) + "\n\n******\n")

# this returns the number of entries per class
text_4 = ("\nVALUE_COUNTS() - this shows how many values for each class/species\n" + str(iris["species"].value_counts()) + "\n\n******\n")
iris_des = iris.describe()

# describe() gives me a table of overall analysis including count, mean, standard deviation, min, max, and 25/50/75 percentiles.
# transpose() changes the x and y of the table. I think it's easier to read this way.
text_5 = ("\nDESCRIBE() - this is a statistical overview of the dataset:\n" + str(iris_des.transpose()) + "\n\n******\n")

# This returns a table/dataframe of the correlation between the attributes
text_6 = ("\nCORR() - this shows the correlation between the variables in the data:\n" + str(iris.corr()) + "\n\n******\n")

# This creates variables for individual classes being passed through the describe() function.
set_des = iris.loc[iris['species'] == "setosa"].describe()
ver_des = iris.loc[iris['species'] == "versicolor"].describe()
vir_des = iris.loc[iris['species'] == "virginica"].describe()

# Transposed version of each is created and returned in the text.
text_7 = ("\nDESCRIBE() by class - overview with each class isolated\n" +\
"--setosa--\n" + str(set_des.transpose()) + "\n\n" +\
"--versicolor--\n" + str(ver_des.transpose()) + "\n\n" +\
"--virginica--\n" + str(vir_des.transpose()) + "\n\n******\n")

iris2 = iris.copy() # creates a new copy of the dataset to manipulate
cols = iris2.columns # creates a variable for the columns in the dataset
original_columns = iris2[cols[0:4]] # creates a variable for the first 4 columns in the dataset

# adds the totals for the first 4 columns in each row and creates a new column for the result
iris2["totals"] = original_columns.sum(axis=1)
# finds the mean for the first 4 columns in each row and creates a new column for the result
iris2["mean"] = original_columns.mean(axis=1)

# reorders columns so we have 'species' last as before
iris2 = iris2[['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'totals', 'mean', 'species']]

# creating variables for individual classes in the new dataset
set_des2 = iris2.loc[iris2["species"] == "setosa"]
ver_des2 = iris2.loc[iris2["species"] == "versicolor"]
vir_des2 = iris2.loc[iris2["species"] == "virginica"]

# the head() of each of the amended versions of each class are returned
text_8 = ("\nThe following are the first 5 rows of each class with totals and means of each row included:\n" +\
"--setosa--\n" + str(set_des2.head()) + "\n\n" +\
"--versicolor--\n" + str(ver_des2.head()) + "\n\n" +\
"--virginica--\n" + str(vir_des2.head()) + "\n\n******\n")

# returns the mean and standard deviation for total dimension for each class
text_9 = ("\nmean for setosa " + str(set_des2[["totals"]].mean()) + "\n" +\
"mean for versicolor " + str(ver_des2[["totals"]].mean()) + "\n" +\
"mean for virginica " + str(vir_des2[["totals"]].mean()) + "\n\n******\n" +\
"\nstandard deviation for setosa " + str(set_des2[['totals']].std()) + "\n" +\
"standard deviation for versicolor " + str(ver_des2[['totals']].std()) + "\n" +\
"standard deviation for virginica " + str(vir_des2[['totals']].std()) + "\n\n******\n")

# creates a variable for all text variables above
text_analysis = [text_1, text_2, text_3, text_4, text_5, text_6, text_7, text_8, text_9]


