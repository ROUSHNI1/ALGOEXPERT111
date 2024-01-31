"geeks of geeks code"
# This python program tells if there exists a pair in array whose sum results in x.
 
# Function to find and print pair
#NESTED TRAVERSAL APPROACH  
#time complexity = O(n^2)  space complexity = O(1)    0.049sec    output = yes

 
def chkPair(A, size, x):
    for i in range(0, size - 1):
        for j in range(i + 1, size):
            if (A[i] + A[j] == x):
                return 1
    return 0
 
 
if __name__ == "__main__":
    A = [0, -1, 2, -3, 1]
    x = -2
    size = len(A)
 
    if (chkPair(A, size, x)):
        print("NESTED TRAVERSAL APPROACH = Yes")
 
    else:
        print("NESTED TRAVERSAL APPROACH = No")

#---------------------------------------------------------------------------------------------------------------------------------
#2nd Approach
#Using Sorting and Two-Pointers technique:
## Python program to check for the sum
# condition to be satisfied
"""Time Complexity: O(NlogN), Time complexity for sorting the array
Auxiliary Space: O(1)  output = yes   0.044sec"""

 
def hasArrayTwoCandidates(A, arr_size, sum):
 
    # sort the array
    quickSort(A, 0, arr_size-1)
    l = 0
    r = arr_size-1
 
    # traverse the array for the two elements
    while l < r:
        if (A[l] + A[r] == sum):
            return 1
        elif (A[l] + A[r] < sum):
            l += 1
        else:
            r -= 1
    return 0
 
# Implementation of Quick Sort
# A[] --> Array to be sorted
# si  --> Starting index
# ei  --> Ending index
 
 
def quickSort(A, si, ei):
    if si < ei:
        pi = partition(A, si, ei)
        quickSort(A, si, pi-1)
        quickSort(A, pi + 1, ei)
 
# Utility function for partitioning
# the array(used in quick sort)
 
 
def partition(A, si, ei):
    x = A[ei]
    i = (si-1)
    for j in range(si, ei):
        if A[j] <= x:
            i += 1
 
            # This operation is used to swap
            # two variables is python
            A[i], A[j] = A[j], A[i]
 
        A[i + 1], A[ei] = A[ei], A[i + 1]
 
    return i + 1
 
 
# Driver program to test the functions
A = [1, 4, 45, 6, 10, -8]
n = 16
if (hasArrayTwoCandidates(A, len(A), n)):
    print(" Using Sorting and Two-Pointers technique = Yes")
else:
    print("Using Sorting and Two-Pointers technique = No")

#----------------------------------------------------------------------------------------------------------------------------------
#3rd Approach    
#Two Sum using Binary Search:
# Python program to check for the sum
# condition to be satisfied
# Time Complexity: O(NlogN)  Auxiliary Space: O(1)  Output = yes
 
def binarySearch(A, low, high, searchKey):
    m = 0
    while (low <= high):
        m = (high + low) // 2
        # Check if searchKey is present at mid
        if (A[m] == searchKey):
            return 1
        # If searchKey greater, ignore left half
        if (A[m] < searchKey):
            low = m + 1
        # If searchKey is smaller, ignore right half
        else:
            high = m - 1
    # if we reach here, then element was
    # not present
    return 0
 
 
def checkTwoSum(A, arr_size, sum):
 
    # sort the array
    A.sort()
    l = 0
    r = arr_size-1
 
    #  Traversing all element in an array search for searchKey
    i = 0
    while i < arr_size-1:
        searchKey = sum-A[i]
        # calling binarySearch function
        if(binarySearch(A, i+1, r, searchKey) == 1):
            return 1
        i = i+1
 
    return 0
 
 
# Driver program to test the functions
A = [1, 4, 45, 6, 10, -8]
n = 14
if (checkTwoSum(A, len(A), n)):
    print(" using Binary Search technique = Yes")
else:
    print(" using Binary Search technique = No") 

#---------------------------------------------------------------------------------------------------------------
#4th Approach
#Two Sum using Hashing:
# Python program to check for the sum
# condition to be satisfied
#Time Complexity: O(N), As the whole array is needed to be traversed only once.
#Auxiliary Space: O(N), A hash map has been used to store array elements.   output = yes
 
def binarySearch(A, low, high, searchKey):
    m = 0
    while (low <= high):
        m = (high + low) // 2
        # Check if searchKey is present at mid
        if (A[m] == searchKey):
            return 1
        # If searchKey greater, ignore left half
        if (A[m] < searchKey):
            low = m + 1
        # If searchKey is smaller, ignore right half
        else:
            high = m - 1
    # if we reach here, then element was
    # not present
    return 0
 
 
def checkTwoSum(A, arr_size, sum):
 
    # sort the array
    A.sort()
    l = 0
    r = arr_size-1
 
    #  Traversing all element in an array search for searchKey
    i = 0
    while i < arr_size-1:
        searchKey = sum-A[i]
        # calling binarySearch function
        if(binarySearch(A, i+1, r, searchKey) == 1):
            return 1
        i = i+1
 
    return 0
 
 
# Driver program to test the functions
A = [1, 4, 45, 6, 10, -8]
n = 14
if (checkTwoSum(A, len(A), n)):
    print("using Hashing technique = Yes")
else:
    print("using Hashing technique = No")    
    
    