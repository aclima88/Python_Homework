# Import the necessary modules
import os
import csv
from pathlib import Path
import sys

# Specify the path where the CSV file is located
budget_data = os.path.join("/Users/angelolima/Desktop/Python_Homework/PyBank/Resources/budget_data.csv")

# Set initial variables
totalMonths = 0
totalProfitLosses = 0
averageChange = 0
greatestIncrease = 0
greatestDecrease = 0
totalChange = 0

# Open the csv file and read through each row 
with open(budget_data, "r") as financial_data:
    reader = csv.reader(financial_data, delimiter=",")

    # Skip the header
    header = next(reader)

    # Skip to row 2
    row1 = next(reader)

    # Create a previous variable to hold the change values that will be added to calculate totalChange.
    previous = int(row1[1])

    # Initialize the totalMonths variable from the first row
    totalMonths += 1

    # Initialize the totalProfitLosses variable with the value in the first row
    totalProfitLosses += int(row1[1])

    # Create a for loop to go through all rows
    for row in reader:
        
        # Add the total number of months in the spreadsheet
        totalMonths += 1

        # Add the values in the Profits/Losses column
        totalProfitLosses += int(row[1])

        # Calculate the change in profits/losses
        current = int(row[1])
        change = current - previous
        totalChange += change

        # Locate the greatest increase in profits
        if change > greatestIncrease:
            greatestIncrease = change

            # Locate the month equivalent to the greatest increase 
            greatestIncrease_index = row[0]

        # Check if the current change is less than the greatest decrease
        if change < greatestDecrease:
            greatestDecrease = change

            # Locate the month equivalent to the greatest increase 
            greatestDecrease_index = row[0]

        

        # Update the previous value for the next iteration
        previous = current

# Calculate the average change
averageChange = round(totalChange / (totalMonths - 1), 2)

print("Financial Analysis")
print("----------------------------")

# Print out the total months
print(f"Total Months: {totalMonths}")

# Print out the total profit losses
print(f"Total: ${totalProfitLosses}")

# Print out the average changes
print(f"Average Change: ${averageChange}")

# Print out the greatest increase in profit and the month when it happened
print (f"Greatest Increase in Profits: {greatestIncrease_index} (${greatestIncrease})")

# Print out the greatest decrease in profit and the month when it happened
print (f"Greatest Decrease in Profits: {greatestDecrease_index} (${greatestDecrease})")


# Save and export a text file of the output of my code
# Find the folder in which the csv file is saved and assign it to the current_dir variable
current_dir = os.path.dirname("/Users/angelolima/Desktop/Python_Homework/PyBank/analysis")

# Join the path to the folder holding the CSV file and the analysis folder and assign the path to the variable output_dir
output_dir = os.path.join(current_dir, "analysis")

# Combine the path to the output_dir folder with the string PyBankOutput.text to create a new path to the file named PyBankOutput.text and assign it to the filename variable
filename = os.path.join(output_dir, "PyBankOutput.txt")

# Use the filename variable to open the path where the output text will be stored.
with open(filename, "w") as f:

    # Redirect the standard output to the filename instead of the terminal
    sys.stdout = f

    # Write the output to the file
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {totalMonths}")
    print(f"Total: ${totalProfitLosses}")
    print(f"Average Change: ${averageChange}")
    print(f"Greatest Increase in Profits: {greatestIncrease_index} (${greatestIncrease})")
    print(f"Greatest Decrease in Profits: {greatestDecrease_index} (${greatestDecrease})")
    
    # Restore the standard output back to the terminal
    sys.stdout = sys.__stdout__