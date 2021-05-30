class Merge: # here making a Merge class with the help of class keyword
    # code for merge and sorting two halves
    count=0
    def sort(self, num, L, R): # this is the sort function which will sort all the left and right subarray or list  here def is used to define a method
        i = j = k = 0
        while i < len(L) and j < len(R): # using while loop until the length of i and j is less than then length of left and right sub array
            if L[i] < R[j]: # now checking the condition if the ith element of sub array L (L[i]) is smaller than the jth element of the sub array R (R[j])
                num[k] = L[i]  # here assign the L[i] value to the kth index of the user array.
                i += 1 #increment the i
            else: # if the above condition will failed then this code inside the else statement will run
                num[k] = R[j] # here assign the R[j] value to the kth index of the user array.
                j += 1 #increment the j
            k += 1 #increment the k

        # now checking for the left elements either in L or R
        while i < len(L): # if still some elements are in LEFT array then it will added to the user array(modifed)
            num[k] = L[i]
            i += 1
            k += 1
        while j < len(R):# if still some elements are in RIGHT array then it will added to the user array(modifed)
            num[k] = R[j]
            j += 1
            k += 1
        return num # AT LAST RETURNING THE ARRAY WHICH WAS INPUT BY THE USER BUT NOW THE SAME ARRAY IS SORTED IN ASCENDING ORDER


    # this the merge_sort function which will split the array into small sub arrays and after that it will sort all the arrays one by one and combine them

    def merge_sort(self,num):
            # first checking the elements in the list
            if len(num)>1: # the elements should be greater then 1 to sort the array
                #first we will find the mid of the array
                mid=len(num)//2
                #now splitting the array into two temporary array
                L=num[:mid] # left sub array
                # print(L)
                R = num[mid:] # right subArray
                # print(R)
               #here we are recursively calling the merge_sort function till the two subarrays or sublist breaks into smallest
                self.merge_sort(L) # this is your first half
                self.merge_sort(R) # second half
                return self.sort(num,L,R) # here calling the sort method which will sort the two subarrays or sublist one by one
            else:
                return num # if the length of user array is less than 1 then it will return the array as list


if __name__ == '__main__': # this the main method which is invoked  automatically  while you will first run your program
    print("Enter Your Numbers In a Line ( Seprated by space):") # print
    num=list(map(int,input().strip().split())) # here we are taking input from the user
    # we are using several methods here qhich are as follows :-
    #1. map() :-returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.)
    #2.input() : taking input
    #3.strip() :- removes any leading (spaces at the beginning) and trailing (spaces at the end) characters (space is the default leading character to remove)
    #4.split()  :-  splits a string into a list.
    obj=Merge() # creating a object (obj) of class Merge
    print(obj.merge_sort(num)) # here printing the output return by the merge_sort() which is a method of class Merge
