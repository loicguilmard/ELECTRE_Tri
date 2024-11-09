#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 20:56:04 2021

@author: cghiaus

Simos method for determining the weights of criteria made by a classification
of cards.

Bibliograpy
1. Papathanasiou, J., Ploskas, N. (2018). Multiple criteria decision aid.
    Methods, Examples and Python Implementations, 136.Appendix: Revised Simos
    https://doi.org/10.1007/978-3-319-91648-4
    file: Papathanasiou_Ploskas_2018.pdf


2. Figueira, J., Roy, B. (2002). Determining the weights of criteria in the
    ELECTRE type methods with a revised Simos' procedure. European journal of
    operational research, 139(2), 317-326.
    https://doi.org/10.1016/S0377-2217(01)00370-8
    file: Figueira_Roy_2002.pdf

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
placement of cards ('white' represents a white card).

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
placement of cards ('white' represents a white card).
"""

import numpy as np
import pandas as pd


def criteria_weights_Simos(set_cards_file: str, z: float):
    """Simos method for weights of criteria made by classification of cards.

    Args:
        set_cards_file (str): File (.csv) with the sets of cards
        (including white cards).
        Each row contains in a cell a string representing the criterion.
        A white card is represented by 'white'.

        z (float >= 1): How many times the last criterion is more importnant
        than the first one. If there is only one rank, z = 1
        (i.e. the last criterion is as importnant as the first criterion).

    Returns:
        df (DataFrame): 2 columns: Criteria, Weight.

    **Bibliograpy**

    1. Papathanasiou, J., Ploskas, N. (2018).
        Multiple criteria decision aid.
        Methods, Examples and Python Implementations. p. 165: Revised Simos.
        https://doi.org/10.1007/978-3-319-91648-4

    2. Figueira, J., Roy, B. (2002).
        Determining the weights of criteria in the
        ELECTRE type methods with a revised Simos' procedure. European journal
        of operational research, 139(2), 317-326.
        https://doi.org/10.1016/S0377-2217(01)00370-8

    """

    # Sets with white cards included (positions)
    sets_white = pd.read_csv(set_cards_file)

    # Sets without white cards (ranks)
    sets = sets_white[~sets_white["0"].str.contains("white")]

    # number of elements in each subset
    c = sets.count(axis=1)

    # unitary ratio between two consecutive ranks
    # the range is actually z - 1
    u = round((z - 1) / len(c), 6)

    # differences e ("écarts") of indexes of non-"white" in subsets
    idx_diff = np.diff(sets.index.to_numpy())
    e = np.append(0, idx_diff)

    # Non-normalized weights
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
    return df


def main():
    """
    Test of function `criteria_weights_Simos` with 2 data sets.

    Returns
    -------
    None.

    """
    set_cards = "./data/subsets_1.csv"
    # The last subset is z = 6.5 more important than the 1st one
    z = 6.5

    df = criteria_weights_Simos(set_cards, z)

    print(f"\nResults for {set_cards} with z = {z}:")
    print(df.sort_values(by=["Criteria"]))
    print()
    print(df.sort_values(by=["Weight"]))

    set_cards = "./data/subsets_3.csv"
    # The last subset is z = 6.5 more important than the 1st one
    z = 6.5

    df = criteria_weights_Simos(set_cards, z)

    print(f"\nResults for {set_cards} with z = {z}:")
    print(df.sort_values(by=["Criteria"]))
    print()
    print(df.sort_values(by=["Weight"]))


if __name__ == "__main__":
    main()
