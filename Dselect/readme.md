# Deterministic Selection Algorithm

Goal: Given an array A of length n, find the i-th order statistic using Deterministic Pivot Selection

The pivot selected here is the median of medians of array A

Pseudo Code:

```
Dselect(A, n, i):
    if n = 1 return A[1]
    Divide A into sorted sub arrays of length 5(or <5 in the case of n %5 = {1,2,3,4})
    C = median of the sorted sub arrays
    p = Dselect(C, n/5, n/10)   #recursively compute the median of C
    Partition A around p
    j = new index of p
    if j = i : return p
    if j > i : 
        return Dselect(1st part of A, j-1, i)
    else:
        return Dselect(2nd part of A, n-j, i-j)
```

Average running Time: O(n)
