#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 22:27:21 2024

@author: cghiaus
"""

import numpy as np
import pandas as pd

import ELECTRE_Tri as et

# Set pandas to display 2 decimal places
pd.options.display.float_format = '{:.2f}'.format

data_file = '../data/performance_matrix.csv'
print("Example of data file")
A = pd.read_csv(data_file, index_col=0)
w = pd.Series({
    'C1': 0.7,
    'C2': 0.3
})

A.columns = ['C1', 'C2']

A_stat = A.agg(['mean', 'std'])

# Define scaling factors for categories
scales = np.array([-1, -0.5, 0.5, 1])  # Very Poor, Poor, Good, Very Good

# Create DataFrame B with index
B = pd.DataFrame(index=['Very Poor', 'Poor', 'Good', 'Very Good'],
                 columns=A_stat.columns)

# Calculate values for each column using broadcasting
for col in A_stat.columns:
    mean_value = A_stat.loc['mean', col]
    std_value = A_stat.loc['std', col]
    B[col] = mean_value + scales * std_value

B

# Calculate thresholds for each column
thresholds = {}
for col in B.columns:
    interval = (B[col].max() - B[col].min()) / B.shape[0]
    thresholds[col] = {
        'q': 0.10 * interval,
        'p': 0.25 * interval,
        'v': 0.50 * interval
    }

# Convert the thresholds dictionary to a DataFrame for clarity
T = pd.DataFrame(thresholds)

T

# Define scaling factors for categories
scales = np.array([-1, -0.5, 0.5, 1])  # Very Poor, Poor, Good, Very Good


opti, pessi = et.ELECTRE_Tri(A, B, T, w,
                              credibility_threshold=0.7)
print("\nOptimistic ranking:")
print(opti)

print("\nPessimistic ranking:")
print(pessi)

