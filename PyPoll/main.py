## Option 2: PyPoll
#![Vote-Counting](Images/Vote_counting.jpg)
#In this challenge, you are tasked with helping a small, rural town modernize its vote-counting process. (Up until now, Uncle Cleetus had been trustfully tallying them one-by-one, but unfortunately, his concentration isn't what it used to be.)
#You will be given two sets of poll data (`election_data_1.csv` and `election_data_2.csv`). Each dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. Your task is to create a Python script that analyzes the votes and calculates each of the following:

#* The total number of votes cast

#* A complete list of candidates who received votes

#* The percentage of votes each candidate won

#* The total number of votes each candidate won

#* The winner of the election based on popular vote.

#As an example, your analysis should look similar to the one below:

#```
#Election Results
#-------------------------
#Total Votes: 620100
#-------------------------
#Rogers: 36.0% (223236)
#Gomez: 54.0% (334854)
#Brentwood: 4.0% (24804)
#Higgins: 6.0% (37206)
#-------------------------
#Winner: Gomez
#-------------------------
#```

#Your final script must be able to handle any such similarly-structured dataset in the future 
#(i.e you have zero intentions of living in this hillbilly town -- so your script needs to work without massive re-writes). 
#In addition, your final script should both print the analysis to the terminal and export a text file with the results.

#import libraries
import os 
import csv 
from collections import Counter 

#input csv file path
csvpath = os.path.join('Data','election_data_1.csv')

#initialize variables 
date = []
election_data = [] 
vote_counter = 0 
candidates = []
candidate_count = 0 

#create lists to hold final data
final_candidates = []
final_candidate_votes = []
final_percent_of_vote = []
final_winner = []
final_source_file = []              #identifies which file the data is from 

#open csv file and read reach record 
with open(csvpath, newline="") as csvfile:
    csvreader= csv.reader(csvfile, delimiter=",")
    next(csvfile)
    for row in csvreader:
        #print(row[0])
        election_data = row
        candidates.append(row[2])
        vote_counter += 1 

    #Tally the candidates and the number of votes each recieved 
    candidate_count = Counter(candidates)

#Print results to the screen and into final lists for output
print("-------------------------")
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(vote_counter))
print("-------------------------")
for name in candidate_count.items():
    #calculate percent of total votes for each candidate
    print(str(name[0]) + ": " + str(int(name[1])/int(vote_counter)*100) + "%  (" + str(name[1]) +")")
    #Populate final lists
    final_candidates.append(name[0])
    final_candidate_votes.append(name[1])
    final_percent_of_vote.append(float(int(name[1])/int(vote_counter)*100))
    if name[0]== max(candidate_count):
        final_winner.append('Y')
    else:
        final_winner.append('N')
    #Populate final list with source path
    final_source_file.append(csvpath)
print("-------------------------")
print("Winner: " + max(candidate_count))
print("-------------------------")

#Zip lists together to create rows that will be written
election_analysis = zip(final_candidates,
                        final_candidate_votes,
                        final_percent_of_vote,
                        final_winner,
                        final_source_file)


# Set variable for output file
output_file = os.path.join("final_election_analysis.csv")
output_file_exists = os.path.isfile("final_election_analysis.csv")
#print(output_file_exists)

#  Open the output file
# using a for append when there is an existing csv file additional conditional code below to check if the file exists before writing header row
with open(output_file, "a", newline="") as datafile:
    writer = csv.writer(datafile)
    if output_file_exists == False:
        # Write the header row
        writer.writerow(["Candidate", "Total_Votes", "Percent_Of_Vote", "Winner","Source_File"])
        # Write in zipped rows
        writer.writerows(election_analysis)
    else:
        # Write in zipped rows
        writer.writerows(election_analysis)



        