#Approach - 1: Brute Force Approach
#The brute force approach is a commonly used way to solve the problem.
# In this approach, our primary goal is to solve the problem, not efficiently. 
# We check every possible pair and the number of possible pairs in the array.
# We will use the two for loop, add the two values, and compare the target value. 
# If it is equal to the target value, return the indices of pairs of the integer.
#algorithm :-
#   Run the first loop to point the first index of the solution in the array.
#   Run another loop to point a second index of the solution for every first integer.
#   If the both elements equal to the target value, return the both indices values
class TwoSum:  
    def __init__(self, list1, target):  
        self.list1 = list1  
        self.target = target  
          
    def solution(self):  
        length = len(list1)  
          
        for i in range(length-1):  
            for j in range(i+1, length):  
                if list1[i]+list1[j] == self.target:  
                    new_list = i, j  
                    return list(new_list)  
        return -1  
  
list1 = [1, 2, 4, 5, 11]  
target = 6  
obj = TwoSum(list1, target)  
print(obj.solution())  
#solution [0,3] 0.038sec
# Explanation -

# In the above program, 
# we have created the TwoSum class and initialized the two variables
# list1 and target. Then, we declare the solution() method where first
# we checked the length of the list and applied two for loops. 
# The first for loop is to maintain the first index, 
# and the second for loop is to maintain the second index. 
# We checked the sum of both values; if it is true;
# we assigned a new list and returned the indices of the elements.
#Time Complexity of Two Number Sums (Brute Force Approach) :-
#
#   We need to use the two for loops.
# The first for loop visits n numbers 
# of elements and second for loop visits n-1. 
# Hence, the check for the possible and total 
# number of pair are: N*(N-1)/2, 
# the time-complexity will be O(N*N) = N2.
# Space Complexity
#0(1): Only constant space for variable is used.