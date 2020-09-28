# Finding the i-th order statistic using randomised pivot selection
import random

class Array:

    def __init__(self, arr):
        self.arr = arr


    def Rselect(self, low, high, i):

        if high - low < 2  :    # base case: return array when there is only one element or no element
            return self.arr[low]

        pivot = self.get_pivot(low, high)
        self.arr[low] , self.arr[pivot] = self.arr[pivot] , self.arr[low] #get pivot element to the start of the array        
        j = self.partition_arr(low, high)
        if j == (i):
        	return self.arr[j]
        if j  > (i):
        	return self.Rselect(low, j, i)
        else:
        	return self.Rselect(j+1, high, i)


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
    	return random.choice(list(range(low,high)))


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
    i_ststic = array.Rselect(0, len(x), int(i) -1)
    print("\n{}-th order statistic of the array is: {}".format(i, i_ststic))
    print("No. of comparisons is {} \n".format(array.comp_count))

