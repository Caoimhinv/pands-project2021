# this is an analysis script on Fisher's iris dataset as part of 
# a project for the Programming and scripting module of HDIP in Data
# Analytics at GMIT (2021)

# This is the main script from which the program runs but it is relient
# on 2 other modules - plot_functions.py & text_analysis.py

# Author: Caoimhin Vallely

# importing pandas and csv libraries
import pandas as pd
import csv

# importing my own text analysis module
import text_analysis as t

# importing my own plot functions module
import plot_functions as pf

# A few functions to define

# This function saves all of the output from text_analysis.py to a txt file - 'outputted_iris_data.txt'
def print_text_file():
    with open('outputted_iris_data_textfile.txt','w') as text_file:
        text_file.writelines(t.text_analysis)

# function to offer user opportunity to save the new appended csv file (with totals and means per row)
# (we were getting lots of decimal places for some of the totals for some 
# reason but <float_format='%.2f'> seems to correct it!)
def print_updated_dataset():
    reply = input("Do you want to save this new dataset to file? y/n ")
    if reply == 'y':
        t.iris2.to_csv('iris_dataset_with_totals.csv', float_format='%.2f')
        try_again()
    elif reply == 'n':
        try_again()
    else:
        print("Invalid selection!")
        main_menu()

# function for use in main_menu
def try_again():
    answer = input('do you want to check out more? y/n: ')
    if answer == 'y':
        main_menu()
    elif answer == 'n':
        print("OK bye! Hope you learned something!")
    else:
        print("Presume you meant 'n'! Bye anyway!")

# function for main user menu and interface
def main_menu():
    print("Please choose one of the following options:\n")
    response1 = input("\t\t1) Text analysis\n\
        \t2) Data visualisations\n\
        \t3) Exit\n\t\t")
    if response1 == '1':
        response2 = input("\n\tChoose from the following:\n\n\
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
        if response2 == '1':
            print(t.text_2)
            try_again()
        elif response2 == '2':
            print(t.text_3)
            try_again()
        elif response2 == '3':
            print(t.text_5)
            try_again()
        elif response2 == '4':
            print(t.text_6)
            try_again()
        elif response2 == '5':
            print(t.text_7)
            try_again()
        elif response2 == '6':
            print(t.text_8)
            print_updated_dataset()
        elif response2 == '7':
            print(t.text_9)
            try_again()
        elif response2 == '8':
            print(t.text_2, t.text_3, t.text_5, t.text_6, t.text_7, t.text_8, t.text_9)
            try_again()
        elif response2 == '9':
            print_text_file()
            try_again()
        elif response2 == '10':
            main_menu()
        elif response2 == '11':
            print("OK! Sorry to see you go!")
        else: 
            print('Invalid selection! Try again!')
            main_menu()

    elif response1 == '2':
        response3 = input("\nChoose from the following:\n\n\
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
        if response3 == '1':
            pf.heatmap()
            try_again()
        elif response3 == '2':
            pf.boxplot_overall()
            try_again()
        elif response3 == '3':
            pf.boxplot_species_separated()
            try_again()
        elif response3 == '4':
            pf.violinplot_all_species()
            try_again()
        elif response3 == '5':
            pf.violin_strip_plots()
            try_again()
        elif response3 == '6':
            pf.histograms()
            try_again()
        elif response3 == '7':
            pf.pairplot()
            try_again()
        elif response3 == '8':
            pf.pairgrid()
            try_again()
        elif response3 == '9':
            main_menu()
        elif response3 == '10':
            print("OK! Sorry to see you go!")
        else:
            print('invalid selection! Try again!')
            main_menu()
    elif response1 == '3':
        print("OK! Sorry to see you go!")
    else:
        print('invalid selection! Try again!')
        main_menu()

# Main program!
# Prints a little intro
print("\n************\n\nWelcome to my analysis project on Fisher's Iris dataset. The dataset comprises measurements of Iris flowers \
and was named after the statistician Ronald Fisher who introduced it in his 1936 paper 'The Use of Multiple Measurements in Taxonic Problems'. \
The following is an analysis of the dataset through standard statistical methods and visualisations with the dual goal of \
gaining some insight into the data and exploring the various tools available in the python programming language. Please follow the menus \
to find your way around. Have fun!\n\n************\n")

# calls the main_menu() function from which everything else runs
main_menu()