# Counting the number of inversions in an aray

Counting the number of inversions in an array is an important application for collaboartive filtering.
Indices (i, j) of an array is called as an inversion if A[i] > A[j], for i < j

Input: An array A of length x
Output: number of inversions 

## Pseudo-code:
```
sort_count(arr, arr_len):

    if arr_len == 1 :return 0
    sorted_left_arr, x = sort_count(arr[0 : arr_len /2], arr_len /2)
    sorted_right_arr, y = sort_count(arr[arr_len /2: ], arr_len /2)
    z = count_split_inversion(sorted_left_arr, sorted_right_arr)
    return x++y+z
    
count_split_inversion(A,B):
    sort_arr = []
    for k = 1:len(A+B)
        if A[i] <= B[j]:
            sort_arr.append(A[i])
            i+=1
        else:
            sort_arr.append(B[j])
            j+=1
            split_inv_count += (len(A) -i)
     return sort_arr, split_inv_count
```
