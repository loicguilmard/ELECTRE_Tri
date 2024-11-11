#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 11:11:11 2024

@author: cghiaus

ELECTRE Tri with 4 default base profiles for 5 categories.
"""
import pandas as pd

import sys
import os

# Get the path to the parent directory /../..
parent_dir = os.path.dirname(           # dir of dir of file
    os.path.dirname(                    # directory of current file
        os.path.abspath(__file__)))     # absolute path to current file

# Add the parent directory to sys.path
sys.path.append(parent_dir)


from src import electre_tri as et


# Problem statement
data_file = "../data/bldg_retrofit_level.csv"
credibility_threshold = 0.7

# Problem solving
A, L, w = et.read_electre_tri_extreme_base_profile(data_file)
B = et.base_profile(L, n_base_profile=2)
T = et.threshold(B)

optimistic, pessimistic = et.electre_tri_b(A, B, T, w,
                                           credibility_threshold)


# Optimistic sorting
opti_sort = et.sort(optimistic)
print('Optimistic sorting')
print(opti_sort.to_frame(name="alternatives").rename_axis("categories"))


# Pessimistic sorting
pessi_sort = et.sort(pessimistic)
print('Pessimistic sorting')
print(pessi_sort.to_frame(name="alternatives").rename_axis("categories"))

# data_file = '../data/default_categories.csv'
# print("Example of data file")
# A = pd.read_csv(data_file, index_col=0)

# A, L, w = et.read_electre_tri_extreme_base_profile(data_file)
# B = et.base_profile(L)
# T = et.threshold(B)

# opti, pessi = et.electre_tri_b(A, B, T, w,
#                              credibility_threshold=0.7)
# print("\nOptimistic ranking:")
# print(opti)

# print("\nPessimistic ranking:")
# print(pessi)

# print('Optimistic sorting')
# print(et.sort(opti).to_frame(name="alternatives").rename_axis("categories"))

# print('Pessimistic sorting')
# print(et.sort(pessi).to_frame(name="alternatives").rename_axis("categories"))
