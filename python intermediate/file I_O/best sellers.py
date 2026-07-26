import csv

# Data to be written to the CSV file
data_to_write = [
  ['Name', 'Age', 'Grade'],
  ['Alice', 25, 'A'],
  ['Bob', 22, 'B'],
  ['Charlie', 28, 'A+']
]

# Open the CSV file in 'write' mode
with open('output.csv', 'w', newline='') as file:
  # Create a CSV writer object
  csv_writer = csv.writer(file)

  # Write the data to the CSV file
  csv_writer.writerows(data_to_write)

with open('output.csv', 'r') as file:
  # Create a CSV reader object
  csv_reader = csv.reader(file)

  # Read and print the contents of the CSV file
  for row in csv_reader:
    print(row)

# Instructions
# We've all seen, perhaps bought, one of our favorite products with a "Bestseller" sticker. 🏅

# Let’s write a program to read a CSV file and find the best-selling book of all time. 🔍

# Download this CSV file of all-time bestselling books data!
# Open the Bestseller - Sheet1.csv file in "read" mode.
# Use the CSV reader to navigate through the data and find the book with the highest sales, via the sales in millions column.
# Create a new file called bestseller_info.csv with the CSV writer.
# In the new file, use .writerow() to add new CSV data.
# Up next, let’s learn about what to do in the face of the unexpected, we'll be exploring error handling.

with open('Bestseller - Sheet1.csv', 'r', encoding='utf-8') as file:
  # Create a CSV reader object
  csv_reader = csv.reader(file)
  sales = []
  for row in csv_reader:
    if row[4] != 'sales in millions':
      sales.append(float(row[4]))
  print(f'The best-selling book of all time is: {sales.index(max(sales)) + 1} with {max(sales)} million sales.')