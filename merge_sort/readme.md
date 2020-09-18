# Merge Sort using Divide and Conquer

The algo consits of two parts:
1. Divide_sort: Divides a n element array into n/2 element array (left_arr and right_arr) and sorts the n/2 length arrays (sort_left_arr, sort_right_arr) recursively
2. merge: Merges to sorted arrays A and B

T(n) = 2T(n/2) + O(n)
