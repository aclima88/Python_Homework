# PyBank

I imported the necessary modules.
Specified the path where the CSV file is located.
After that I defined the initial variables and set them to zero.
I then, asked the python to ppen the csv file saved in the 'Resources' folder and read through each row of the CVS file.
I instructed python to skip the header row since it doesn't contain data.
I then instructed python to skip row 1 of the CSV file and go directly to row 2, in order to be able to calculate then change of profit/losses from one month to the next.
I create a 'previous' variable to hold the change values that will be added to calculate totalChange.
I initialized the totalMonths variable from the first row to loop through all rows.
I initialized the totalProfitLosses variable with the value in the first row of the CSV file.

I created a for loop to go through all rows in the CSV file.

Inside the for loop:
I calculated the total number of months in the spreadsheet
I ihad the totalProfitLosses variable loop through the Profits/Losses column
I then calculate the change in profits/losses from one month to the next by creating a current variable that starts on row 2 of the CSV file then subtracts the value in that cell from the value of the of the cell prior to it, and loops through all cells performing this operation until it runs out of rows.
I then asked python to locate the greatest increase in profits by looping through the change values that came out of the calculation above and finding the highest of the values and find the Date row for the month equivalent to the hgihest value.
I did the same as bove for the lowest profit increase/highest profit decrease and also locate the month equivalente to that value.
I updated the value of the 'previous' variable with the new value of each change in profit calculation for the next iteration in the loop.

Outside of the foor loop:
I calculate the average change by deviding the totalChange in profits by the total number of months and rounded the return value to the second decimal point.

I then instructed python to print to the terminal, the title of the output file, the total number of months, the total profit, the average changes in profit, the greatest increase in profits and the month when it happened, and the lowest increase/highest decrease in profits and the month when it happened.

I then instructed python to export a text file with the title of the output file, the total number of months, the total profit, the average changes in profit, the greatest increase in profits and the month when it happened, and the lowest increase/highest decrease in profits and the month when it happened.
    The program did that by finding the folder where the CSV file was located and assigning the path to the 'current_dir' variable. Then joining the path to the folder holding the CSV file and the analysis folder and assigning that path to the variable 'output_dir'. After that it combined the path to the output_dir folder with the string PyBankOutput.text to create a new path to the file named PyBankOutput.text, and assigning the path to the 'filename' variable. The code then used the 'filename' variable to open the path where the output text will be stored. The sys.stdout function redirects the standard output to the 'filename' variable instead of the terminal which is the automatic location where outputs are usually printed out to. It then uses print() statements top write the output to the text file and it finishes by restoring the standard output location back to the terminal.

Joel Johnson, Ehsan Aref Adib and Andrew Hong all helped me brainstorm and troubleshoot my code. They didn't write any code for me but they were very helpful in helping me walk through the exercise and troubleshoot when I got stuck. 

Luna, one of the LAs helped me troubleshoot my code as well and helped me write the part of the code that calculates change from one month to the next, add those changes together and find the average of the changes in profit/losses.


#PyPoll

Import the necessary modules

Specify the path where the CSV file is located

Initiate the needed variables

Open the CSV file using "read" mode.
    Initialize the CSV reader

    Skip the header row

    Loop through the rows in the CSV file

        Increment the total number of votes


        Get the candidate name from the row and add it to the candidateList list


Count the occurrences of each candidate's name using Counter


Find the winner with the most votes by going inot the candidate_counts dictionary counting the number of votes each candidate won.


Print out the total number of votes cast


Calculate and print the percentage of votes for each candidate

    Print the name of each candidate, the % of votes they each won and the total number of votes they each won

Print out the name of the Winner

Save and export a text file of the output of my code
Find the folder in which the csv file is saved and assign it to the current_dir variable


Join the path to the folder holding the CSV file and the analysis folder and assign the path to the variable output_dir


Combine the path to the output_dir folder with the string PyBankOutput.text to create a new path to the file named PyBankOutput.text and assign it to the filename variable


Use the filename variable to open the path where the output text will be stored.

I received help from the LAs and used chat GPT and Google Bard to help me figure out syntax issue.
