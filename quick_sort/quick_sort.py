# Implementing quick Sort

class sort:

    def __init__(self, arr, pivot_type):
        self.arr = arr
        self.pivot_type = pivot_type


    def quick_sort(self, low, high):

        if high - low < 2  :    # base case: return array when there is only one element or no element
            return

        pivot_dict = {  0: self.pivot_low(low, high),
                        1: self.pivot_high(low, high),
                        2: self.pivot_median(low, high)
                     }    

        pivot = pivot_dict.get(self.pivot_type)
        self.arr[low] , self.arr[pivot] = self.arr[pivot] , self.arr[low] #get pivot element to the start of the array        
        part_idx = self.partition_arr(low, low, high)
        self.quick_sort(low, part_idx)
        self.quick_sort(part_idx+1, high)

    
    def median3_sort(self, median_arr):

        if len(median_arr) == 1 :    # base case: return array when there is only one element or no element
            return median_arr

        elif len(median_arr) ==2:   

            if median_arr[0] > median_arr[1]:
                median_arr[0], median_arr[1] = median_arr[1], median_arr[0]
            return median_arr
        
        else:
            if median_arr[0] > median_arr[1]:
                median_arr[0], median_arr[1] = median_arr[1], median_arr[0]
            if median_arr[1] > median_arr[2]:
                median_arr[1], median_arr[2] = median_arr[2], median_arr[1]
            if median_arr[0] > median_arr[1]:
                median_arr[0], median_arr[1] = median_arr[1], median_arr[0]

            return median_arr

    def partition_arr(self, pivot, low, high):
        self.comp_count += (high - low) -1
        i = low + 1
        for j in range(low + 1, high):
            if self.arr[j] <= self.arr[pivot]:
                self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
                i += 1
        
        
        self.arr[low], self.arr[i -1] = self.arr[i-1] , self.arr[low]
        return i - 1 

    def pivot_high(self, low, high):

        return high -1 #pivot is the last element of the array

    def pivot_low(self, low, high):

        return low #pivot is the first element of the array
    
    def pivot_median(self, low, high):
        if (high - low) < 3:
            return low 
        #if the length of the array is odd, median is evident, if length if the array is 2k, median is at k
        middle = low + ((high -1 - low) // 2)   
        sub_arr = [self.arr[low], self.arr[middle], self.arr[high -1]]
        sub_arr = self.median3_sort(sub_arr)
        median = sub_arr[1]
        return self.arr.index(median)

if __name__ == "__main__":

    while True:
        pivot_type = input("How do you want the pivot to be calculated:\n\
        0: First element of the array is the pivot\n\
        1: Last element of the array is the pivot\n\
        2: Median of the array is the pivot\n")

        if pivot_type =='0' or pivot_type=='1' or pivot_type=='2':
            break
        else:
            print("Invalid Input! Try again")

    # x = [4,2,3] #input the array here

    with open("QuickSort_numbers.txt") as f:     # open a integer list file 
        x= [int(y) for y in f.read().splitlines()]   

    algo = sort(x, int(pivot_type))
    algo.comp_count = 0    
    algo.quick_sort(0, len(x))
    print("sorted array: {}".format(algo.arr))
    print("No. of comparisons is {} \n".format(algo.comp_count))
