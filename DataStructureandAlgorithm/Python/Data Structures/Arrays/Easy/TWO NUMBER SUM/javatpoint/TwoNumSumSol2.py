#Approach -2: Using Dictionary
#In this approach,
# we created the TwoSum class, and inside it, we declare the solution() method.
# In this method, we declared a dictionary to keep track of all the values
# seen so far in the value to the index. Now, we iterate the given list using 
# the enumerated. Then, we subtract the num value from the target value to
# search its pair. If the pair is found, return the index of both numbers.
# Otherwise, add it to our dictionary for a future visit.
#Using the dictionary, it takes only one for loop so the time complexity will be the O(N).
class Solution:  
    def twoSum(self, nums, target):  
        #declaring a dictionary to keep track of all the values   
        visited_numbers = dict()  
          
        # iterating over the entire array  
        for index, num in enumerate(nums):  
              
            #subtracting the num from the target to search for its pair  
            number_to_be_search = target - num  
              
            #if the pair is found, return the index of the both numbers  
            if number_to_be_search in visited_numbers:  
                return [index, visited_numbers[number_to_be_search]]  
            #otherwise we simply add it to out dictionary for future lookup  
            else:  
                visited_numbers[num] = index  
       
list1 = [2, 7, 11, 15]      
target = 18  
obj = Solution()  
print(obj.twoSum(list1, target))  
#output [2 ,1] 0.042 sec