# Import the necessary modules
import os
import csv
from pathlib import Path
import pandas as pd


# Specify the path where the CSV file is located
election_data = os.path.join("/Users/angelolima/Desktop/Python_Homework/PyPoll/Resources/election_data.csv")

# Read the election data csv and store into a Pandas DataFrame
election_df = pd.read_csv(election_data, encoding="utf-8")
election_df.head() 

# Calculate the total number of votes by counting the number of times rows in the data set
totalVotes = len(election_df)

# Calculate the total votes per candidate by using the pandas method .value_counts()
# and setting the sort function to false, so it returns the candidates names in the order they appear in the dataframe
votesPerCandidate = election_df['Candidate'].value_counts(sort=False)

# Calculate the percentage of votes each candidate won
votePercentage = (votesPerCandidate / totalVotes) * 100

# Create a dataframe called voteSummary to story the votes summary then create a dictionary in the dataframe to pull the columns and the corresponding values in each column
voteSummary_df = pd.DataFrame({# Convert the 'Vote Percentage' column to a string using .astype(str) and then add the % symbol to the end of the percentage number by concatenating the "%" symbol using the '+' operator and round the output to the third decimal place
                               'Vote Percentage':votePercentage.round(3).astype(str) + '%',
                               
                               # Print the number of votes inside the () and round the total votes per candidate to the third decimal place
                               'Votes': votesPerCandidate})



# Locate the candidate with the most votes using the loc method from pandas
winner = voteSummary_df['Votes'].idxmax()

print("                    Election Analysis")
print("---------------------------------------------------")

# Print out the total number of votes cast
print(f"Total Votes: {totalVotes}")

print("---------------------------------------------------")

#Use the .to_string(header=false) method to remove the headers in the output
print(voteSummary_df.to_string(header=False))

print("---------------------------------------------------")

print("Winner:", winner)

print("---------------------------------------------------")