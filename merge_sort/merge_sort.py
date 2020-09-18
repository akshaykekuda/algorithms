# Implementing Merge Sort
import math

class merge_sort(object):

    def divide_sort(self, arr, arr_len):
        
        if arr_len <2:    # base case: return array when there is only one element
            return arr
        sub_arr_len = arr_len // 2
        left_arr = arr[0 : sub_arr_len]
        right_arr = arr[sub_arr_len :]
        sort_left_arr = self.divide_sort(left_arr , len(left_arr))
        sort_right_arr = self.divide_sort(right_arr , len(right_arr))
        return self.merge(sort_left_arr, sort_right_arr)

    def merge(self, A, B):
        i = 0; j = 0
        n = len(A) + len(B)
        sort_arr = []
        for k in range(n):
            if i == len(A): # when you reach end of array A, append remaining elements of array B
                sort_arr.append(B[j])
                j += 1
                continue
            if j == len(B): # when you reach end of array B, append remaining elements of array A
                sort_arr.append(A[i])
                i += 1
                continue

            if A[i] < B[j]:
                sort_arr.append(A[i])
                i+=1
            else:
                sort_arr.append(B[j])
                j+=1

        return sort_arr



if __name__ == "__main__":

    x = [2, 4, 6, 8, 2, 4 , 6, 8] #input the array here
    algo = merge_sort()
    sorted_x = algo.divide_sort(x, len(x))
    print("Sorted array is {} \n".format(sorted_x))




