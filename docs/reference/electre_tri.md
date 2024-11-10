<!-- markdownlint-disable -->

# <kbd>module</kbd> `ELECTRE_Tri_B.py`
Created on Fri Oct 11 19:24:18 2024 

Last modified on Tue Oct 29 10:39:45 2024 

@author: cghiaus 

ELECTRE Tri-B 

In ELECTRE Tri-B each category is characterized by two reference profiles corresponding to the limits of this category. In contrast, in ELECTRE Tri-C each category is characterized by one reference profile only, being representative of the category [Corente et al; 2016]. 

__References__

Almeida-Dias, J., Figueira, J. R., & Roy, B. (2010). Electre Tri-C: A multiple criteria sorting method based on characteristic reference actions. European Journal of Operational Research, 204(3), 565-580. https://doi.org/10.1016/j.ejor.2009.10.018 https://hal.science/hal-00907583v1/document 

Mousseau, V., Slowinski, R., & Zielniewicz, P. (1999). ELECTRE TRI 2.0 Methodological guide and user’s manual. Universite Paris Dauphine, Document du LAMSADE, 111, 263-275. https://www.lamsade.dauphine.fr/mcda/biblio/PDF/mous3docl99.pdf 

Mousseau, V., Slowinski, R., & Zielniewicz, P. (2000). A user-oriented implementation of the ELECTRE-TRI method integrating preference elicitation support. Computers & operations research, 27(7-8), 757-777. https://doi.org/10.1016/S0305-0548(99)00117-3 https://www.lamsade.dauphine.fr/mcda/biblio/PDF/mous3cor00.pdf 

J. Almeida-Dias , J. R. Figueira , B. Roy (2010) A multiple criteria sorting method defining each category by several characteristic reference actions: The Electre Tri-nC method, Cahier du LAMSADE 294, Université Paris Daufine, CNRS https://hal.science/hal-01511223/document 

Corrente, S., Greco, S., & Słowiński, R. (2016). Multiple criteria hierarchy process for ELECTRE Tri methods. European Journal of Operational Research, 252(1), 191-203. https://doi.org/10.1016/j.ejor.2015.12.053 https://pure.port.ac.uk/ws/portalfiles/portal/5001301/GRECO_Multiple_Criteria_Hierarchy_Process_for_ELECTRE_Tri_methods_Postprint.pdf 

Figueira, J. R., Mousseau, V., & Roy, B. (2016). ELECTRE methods. Multiple criteria decision analysis: State of the art surveys, 155-185. https://www.lamsade.dauphine.fr/mcda/biblio/PDF/JFVMBR2005.pdf 

Corrente, S., Greco, S., & Słowiński, R. (2016). Multiple criteria hierarchy process for ELECTRE Tri methods. European Journal of Operational Research, 252(1), 191-203. https://doi.org/10.1016/j.ejor.2015.12.053 https://pure.port.ac.uk/ws/portalfiles/portal/5001301/GRECO_Multiple_Criteria_Hierarchy_Process_for_ELECTRE_Tri_methods_Postprint.pdf 

Baseer, M., Ghiaus, C., Viala, R., Gauthier, N., & Daniel, S. (2023). pELECTRE-Tri: Probabilistic ELECTRE-Tri Method—Application for the Energy Renovation of Buildings. Energies, 16(14), 5296. https://doi.org/10.3390/en16145296 


---

## <kbd>function</kbd> `read_electre_tri_data`

```python
read_electre_tri_data(filename)
```

Reads the data of the ELECTRE Tri problem. 



**Args:**
 
 - <b>`filename`</b> (str):  Name of .csv file containing the data of the problem. 



**Returns:**
 
 - <b>`A`</b> (DataFrame):  Performance matrix of alternatives (rows) for criteria (columns). 


 - <b>`B`</b> (DataFrame):  Base profiles in ascending order for criteria (columns). 


 - <b>`T`</b> (DataFrame):  Indifference (q), preference (p) and veto (v) thresholds for each criterion (column). 


 - <b>`w`</b> (Series):  Weight for each criterion. 

Example 
------- 

```python
data_file = './data/simple_example.csv'
A, B, T, w = read_electre_tri_data(data_file) 
...
```

where `simple_example.csv` is:

```
    type, profile, c1, c2
    A,    a1,     8.5, 18
    A,    a2,      14, 16
    A,    a3,       5, 27
    B,    b1,      10, 15
    B,    b2,      15, 20
    T,     q,       1, 2
    T,     p,       2, 4
    T,     v,       4, 8
    w,      ,     0.7, 0.3
```


---

## <kbd>function</kbd> `read_electre_tri_extreme_base_profile`

```python
read_electre_tri_extreme_base_profile(filename)
```

Reads the data for worst and best possible base profiles. 



**Args:**
 
 - <b>`filename`</b> (str):  Name of .csv file containing the data of the problem. 



**Returns:**
 
 - <b>`A`</b> (DataFrame):  Performance matrix of alternatives (rows) for criteria (columns). 


 - <b>`L`</b> (DataFrame):  Worst and best base profiles in ascending order for criteria (columns). 


 - <b>`w`</b> (Series):  Weight for each criterion. 


---

## <kbd>function</kbd> `base_profile`

```python
base_profile(L, n_base_profile=4)
```

Base profiles for each criterion. 

The range between the best and the worst possible levels `L` is divided in equidistant `n_base_profile` resulting in `n_base_profile + 1` categories. 



**Args:**
 
 - <b>`L`</b> (DataFrame):  Worst and best possible base profiles in ascending order for criteria (columns). 


 - <b>`n_base_profile`</b> (int, optional):  Number of base profiles. Defaults to 4. 



**Returns:**
 
 - <b>`B`</b> (DataFrame):  Base profiles in ascending order for criteria (columns). 


---

## <kbd>function</kbd> `threshold`

```python
threshold(B, threshold_percent=[0.1, 0.25, 0.5])
```

Indifference (q), preference (p), and veto (v) thresholds as a percentage of the range between two consecutive equidistant base profiles. 



**Args:**
 
 - <b>`B`</b> (DataFrame):  Base profiles in ascending order for criteria (columns). 


 - <b>`threshold_percent`</b> (list, optional):  Values of indifference (q), preference (p) and veto (v) thresholds as a percentage of the range between two consecutive equidistant base profiles. Defaults to [0.10, 0.25, 0.50]. 



**Returns:**
 
 - <b>`T`</b> (DataFrame):  Indifference (q), preference (p) and veto (v) thresholds for each criterion (column). 


---

## <kbd>function</kbd> `partial_concordance`

```python
partial_concordance(A, B, T)
```

Partial concordance between profiles `a` and `b` for each criterion `c`. 

Truth value (between 0 and 1) of the concordance (i.e. agreement) with the statement:  *a outranks b for criterion c* where "outranks" means "is at least as good as". 

In ELECTRE Tri, two partial concordances are calculated: 
    - between alternatives a and base profiles b; 
    - between base profiles b and alternatives a. 





**Args:**
 
 - <b>`A`</b> (DataFrame):  Performance matrix of alternatives (rows) for criteria (columns). 


 - <b>`B`</b> (DataFrame):  Base profiles in ascending order for criteria (columns). 


 - <b>`T`</b> (DataFrame):  Indifference (q), preference (p) and veto (v) thresholds for each criterion (columns). 



**Returns:**
 
 - <b>`con_ab`</b> (DataFrame):  Partial (or local) concordance between alternatives `a` and base profiles `b` for each criterion `c`. con_ab has `criteria` and `base` as indexes and `alternatives` as columns. 


 - <b>`con_ba`</b> (DataFrame):   Partial (or local) concordance between base profiles `b` and alternatives `a` for each criterion `c`. con_ba has `criteria` and `base` as indexes and `alternatives` as columns.. 

Let's note: 
    - a : value of alternative a for a given criterion c 
    - b : value of base b for the same criterion c 
    - q : indifference threshold of b for criterion c 
    - p : preference threshold of b for criterion c 

Partial concordance between a and b, con_ab, is: 
    - = 1, if a >= b - q 
    - = 0, if a < b - p 
    - = (a - b + p) / (p - q), otherwise 

Partial concordance between b and a, con_ab, is: 
    - = 1, if b >= a - q 
    - = 0, if b < a - p 
    - = (b - a + p) / (p - q), otherwise 



Example 
------- 

For `data_file.csv`: 

```
    type, profile, c1, c2
    A,    a1,     8.5, 18
    A,    a2,      14, 16
    A,    a3,       5, 27
    B,    b1,      10, 15
    B,    b2,      15, 20
    T,     q,       1, 2
    T,     p,       2, 4
    T,     v,       4, 8
    w,      ,     0.7, 0.3
```


Partial concordance between alternatives and base profiles, `con_ab`: 

|          |      | a1  | a2  | a3  |
|----------|------|-----|-----|-----|
| criteria | base |     |     |     |
| c1       | b1   | 0.5 |  1  | 0   |
|          | b2   | 0   |  1  | 0   |
| c2       | b1   | 1   |  1  | 1   |
|          | b2   | 1   |  0  | 1   |

Consider column a1: 

con_ab[(c1, b1), a1] = 0.5 means that it is partly true that a1 outranks b1 on criterion c1, i.e., on c1, a1 is between indifference (b1 - q ) and preference (b1 - p) boundaries of b1. 

con_ab[(c1, b2), a1] = 0 means that it not true that a1 outranks b2 on criterion c1, i.e., on c1, a1 is bellow preference boundary of b1, b1 - p. 

con_ab[(c2, b2), a1] = 1 means that it true that a1 outranks b1 on criterion c2, i.e., on c2, a1 is above indifference boundary of b1, b1 - q. 



Partial concordance between base profiles and alternatives, `con_ba`:

|          |      | a1  | a2  | a3  |
|----------|------|-----|-----|-----|
| criteria | base |     |     |     |
| c1       | b1   | 1   | 0   | 1   |
|          | b2   | 1   | 1   | 1   |
| c2       | b1   | 0.5 | 1   | 0   |
|          | b2   | 1   | 1   | 0   |

Consider row (c2, b1): 

con_ab[(c2, b1), a1] = 0.5 means that it is partly true that b1 outranks a1 on criterion c2, i.e., on c1, b1 is between indifference (a1 - q ) and preference (a1 - p) boundaries of a1. 

con_ab[(c2, b1), a2] = 1 means that it true that b1 outranks a2 on criterion c2, i.e., on c2, b1 is above indifference boundary of a1, a1 - q. 

con_ab[(c2, b1), a3] = 0 means that it not true that b1 outranks a3 on criterion c2, i.e., on c2, b1 is bellow preference boundary of a3, a3 - p. 


---

## <kbd>function</kbd> `discordance`

```python
discordance(A, B, T)
```

Partial discordance between profiles `a` and `b` for each criterion `c`. 

Truth value (between 0 and 1) of the discordance (i.e. disagreement) with the statement:  *a outranks b for criterion c* where "outranks" means "is at least as good as". 





**Args:**
 
 - <b>`A`</b> (DataFrame):  Performance matrix of alternatives (rows) for criteria (columns). 


 - <b>`B`</b> (DataFrame):  Base profiles in ascending order for criteria (columns). 


 - <b>`T`</b> (DataFrame):  Indifference (q), preference (p) and veto (v) thresholds for each criterion (columns). 



**Returns:**
 
 - <b>`dis_ab`</b> (DataFrame):  Partial (or local) discordance between alternatives `a` and base profiles `b` for each criterion `c`. d_ab has `criteria` and `base` as indexes and `alternatives` as columns. 


 - <b>`dis_ba`</b> (DataFrame):  Partial (or local) discordance between base profiles `b` and alternatives `a` for each criterion `c`. d_ba has `criteria` and `base` as indexes and `alternatives` as columns. 

Let's note: 
    - a : value of alternative a for a given criterion c 
    - b : value of base b for the same criterion c 
    - q : indifference threshold of b for criterion c 
    - p : preference threshold of b for criterion c 

Partial concordance between a and b, con_ab, is: 
    - = 1, if a >= b - q 
    - = 0, if a < b - p 
    - = (a - b + p) / (p - q), otherwise 

Partial concordance between b and a, con_ab, is: 
    - = 1, if b >= a - q 
    - = 0, if b < a - p 
    - = (b - a + p) / (p - q), otherwise 

Example 
------- 

For `data_file.csv`: 

```
    type, profile, c1, c2
    A,    a1,     8.5, 18
    A,    a2,      14, 16
    A,    a3,       5, 27
    B,    b1,      10, 15
    B,    b2,      15, 20
    T,     q,       1, 2
    T,     p,       2, 4
    T,     v,       4, 8
    w,      ,     0.7, 0.3
```

Partial discordance between alternatives and base profiles, `dis_ab`: 

|          |      | a1  | a2  | a3  |
|----------|------|-----|-----|-----|
| criteria | base |     |     |     |
| c1       | b1   | 0   | 0   | 1   |
|          | b2   | 1   | 0   | 1   |
| c2       | b1   | 0   | 0   | 0   |
|          | b2   | 0   | 0   | 0   |

Consider column a1: 

dis_ab[(c1, b1), a1] = 0 means that it not true that a1 is worse than b1 on criterion c1, i.e., on c1, a1 is above preference boundary of b1, b1 - p. 

con_ab[(c1, b2), a1] = 1 means that it true that a1 is worse that b2 on criterion c1, i.e., on c1, a1 is bellow indifference boundary of b1, b1 - v 

Partial discordance between base profiles and alternatives, `dis_ba`: 

|          |      | a1  | a2  | a3   |
|----------|------|-----|-----|------|
| criteria | base |     |     |      |
| c1       | b1   | 0   | 1   | 0    |
|          | b2   | 0   | 0   | 0    |
| c2       | b1   | 0   | 0   | 1    |
|          | b2   | 0   | 0   | 0.75 |

Consider row (c2, b2): 

dis_ba[(c2, b2), a3] = 0 means that it not true that b2 is worse than a3 on criterion c2, i.e., on c2, b2 is above preference boundary of a3, a3 - p. 

dis_ba[(c2, b2), a3] = 0.25 means that it is partly true that b2 is worse than a1 on criterion c2, i.e., on c2, b2 is between preferrence (a1 - p ) and veto (a1 - v) boundaries of a1. 


---

## <kbd>function</kbd> `global_concordance`

```python
global_concordance(c, w)
```

Global concordance between profiles `a` and `b`. 

Truth value (berween 0 and 1) of the statement:  *a outranks b globlly, i.e. for all criteria* where "outranks" means "is at least as good as". 





**Args:**
 
 - <b>`c`</b> (DataFrame):  Partial (or local) concordance between two profiles (a, b) for all criteria. 


 - <b>`w`</b> (Series):  Weights of criteria. 



**Returns:**
 
 - <b>`C`</b> (DataFrame):  Global concordance between two profiles. 

The global concordance index is the sum of weighted partial concordances divided by the sum of the weights. 

Example 
------- Given partial concordance between alternatives and base profiles, `c_ab`: 

|          |      | a1  | a2  | a3  |
|----------|------|-----|-----|-----|
| criteria | base |     |     |     |
| c1       | b1   | 0.5 |  1  | 0   |
|          | b2   | 0   |  1  | 0   |
| c2       | b1   | 1   |  1  | 1   |
|          | b2   | 1   |  0  | 1   |

and the weights w: 

|   |    | c1  | c2  |
|---|----|-----|-----|
| w |    | 0.7 | 0.3 |

the global concordance C_ab is: 

|         |  a1  |  a2  |  a3  |
|---------|------|------|------|
|  base   |      |      |      |
|   b1    | 0.65 | 1.0  | 0.3  |
|   b2    | 0.3  | 0.7  | 0.3  |

C[b1, a1] = (0.7 * 0.5 + 0.3 * 1) = 0.65 


---

## <kbd>function</kbd> `credibility_index`

```python
credibility_index(C, d)
```

Credibility of the assertion "a outranks b". 

Credibility index σ(a,b) corresponds to the concordance index C(a,b) weakened by discorcdances d(a, b): 

 When no criterion shows strong opposition (discordance) to the  outranking relation, the credibility index is equal to the global  concordance. 

 When a discordant criterion opposes a veto to the assertion  ”a outranks b" (i.e. discordance is 1), then credibility index σ(a,b)  becomes null (the assertion ”a outranks b" is not credible at all). 

 When one or more criteria strongly oppose the outranking relation  (i.e., their discordance exceeds the global concordance),  the credibility index is reduced by multiplying the global concordance  by a factor derived from the discordances that exceed the global  concordance.  The formula for this correction involves a product of terms,  each representing the effect of a discordant criterion. 

This approach ensures that strong opposition on even a single criterion can significantly reduce the credibility of the outranking relation, reflecting the non-compensatory nature of ELECTRE methods. 

The credibility index provides a nuanced measure of the strength of the outranking relation by taking into account performance on both supporting and opposing criteria. 



**Args:**
 
 - <b>`C`</b> (DataFrame):  Global concordance. 


 - <b>`d`</b> (DataFrame):  Discordance. 



**Returns:**
 
 - <b>`sigma`</b> (DataFrame):  Credibility index. 

Example 
------- 

Global concordance `C_ba`: 

|         |  a1  |  a2  |  a3  |
|---------|------|------|------|
|  base   |      |      |      |
|   b1    | 0.85 | 0.3  | 0.7  |
|   b2    | 1.0  | 1.0  | 0.7  |

Discordance between base profiles and alternatives, `d_ba`: 

|          |      | a1  | a2  | a3   |
|----------|------|-----|-----|------|
| criteria | base |     |     |      |
| c1       | b1   | 0   | 1   | 0    |
|          | b2   | 0   | 0   | 0    |
| c2       | b1   | 0   | 0   | 1    |
|          | b2   | 0   | 0   | 0.75 |

Obtained credibility index `sigma_ba`: 

|         |  a1  |  a2  |  a3  |
|---------|------|------|------|
|  base   |      |      |      |
|   b1    | 0.85 |  0   |  0   |
|   b2    |  1   |  1   | 0.583|

sigma_ba[b1, a1] = C_ba[b1, a1] because d_ba[b1, a1] = 0. 

sigma_ba[b1, a2] = C_ba[b1, a2] because d_ba[b1, a1] = 1. 

sigma_ba[b2, a3] = 

C_ba[b2, a3] * (1 - d_ba[(c2, b2), a3]) /  (1 - C_ba[b2, a3]) = 

0.7 * (1 - 0.75)/(1 - 0.7) = 0.583 

because d_ba[(c2, b2), a3] = 0.8 > C_ba[b2, a3] = 0.7 

and the other dscordances are 0 or smaller than the global concordances. 


---

## <kbd>function</kbd> `outrank`

```python
outrank(sigma_ab, sigma_ba, credibility_threshold)
```

Preference relation between alternatives and base profiles. 

Four outranking (preference) relations are defined: 


- σ(a,b) < λ and σ(b,a) ≥ λ  ⇒ a I b, "a is indifferent to b" 
- σ(a,b) ≥ λ and σ(b,a) ≥ λ  ⇒ a ≻ b, "a is preferred to b" 
- σ(a,b) < λ and σ(b,a) < λ  ⇒ a ≺ b, "a is not preferred to b" 
- σ(a,b) ≥ λ and σ(b,a) < λ  ⇒ a R b, "a is incomparable with b" 

 where λ is a cutting level, i.e. the smallest value  of the  credibility index compatible with the  assertion ”a outranks b", i.e., σ(a, b) ≥ λ ⇒ a > b. 

a ≻ b, "a outranks b", i.e. "a is as least as good as b", means that a is preferred to b. 

a ≺ b, "a is not preferred to b", i.e. "a is not as least as good as b", means that a is not preferred to b. 

a I b, "a is indifferent to b" means that the performances of the alternative a and of the base profile b are considered equivalent or close enough that no clear preference can be established between them. 

a R b, "a is incomparable with b" means that there is not enough evidence to estabish preference or indifference between profiles. This is typically the case when an alternative a outranks the base profile b on some criteria and the base profile b outranks the alternative a on other criteria. 



**Args:**
 
 - <b>`sigma_ab`</b> (DataFrame):  Credibility index that alternative a outranks base profile b. 


 - <b>`sigma_ba`</b> (DataFrame):  Credibility index that base profile b ouranks alternative a. 


 - <b>`credibility_threshold`</b> (float):  Credibility threshold is a minimum degree of credibility index that is considered necessary to validate the statement "alternative a outranks base profile b". It takes a value within the range [0.5, 1], typically 0.75. 



**Returns:**
 
 - <b>`outranking`</b> (DataFrame):  Preference relations: ≻, ≺, I, R between base profiles (rows) and alternatives (columns). 

Example 
------- 

credibility index `sigma_ab`: 

|         |  a1  |  a2  |  a3  |
|---------|------|------|------|
|  base   |      |      |      |
|   b1    | 0.65 |  1   |  0   |
|   b2    |  0   |  0.7 |  0   |

credibility index `sigma_ba`: 

|         |  a1  |  a2  |  a3  |
|---------|------|------|------|
|  base   |      |      |      |
|   b1    | 0.85 |  0   |  0   |
|   b2    |  1   |  1   | 0.583|

credibility_threshold = 0.7 

outranking 

|         |  a1  |  a2  |  a3  |
|---------|:----:|:----:|:----:|
|  base   |      |      |      |
|   b1    |   ≻  |  ≺   |  R   |
|   b2    |  ≻   |  I   |  R   |

---

## <kbd>function</kbd> `classify`

```python
classify(outranking)
```

Optimistic and pessimistic classification. 

These classification procedures are used to assign alternatives to ordered categories separated by base profiles. They utilize outranking relations: 
     - preferred "≻" 
     - not preferred "≺" 
     - indifferent "I" 
     - incomparable "R" 

between the alternatives and the base profiles: 


    -The optimistic procedure increases the level of base profiles till  the lowest base profile which is "preferred" to alternative (b ≻ a)  is found.  The alternative is assigned to the category having this base as upper  bound. If no base is "preferred", the alternative is assigned to  the category above the highest base profile. 


    -The pesimestic procedure decreases the level of base profiles till  a base profile which is "not preferred" to alternative (b ≺ a)  is found.  The alternative is assigned to the category having this base as lower  bound. If no base is "not preferred", the alternative is assigned to  the category below the lowest base profile 

When the outranking relation between base and alternative is only of "preferrence" ("b ≻ a" or "b ≺ a"), the classification of the alternative gives the same result with optimistic and pessimistic procedure. For example, consider the outranking relation b = ["≺", "≺", "≻", "≻", "≻", "≻"] for an alternative a. Both classifications (optimistic and pessimistic) classify alternative a in (b1, b2), a ∈ (b1, b2). 

When the outranking relation between alternative and base is of "indifference" ("I") or "incomparable" ("R"), the pessimmistic procedure assigns the alternative in a lower category than the optimistic procedure. For example, consider the outranking relation b = ["≺", "≺", "I", "R", "≻", "≻"] for an alternative a. Optimistic classification starts from b[0] = "≺" and increases the index of b till b[4] = "≻". The alternative is classified in (b3, b4), a ∈ (b3, b4). Pessimstic classification starts from b[-1] = "≻" and decreases the index of b till b[1] = "≺". The alternative is classified in (b1, b2), a ∈ (b1, b2). 



**Args:**
 
 - <b>`outranking`</b> (DataFrame):  Preference relations: ≻, ≺, I, R between base profiles (index) and alternatives (columns). 



**Returns:**
 
 - <b>`opti`</b> (DataFrame):  Optimistic classification matrix. 


 - <b>`pessi`</b> (DataFrame):  Pessimistic classification matrix. 

Called Functions 
---------------- create(outranking) : Creates the categories (separated by base profiles) and an empty matrix of classification. optimistic_classification(outranking) : Optimistic classification (ascending rule). pessimistic_classification(outranking): Pessimistic classification (descending rule). 


---

## <kbd>function</kbd> `sort`

```python
sort(class_matrix)
```

Classes (in ascending order) and alternatives that are in each class. 



**Args:**
 
 - <b>`class_matrix`</b> (DataFrame):  Matrix of (optimistic or pessimesitc) classification obtained by using classify(). 



**Returns:**
 
 - <b>`Series`</b>:  classes (categories) with boundaries the base profiles (index); list of alternatives in each class (values). 


---

## <kbd>function</kbd> `rank`

```python
rank(class_matrix)
```

Alternative and the class to which it belongs. 



**Args:**
 
 - <b>`class_matrix`</b> (DataFrame):  Matrix of (optimistic or pessimesitc) classification obtained by using classify(). 



**Returns:**
 
 - <b>`Series`</b>:  Alternaitves, e.g. 'a1', 'a2' (index) and the class (category) to which the alternative bellongs, e.g. '< b1', '∈ (b1, b2)' (values). 


---

## <kbd>function</kbd> `electre_tri_b`

```python
electre_tri_b(A, B, T, w, credibility_threshold)
```

ELECTRE Tri-B workflow. 

All criteria are in ascending order, i.e., higher values are better (e.g. efficiency). For criterian that need to be minimised (e.g. cost): 
    - use sign inversion for values of alternatives and base profiles. 
    - do not use sign inversion for thresholds and weights. 

The base profiles need to be in ascending order. 

The steps of ELECTRE Tri-B method are: 
    - Calculate partial concordance, discordance, and global concordance. 
    - Assess the credibility for the outranking between: 
        - alternatives `a` and base profiles `b`; 
        - base profiles `b` and alternatives `a`. 
    - Outrank the alternatives. 
    - Classify the alternatives. 



**Args:**
 
 - <b>`A`</b> (DataFrame):  Matrix of performance of alternatives (on rows) for criteria (on columns). Multiply by -1 for citeria to be minimised. 


 - <b>`B`</b> (DataFrame):  Matrix of base profiles organized in ascending order. Base profiles are on rows and criteria on columns. Multiply by -1 for citeria to be minimised. 


 - <b>`T`</b> (DataFrame):  Matrix of thresholds: 
        - q : indifference, 
        - p : preference, 
        - v  :veto. The thresholds are for each criterion. Do not multiply by -1 for citeria to be minimised. 


 - <b>`w`</b> (DataFrame):  Vector of weights for each criterion. Do not multiply by -1 for citeria to be minimised. 


 - <b>`credibility_threshold`</b> (float):  Thershold between 0.5 and 1 (typically 0.75) to be used for the credibility of outranking. 



**Returns:**
 
 - <b>`optimistic`</b> (DataFrame):  Optimistic ranking DataFrame with index for categories and columns for alternatives. Values are NaN or 1. Value 1 indicates the category in which is an alternative. There is only one value of 1 per row and per colum, i.e. an alternative belongs to one and only one category. 


 - <b>`pessimistic`</b> (DataFrame):  Pessimistic ranking DataFrame with index for categories and columns for alternatives. Values are NaN or 1. Value 1 indicates the category in which is an alternative. There is only one value of 1 per row and per colum, i.e. an alternative belongs to one and only one category. 

Tha data of the problem can be read from a data file using read_electre_tri_data(filename). The `filename = "data_file.csv"` contains the follwong matrices and vector with columns representing criteria: 
    - A : matrix of performance of alternatives. 
    - B : matrix of base profiles organized n ascending order. 
    - T : matrix of thresholds: 
        - q : indifference, 
        - p : preference, 
        - v  :veto. 
    - w : vector of weights for each criterion. 

```python
A, B, T, w = read_electre_tri_data(data_file)
opti, pessi = ELECTRE_Tri(A, B, T, w, credibility_threshold=0.7)
```


where `data_file.csv` is: 

```
type, profile, c1, c2
A,    a1,     8.5, 18
A,    a2,      14, 16
A,    a3,       5, 27
B,    b1,      10, 15
B,    b2,      15, 20
T,     q,       1, 2
T,     p,       2, 4
T,     v,       4, 8
w,      ,     0.7, 0.3 
```

---

## <kbd>function</kbd> `electre_tri_equidistant_profiles`

```python
electre_tri_equidistant_profiles(
    data_file,
    n_base_profile=4,
    threshold_percent=[0.1, 0.25, 0.5],
    credibility_threshold=0.75
)
```

ELECTRE Tri-B workflow for base profiles from worst/best profiles. 

Workflow 
-------- 

Given: 
    - performance matrix, A 
    - level of worst and best possible base profiles, L 
    - weights of criteria, w 

Calculate: 
    - base profiles, B 
    - theresholds, T 

Perform: ELECTRE_Tri(A, B, T, w, credibility_threshold) 



**Args:**
 
 - <b>`data_file`</b> (str):  Name of .csv file containing the data of the problem (performance of alternatives A, worst/best possible base levels L, and weights w). 


 - <b>`n_base_profile`</b> (int, optional):  Number of equidistant base profiles between worst and best possible. Defaults to 4. 


 - <b>`threshold_percent`</b> (list, optional):  Percentage of the range between base profiles for veto v, preferrence p, and indifference p thresholds. Defaults to [0.10, 0.25, 0.50]. 


 - <b>`credibility_threshold`</b> (float, optional):  Thershold between 0.5 and 1 (typically 0.75) to be used for the credibility of outranking. Defaults to 0.75. 



**Returns:**
 
 - <b>`optimistic`</b> (DataFrame):  Optimistic ranking DataFrame with index for categories and columns for alternatives. Values are NaN or 1. Value 1 indicates the category in which is an alternative. There is only one value of 1 per row and per colum, i.e. an alternative belongs to one and only one category. 


 - <b>`pessimistic`</b> (DataFrame):  Pessimistic ranking DataFrame with index for categories and columns for alternatives. Values are NaN or 1. Value 1 indicates the category in which is an alternative. There is only one value of 1 per row and per colum, i.e. an alternative belongs to one and only one category. 

Example 
------- 

```python
data_file = './data/default_categories.csv'
opti, pessi = ELECTRE_Tri_equidistant_profiles(``` ...    data_file, ...    n_base_profile=4, ...    threshold_percent=[0.10, 0.25, 0.50], ...    credibility_threshold=0.7) 
```



where `default_categories.csv` is: 

```

type, profile,                 Saving/(kWh/m²/year), Cost/(€/m²) 
A,    a1:  Basic renovation,                      50, -100 
A,    a2:  Moderate renovation,                   80, -200 
A,    a3:  Extensive renovation,                 120, -350
L,    worst,                                      0, -400
L,    best,                                     150,  -50
w,   ,                                            0.7,  0.3 
```

---

## <kbd>function</kbd> `plot_alternatives_vs_base_profile`

```python
plot_alternatives_vs_base_profile(A, B_row, T)
```

Plots alternatives as lines and one base profile with ranges of indifference, preference and veto. 



**Args:**
 
 - <b>`A`</b> (DataFrame):  Performance matrix of alternatives (rows) for criteria (columns). 


 - <b>`B_row`</b> (DataFrame):  One Base profile. 


 - <b>`T`</b> (DataFrame):  Indifference (q), preference (p) and veto (v) thresholds for each criterion (columns). 



**Returns:**
 None. 

Example 
------- 

```python
plot_alternatives_vs_base_profile(A, B.iloc[0], T)
```



---

## <kbd>function</kbd> `plot_base_profiles_vs_alternative`

```python
plot_base_profiles_vs_alternative(B, A_row, T)
```

Plots base profiles as lines and one alternative with ranges of indifference, preference and veto. 



**Args:**
 
 - <b>`B`</b> (DataFrame):  Base profiles in ascending order for criteria (columns). 


 - <b>`A_row`</b> (DataFrame):  One alternative from the performance matrix. 


 - <b>`T`</b> (DataFrame):  Indifference (q), preference (p) and veto (v) thresholds for each criterion (columns). 



**Returns:**
 None. 

Example 
------- 

```python
plot_base_profiles_vs_alternative(B, A.iloc[0], T)
```



---

## <kbd>function</kbd> `main`

```python
main()
```








---

_This file was generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
