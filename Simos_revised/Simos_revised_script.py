#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 20:56:04 2021
Updated on Tue Apr  5 20:04:44 2022

@author: cghiaus

Simos method for determining the weights of criteria made by a classification
of cards.

Bibliograpy
1. Papathanasiou, J., Ploskas, N. (2018). Multiple criteria decision aid.
    Methods, Examples and Python Implementations, 136.Appendix: Revised Simos
    https://doi.org/10.1007/978-3-319-91648-4

2. Figueira, J., Roy, B. (2002). Determining the weights of criteria in the
    ELECTRE type methods with a revised Simos' procedure. European journal of
    operational research, 139(2), 317-326.
    https://doi.org/10.1016/S0377-2217(01)00370-8

The subsets for tests:

subsets_1 = [['b', 'd'],
             ['c'],
             ['white'],
             ['e', 'f', 'h'],
             ['white'],
             ['white'],
             ['a', 'g']]
from
Papathanasiou, J., Ploskas, N. (2018), Table A.1, page 167
8 criteria: {a, b, c, d, e, f, g, h}
grouped in 4 subsets of ex aequo with white cards between

subsets_2 = [['c', 'g', 'l'],
             ['d'],
             ['white'],
             ['b', 'f', 'i', 'j'],
             ['e'],
             ['a', 'h'],
             ['k']]
from
Figueira, J., Roy, B. (2002) Table 1 page 319
12 criteria {A, b, c, d, f, g, h, i, j, k, l}
grouped in 6 subsets of ex aequo
"""

import numpy as np
import pandas as pd

# The last subset is z = 6.5 more important than the 1st one
# parameter z
z = 6.5

# Sets with white cards included (positions)
sets_white = pd.read_csv("subsets_1.csv")


# Sets without white cards (ranks)
sets = sets_white[~sets_white["0"].str.contains("white")]

# number of elements in each subset
c = sets.count(axis=1)

# unitary ratio between two consecutive ranks
# the range is actually z - 1
u = round((z - 1) / len(c), 6)

# differences e (écarts?) of indexes of non-'white' in subsets
idx_diff = np.diff(sets.index.to_numpy())
e = np.append(0, idx_diff)

# Non-normalized weights k
k = 1 + u * np.cumsum(e)

# Normalized weights
weights = 100 / sum(c * k) * k

# Reshape the results to match each criterion with its weight
# flat sets
sets_flat = sets.stack().values

# weights expanded to correspond to number of elemnets of sets_flat
weights_expand = [c.values[i] * [weights[i]]
                  for i in range(len(c))]
# weights flatten to have a biunivocal correspondence with sets_flat
weights_flat = sum(weights_expand, [])

df = pd.DataFrame({'Criteria': sets_flat, 'Weight': weights_flat})

df.sort_values(by=["Criteria"])
df.sort_values(by=["Weight"])
