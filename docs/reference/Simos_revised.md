<!-- markdownlint-disable -->

# <kbd>module</kbd> `Simos_revised.py`
Created on Thu Dec 16 20:56:04 2021 

Last updated on Fri Nov  8 12:37:14 2024

@author: cghiaus 

Simos method for determining the weights of criteria made by a classification of cards. 

Bibliograpy 1. Papathanasiou, J., Ploskas, N. (2018). Multiple criteria decision aid.  Methods, Examples and Python Implementations, 136.Appendix: Revised Simos  https://doi.org/10.1007/978-3-319-91648-4  file: Papathanasiou_Ploskas_2018.pdf 



2. Figueira, J., Roy, B. (2002). Determining the weights of criteria in the  ELECTRE type methods with a revised Simos' procedure. European journal of  operational research, 139(2), 317-326.  https://doi.org/10.1016/S0377-2217(01)00370-8  file: Figueira_Roy_2002.pdf 

The subsets for tests: 

.. code-block:: none

    subsets_1 = [
    ['b', 'd'],  
    ['c'],  
    ['white'],  
    ['e', 'f', 'h'],  
    ['white'],  
    ['white'],  
    ['a', 'g']
    ] 


from Papathanasiou, J., Ploskas, N. (2018), Table A.1, page 167 8 criteria: {a, b, c, d, e, f, g, h} grouped in 4 subsets of ex aequo with white cards between placement of cards ('white' represents a white card). 

.. code-block:: none

    subsets_2 = [
    ['c', 'g', 'l'],  
    ['d'],  
    ['white'],  
    ['b', 'f', 'i', 'j'],  
    ['e'],  
    ['a', 'h'],  
    ['k']
    ] 
    
from Figueira, J., Roy, B. (2002) Table 1 page 319 12 criteria {A, b, c, d, f, g, h, i, j, k, l} grouped in 6 subsets of ex aequo placement of cards ('white' represents a white card).


---

## <kbd>function</kbd> `criteria_weights_Simos`

```python
criteria_weights_Simos(set_cards_file: str, z: float)
```

Simos method for weights of criteria made by classification of cards. 



**Args:**
 
 - <b>`set_cards_file`</b> (str):  File (.csv) with the sets of cards (including white cards). Each row contains in a cell a string representing the criterion. A white card is represented by 'white'. 


 - <b>`z`</b> (float >= 1):  How many times the last criterion is more importnant than the first one. If there is only one rank, z = 1 (i.e. the last criterion is as importnant as the first criterion). 



**Returns:**
 
 - <b>`df`</b> (DataFrame):  2 columns: Criteria, Weight. 

**Bibliograpy** 

1. Papathanasiou, J., Ploskas, N. (2018). Multiple criteria decision aid. Methods, Examples and Python Implementations. p. 165:  Revised Simos. https//doi.org/10.1007/978-3-319-91648-4 

2. Figueira, J., Roy, B. (2002). Determining the weights of criteria in the ELECTRE type methods with a revised Simos' procedure. European journal of operational research, 139(2), 317-326. https//doi.org/10.1016/S0377-2217(01)00370-8 

_This file was generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
