#!/usr/bin/env python3
import sys
import os
import csv
import numpy as np
import pandas as pd
"""
average every n rows and merge into a single row.
First row is ignored.
$ ./compress_csv.py /path/to/csv_file.csv 5
"""

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("provide CSV file and chuncks of rows to compress as argument.")
        exit()
    filename = sys.argv[1]
    n = int(sys.argv[2])
    print(f"loading CSV: {filename}, averaging every {n} rows....")

    basename = os.path.splitext(os.path.basename(filename))[0]
    data_pd = pd.read_csv(filename)
    data_np = data_pd.values
    output_np = np.zeros((data_np.shape[0]//n, data_np.shape[1]))
    for i in range(output_np.shape[0]):
        start_index = i * n
        end_index = min((i+1)*n, data_np.shape[0])
        output_np[i, :] = np.average(data_np[start_index:end_index, :], axis=0)
    output_pd = pd.DataFrame(data = output_np, columns =data_pd.columns)
    
    print(f"{data_np.shape} -> {output_np.shape}")
    output_filename = f"{basename}_compressed_{n}.csv"
    print(f"output to {output_filename}")
    output_pd.to_csv(output_filename)