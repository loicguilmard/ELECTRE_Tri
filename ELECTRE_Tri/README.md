# ELECTRE Tri

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/cghiaus/ELECTRE_Tri/HEAD)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/cghiaus/dm4bem_book/blob/main/LICENSE)

ELECTRE Tri-B is a Multiple-Criteria Decision-Making (MCDM) method for sorting alternatives into predefined categories delimited by base profiles. This repository contains a Python implementation of ELECTRE Tri-B, along with explanatory materials and example data files.

## Repository contents

Python module:
- `ELECTRE_Tri.py`: core functions for implementing ELECTRE Tri method.

Jupyter notebooks:
- `ELECTRE_Tri_application.ipynb`: simple application which requires only the performance matrix and criteria weights. The base profiles and the thresholds are given by default values;
- `ELECTRE_Tri_explained.ipynb`: computational explanation of ELECTRE Tri-B method.
- `ELECTRE_Tri_yours.ipynb`: sandbox for your own ELECTRE Tri-B Multiple-Criteria Decision-Making.

Data folder:
- `data/`: Folder containing example datasets from literature for use with the Jupyter notebook.

## Usage

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/cghiaus/ELECTRE_Tri/HEAD)

1. Launch mybinder.
2. Upload your data file (which describes the ELECTRE Tri-B problem) in `data` folder.
3. See the results.
