#In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. 
#You will be given two sets of revenue data (`budget_data_1.csv` and `budget_data_2.csv`). 
#Each dataset is composed of two columns: `Date` and `Revenue`. 
#(Thankfully, your company has rather lax standards for accounting so the records are simple.)

#Your task is to create a Python script that analyzes the records to calculate each of the following:

#* The total number of months included in the dataset

#* The total amount of revenue gained over the entire period

#* The average change in revenue between months over the entire period

#* The greatest increase in revenue (date and amount) over the entire period

#* The greatest decrease in revenue (date and amount) over the entire period

#As an example, your analysis should look similar to the one below:

#```
#Financial Analysis
#----------------------------
#Total Months: 25
#Total Revenue: $1241412
#Average Revenue Change: $216825
#Greatest Increase in Revenue: Sep-16 ($815531)
#Greatest Decrease in Revenue: Aug-12 ($-652794)


#Your final script must be able to handle any such similarly structured dataset in the future 
#(your boss is going to give you more of these -- so your script has to work for the ones to come). 
#In addition, your final script should both print the analysis to the terminal and export a text file with the results.

import os 
import csv 
from collections import Counter 

csvpath = os.path.join('Data','budget_data_1.csv')

date = []
budget_data = [] 
total_revenue = 0
hold_date = ''
date_counter = 0 
prev_revenue = 0
revenue_change = []
hold_revenue_change = 0 

with open(csvpath, newline="") as csvfile:
    csvreader= csv.reader(csvfile, delimiter=",")
    next(csvfile)
    for row in csvreader:
        #print(row[0])
        budget_data = row
        date_list = row[0]
        revenue_list = row[1]

    #Tally number of months in budget
        #print(date_list)
        #print(revenue_list)
        if date_counter == 0:
            hold_date = date_list 
            date_counter += 1
            prev_revenue = revenue_list 
        elif hold_date != date_list:
            hold_date = date_list 
            date_counter += 1 
            #print(prev_revenue)
            revenue_change = int(revenue_list) - int(prev_revenue)
            prev_revenue = revenue_list

        #print(date_counter)
        #print(prev_revenue)
        #print(revenue_list)
        print(revenue_change)
        
        #???    why isnt this working????
        #total_revenue_change = sum(revenue_change)/len(revenue_change)


        #hold_revenue_change + revenue_change
        #hold_revenue_change = revenue_change 

    #Calculate Total_Revenue for the entire budget period 
        total_revenue = total_revenue + int(revenue_list)
        #print(str(total_revenue))

    #* The average change in revenue between months over the entire period
    #Calculate the change between months
    # new month - old month = change 
    
    #    if prev_revenue != 0.00:
    #        revenue_change = revenue_list - prev_revenue

    #hold that data in a list

    #calculate the average on the list 





        