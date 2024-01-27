#Nested Traversal Approach
#O(n^2) Time |  O(1) Space
def twoNumberSum(array , targetSum):
  
  arrays = list(array) #now converting set to list or you can use tupple convert the unordered set to an ordered list first. Only then you use indexing or slicing so the error doesn’t occur anymore
  for i in range(len(array) - 1 ):
        firstNum = arrays[i] #now using list arrays To fix the TypeError: 'set' object is not subscriptable, either convert the unordered set to an ordered list or tuple before accessing it or get rid of the indexing or slicing call altogether.
        for j in range(i + 1, len(array)):
            secondNum = arrays[j] #now here secondNum variable can acess arays list element because it become in ordered list from unordered set which is array initialize out of def twoNumberSum and after called in parameter to pass array element.
            if firstNum + secondNum == targetSum :
                return [firstNum,secondNum]
  return []


array = {4 , 5, 5 , 7 , 3, 2 , 8, 6} #this is a set 
targetSum = 10 
    

print('so the the two number equal to target are:')
num = twoNumberSum(array , targetSum)
print (num)

