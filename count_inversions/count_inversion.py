# Counting the number of inversions in an array

class inversions(object):

    def __init__(self, arr):
        self.arr = arr
    
    def count_inversions(self):
        array , total_inversions = self.sort_count(self.arr, len(self.arr))
        return total_inversions

    def sort_count(self, arr, arr_len):
        
        if arr_len == 1:    # base case: return array when there is only one element
            return arr, 0
        sub_arr_len = arr_len // 2
        left_arr = arr[0 : sub_arr_len]
        right_arr = arr[sub_arr_len :]
        sort_left_arr, x = self.sort_count(left_arr , len(left_arr))
        sort_right_arr, y = self.sort_count(right_arr , len(right_arr))
        sort_arr, z = self.merge_count_split_inv(sort_left_arr, sort_right_arr)
        return sort_arr, x+y+z

    def merge_count_split_inv(self, A, B):
        i = 0; j = 0; split_inv_count = 0
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

            if A[i] <= B[j]:
                sort_arr.append(A[i])
                i+=1
            else:
                sort_arr.append(B[j])
                j+=1
                split_inv_count += (len(A) -i)

        return sort_arr, split_inv_count



if __name__ == "__main__":


    with open("integers.txt") as f:     # open a integer list file 
        x= [int(y) for y in f.read().splitlines()]

    # x = [1,6,3,2,4,5] #input the array here
    algo = inversions(x)
    inv_count = algo.count_inversions()
    print("Number of inversions is {} \n".format(inv_count))




