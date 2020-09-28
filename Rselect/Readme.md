# Randmomized Selection Algorithm

Goal: Given an array A of length n, find the ith order statistic using Random Pivot Selection

Pseudo Code:

```
Rselect(A, n, i):
    if n = 1 return A[1]
    chose pivot p at random from A
    Partition A around p
    j = new index of p
    if j = i : return p
    if j > i : 
        return Rselect(1st part of A, j-1, i)
    else:
        return Rselect(2nd part of A, n-j, i-j)
```

Average running Time: O(n)
