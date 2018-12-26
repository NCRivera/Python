#!/usr/bin/env python3

# Importing CSV and sys module.
import csv 
import sys

# This takes the second and third argurment I passed through the command 
# prompt.
input_file = sys.argv[1]  # file name: supplier_data.csv
output_file = sys.argv[2] # file name: 4output.csv

# This contains the dates I want the rows for.
important_dates = ['1/20/2014', '1/30/2014']

# Read the file
with open(input_file, 'r', newline='') as csv_in_file: 
    # Writes to file
    with open(output_file, 'w', newline='') as csv_out_file: 
        filereader = csv.reader(csv_in_file)  # Reader Object
        filewriter = csv.writer(csv_out_file) # Writer Object
        header = next(filereader) # Reads the first line, can use readline().
        filewriter.writerow(header) # Writing the column names manually
        for row_list in filereader: # For Loop
            a_date = row_list[4] # will be used to check the row
            if a_date in important_dates:
                filewriter.writerow(row_list) # Write if condition TRUE