"""
Created on Thu Feb 22 09:34:38 2018

@author: Debbie Chan

Vote Tallying

There are two sets of poll data (election_data_1.csv and election_data_2.csv). 
Each dataset is composed of three columns: Voter ID, County, and Candidate. 

Script that analyzes the votes and calculates each of the following:

   1) The total number of votes cast

   2) A complete list of candidates who received votes

   3) The percentage of votes each candidate won

   4) The total number of votes each candidate won

   5) The winner of the election based on popular vote.

The analysis looks similar to the one below:

Election Results
-------------------------
Total Votes: 620100
-------------------------
Rogers: 36.0% (223236)
Gomez: 54.0% (334854)
Brentwood: 4.0% (24804)
Higgins: 6.0% (37206)
-------------------------
Winner: Gomez
-------------------------
"""

# Import modules
import os 
import csv

# Open csv files for reading current employee records and open another csv file to write employee data in the required format.
csvpath = os.path.join('raw_data', 'election_data_2.csv')

# Initialize variables
candidates = []
candidateCount = 0
candidatePct = 0.00

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skip header
    next(csvreader, None)
        
    # Read through election data csv file.
    for row in csvreader:
        candidates.append(row[2])
    
    # Calculate the total number of votes cast in the poll.
    totalVotes = (len(candidates))
    
    # Get unique candidate's names for calculating individual votes and percentage
    unique_candidates = set(candidates)             

    # Initialize dictionary to store candidate's name, count, and percentage.
    tally = {}
    
    # Save individual candidate's name, count and percentage to a dictionary
    for e in unique_candidates:
        candidateCount = candidates.count(e)
        candidatePct = ( candidateCount / totalVotes ) * 100
        tally[e] = [candidatePct, candidateCount]       

    # Determine the winner of the poll
    winner = max(tally, key=tally.get)
    
    # Print results to screen
    print ('Election Results')
    print ('-' * 30)
    print ('Total Votes: ', totalVotes)
    print ('-' * 30)
    
    for e in unique_candidates:
        print (e, ': ', '{0:.1f}%'.format(tally[e][0], 1), ' (', tally[e][1], ')')
        
    print ('-' * 30)
    print ('Winner: ', winner)
    print ('-' * 30)    
    
    # Print results to a file
    with open('poll_results.txt', 'w') as f:
        print ('Election Results', file=f)
        print ('-' * 30, file=f)
        print ('Total Votes: ', totalVotes, file=f)
        print ('-' * 30, file=f)
    
        for e in unique_candidates:
            print (e, ': ', '{0:.1f}%'.format(tally[e][0], 1), ' (', tally[e][1], ')', file=f)
        
        print ('-' * 30, file=f)
        print ('Winner: ', winner, file=f)
        print ('-' * 30, file=f)    