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

#import libraries
import os 
import csv 
from collections import Counter 

#input csv file path
csvpath = os.path.join('Data','budget_data_1.csv')

#initialize variables 
date = []
budget_data = [] 
total_revenue = 0
hold_date = ''
date_counter = 0 
prev_revenue = 0
revenue_change = 0
hold_revenue_change = 0 
total_revenue_change = 0 
greatist_decrease_amt = 0 
greatist_decrease_Date = ""
greatist_increase_amt = 0 
greatist_increase_date = ""

#open csv file and read reach record 
with open(csvpath, newline="") as csvfile:
    csvreader= csv.reader(csvfile, delimiter=",")
    next(csvfile)
    for row in csvreader:
        #print(row[0])
        budget_data = row
        budget_date = row[0]
        budget_revenue = row[1]

    #Tally number of months in budget
        if date_counter == 0:
            hold_date = budget_date 
            date_counter += 1
            prev_revenue = budget_revenue
        elif hold_date != budget_date:
            hold_date = budget_date 
            #increment date counter
            date_counter += 1 
            #Calculate total Revenue change 
            total_revenue_change = total_revenue_change + (int(budget_revenue) - int(prev_revenue)) 
            if total_revenue_change < greatist_decrease_amt:
                greatist_decrease_amt = total_revenue_change
                greatist_decrease_date = budget_date 
                print("decrease " + str(greatist_decrease_date) + " " + str(greatist_decrease_amt))
            elif total_revenue_change > greatist_increase_amt:
                greatist_increase_amt = total_revenue_change
                greatist_increase_date = budget_date 
                print("inrease " + str(greatist_increase_date) + " " + str(greatist_increase_amt))
                
            #populate previous revenue 
            prev_revenue = budget_revenue
        
    #print("total revenue change: " + str(total_revenue_change))

    #Calculate average revenue change     
    average_revenue_change = total_revenue_change/(date_counter -1)
    #print("average_revenue_change")
    #print(average_revenue_change)

    
    #Calculate Total_Revenue for the entire budget period 
    total_revenue = total_revenue + int(budget_revenue)
    #print("Total_Revenue")
    #print(str(total_revenue))

    print("----------------------------")
    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: " + str(date_counter))
    print("Total_Revenue: " + str(total_revenue))
    print("Average Revenue Change:" + str(average_revenue_change))
    print("Greatist Increase in Revenue:" + str(greatist_increase_date) + " " + str(greatist_increase_amt))
    print("Greatist Decrease in Revenue:" + str(greatist_decrease_date) + " " + str(greatist_decrease_amt))

#```
#Financial Analysis
#----------------------------
#Total Months: 25
#Total Revenue: $1241412
#Average Revenue Change: $216825
#Greatest Increase in Revenue: Sep-16 ($815531)
#Greatest Decrease in Revenue: Aug-12 ($-652794)




        