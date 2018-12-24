#!/usr/bin/env python3
import csv  # CSV Module to work with these doc types
import sys  # Sys module to work in command prompt
input_file = sys.argv[1]  # First arg in command prompt after running file
output_file = sys.argv[2]  # Output arg in cmd
with open(input_file, 'r', newline='') as csv_in_file:  # Reading the file
    with open(output_file, 'w', newline='') as csv_out_file:  # Creating the out file
        filereader = csv.reader(csv_in_file, delimiter=',')  # File read
        filewriter = csv.writer(csv_out_file, delimiter=',')  # File write
        for row_list in filereader:  # Loop every row in reader
            print(row_list)  # Print
            filewriter.writerow(row_list)  # Write to new file

