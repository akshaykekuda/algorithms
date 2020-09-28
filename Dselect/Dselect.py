# Finding the i-th order statistic using randomised pivot selection
import random

class Array:

    def __init__(self, arr):
        self.arr = arr


    def Dselect(self, low, high, i):

        if high - low < 2  :    # base case: return array when there is only one element or no element
            return self.arr[low]

        C = []

        if (high - low) % 5:
        	sort_arr_less_five = self.merge_sort(self.arr[low: high], (high -low )% 5)
        	C.append(sort_arr_less_five[((high -low -1) % 5) // 2])

        else:
        	for five in range(low, high - high %5, 5):
        		sort_arr_five = self.merge_sort(self.arr[five : five + 5], 5)
        		C.append(sort_arr_five[2])
        
        median_arr = Array(C)
        median_arr.comp_count = 0
        pivot = median_arr.Dselect(0, len(C), len(C) //10)
        pivot_index = self.arr.index(pivot)
        
        self.arr[low] , self.arr[pivot_index] = self.arr[pivot_index] , self.arr[low] #get pivot element to the start of the array        
        j = self.partition_arr(low, high)
        if j == (i):
        	return self.arr[j]
        if j  > (i):
        	return self.Dselect(low, j, i)
        else:
        	return self.Dselect(j+1, high, i)


    def partition_arr(self, low, high):
        self.comp_count += (high - low) -1
        i = low + 1
        for j in range(low + 1, high):
            if self.arr[j] <= self.arr[low]: #pivot in first index
                self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
                i += 1
        self.arr[low], self.arr[i -1] = self.arr[i-1] , self.arr[low]
        return i - 1 

    def get_pivot(self, low, high):
    	# return low
    	return random.choice(list(range(low,high)))

    
    def merge_sort(self, arr, arr_len):
        
        if arr_len == 1:    # base case: return array when there is only one element
            return arr
        sub_arr_len = arr_len // 2
        left_arr = arr[0 : sub_arr_len]
        right_arr = arr[sub_arr_len :]
        sort_left_arr = self.merge_sort(left_arr , len(left_arr))
        sort_right_arr = self.merge_sort(right_arr , len(right_arr))
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

    x = list(range(1, 100))
    random.shuffle(x)
    i = random.choice(x)

    #with open("QuickSort_numbers.txt") as f:     # open a integer list file 
    #   x= [int(y) for y in f.read().splitlines()]

    while False:
        i = input("Enter the i-th order statistic to compute\n")

        if 0< int(i) <= len(x):
            break
        else:
            print("Invalid Input! i-th order statistic exceeds input array length Try again")
  

    array = Array(x)
    array.comp_count = 0
    i_ststic = array.Dselect(0, len(x), int(i) -1)
    print("\n\n Array: \n{}\n\n\nThe {}-th order statistic of the array is: {}".format(x, i, i_ststic))
    print("No. of comparisons is {} \n".format(array.comp_count))

