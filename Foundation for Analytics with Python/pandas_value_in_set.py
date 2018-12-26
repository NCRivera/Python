#!/usr/bin/env python3

import pandas as pd # Pandas import
import sys # Sys module import

input_file = sys.argv[1] # First arg in cmd line
output_file = sys.argv[2] # second arg in cmd

data_frame = pd.read_csv(input_file) # Cmd Line to dataframe object

important_dates = ['1/20/2014', '1/30/2014'] # if statement filter

data_frame_value_in_set = data_frame.loc[data_frame['Purchase Date'].isin\
                          (important_dates), :] # Not understanding pandas 
                                                # syntax. First arg is for 
                                                # rows, no?
data_frame_value_in_set.to_csv(output_file) # Streamlined
