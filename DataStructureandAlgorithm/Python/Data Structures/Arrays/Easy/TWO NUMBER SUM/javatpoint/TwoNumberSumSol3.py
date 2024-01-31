#Approach - 3: Using Two Pointers
#In this approach, we will use the (binary search algorithm)
# where the given list array must be sorted. We need to
# fix the first index and then the required value to fulfill the
# target found in the list.
#We will use the two pointers: left and right; 
# the left denotes the first element, and the right denotes the last element of the list.
# Then we compare the sum of the pointer's value to the target value;
# if some of the value and target is equal, return the pointers index pairs.
# If the sum of value is more than the target, we decrement the right pointer. 
# Otherwise, some of the value is less than the target; we need to increase the 
# left pointer by one and check the same conditions.
#Time Complexity using Two Sum :-
#   The time complexity will be O(n) even in the worst case, we visit all the elements in the array only once.
#Space complexity :-0(1)
# Only constant space for the variable is used.
#Using the dictionary, it takes only one for loop so that the time complexity will be the O(n).
class Solution:  
    def twoSum(self, list1, target):  
        left = 0  
        right = len(list1) - 1  
          
        temSum = 0  
          
        while (left<right):  
            tempSum = list1[left] + list1[right]  
            if tempSum == target:  
                return list((left, right))  
            elif tempSum>target:  
                right -= 1  
            elif tempSum<target:  
                left += 1  
                  
        return list((-1, -1))  
           
list1 = [2, 7, 11, 15]      
target = 26  
obj = Solution()  
print(obj.twoSum(list1, target))  
#Output:[2, 3] 0.037sec