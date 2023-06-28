def find_number_of_months(budget_data):

  # Finds the number of months in the CSV file.
  months = 0
  with open(budget_data, newline="") as financial_data:
    reader = csv.reader(financial_data, delimiter=",")

    # Read the header row
    header = next(reader)

    # Create empty lists to store the data from each column
    column_1 = []
    column_2 = []
    column_3 = []

    for row in reader:
      # Store the data from each column into the corresponding list
      column_1.append(row[0])
      column_2.append(row[1])
      column_3.append(row[2])

    # Find the number of months
    for row in column_1:
      if isinstance(row, str):
        if row.startswith("month"):
          months += 1

  return months

if __name__ == "__main__":
  budget_data = "budget_data.csv"
  number_of_months = find_number_of_months(budget_data)

  # Print the number of months
  print("Number of months:", number_of_months)

  # Print each column of data
  print("Column 1:", column_1)
  print("Column 2:", column_2)
  print("Column 3:", column_3)