# Import the necessary modules
import os
import csv
from pathlib import Path
from collections import Counter
import sys

# Specify the path where the CSV file is located
election_data = os.path.join("/Users/angelolima/Desktop/Python_Homework/PyPoll/Resources/election_data.csv")

# Initiate the needed variables
totalVotes = 0
candidateList = []  # Create an empty list to store the candidates' names
candidate_counts = {}
votePercentage = {}
winner = ""
winnerVotes = 0

# Open the CSV file using "read" mode.
with open(election_data, 'r') as csvfile:
    # Initialize the CSV reader
    reader = csv.reader(csvfile, delimiter=',')

    # Skip the header row
    header = next(reader)

    # Loop through the rows in the CSV file
    for row in reader:
        # Increment the total number of votes
        totalVotes += 1

        # Get the candidate name from the row and add it to the candidateList list
        candidate = row[2]
        candidateList.append(candidate)

# Count the occurrences of each candidate's name using Counter
candidate_counts = Counter(candidateList)

# Find the winner with the most votes by going inot the candidate_counts dictionary counting the number of votes each candidate won.
for candidate, count in candidate_counts.items():
        if count > winnerVotes:
            winner = candidate
            winnerVotes = count

print("                Election Analysis")
print("------------------------------------------------")

# Print out the total number of votes cast
print(f"Total Votes: {totalVotes}")

print("------------------------------------------------")

# Calculate and print the percentage of votes for each candidate
for candidate, count in candidate_counts.items():
    percentage = (count / totalVotes) * 100
    votePercentage[candidate] = percentage
    #Print the name of each candidate, the % of votes they each won and the total number of votes they each won
    print(f"{candidate}: {percentage:.3f}% ({count})")

print("------------------------------------------------")

# Print out the name of the Winner
print("Winner:", winner)

print("------------------------------------------------")



# Save and export a text file of the output of my code
# Find the folder in which the csv file is saved and assign it to the current_dir variable
current_dir = os.path.dirname("/Users/angelolima/Desktop/Python_Homework/PyPoll/analysis")

# Join the path to the folder holding the CSV file and the analysis folder and assign the path to the variable output_dir
output_dir = os.path.join(current_dir, "analysis")

# Combine the path to the output_dir folder with the string PyBankOutput.text to create a new path to the file named PyBankOutput.text and assign it to the filename variable
filename = os.path.join(output_dir, "PyBankOutput.txt")

# Use the filename variable to open the path where the output text will be stored.
with open(filename, "w") as f:

    # Redirect the standard output to the filename instead of the terminal
    sys.stdout = f
    print("                Election Analysis")
    print("------------------------------------------------")

    # Print out the total number of votes cast
    print(f"Total Votes: {totalVotes}")

    print("------------------------------------------------")

    # Calculate and print the percentage of votes for each candidate
    for candidate, count in candidate_counts.items():
        percentage = (count / totalVotes) * 100
        votePercentage[candidate] = percentage
        #Print the name of each candidate, the % of votes they each won and the total number of votes they each won
        print(f"{candidate}: {percentage:.3f}% ({count})")

    print("------------------------------------------------")

    # Print out the name of the Winner
    print("Winner:", winner)

    print("------------------------------------------------")

    # Restore the standard output back to the terminal
    sys.stdout = sys.__stdout__