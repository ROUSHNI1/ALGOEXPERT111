def twoNumberSum(array , targetSum):
  for i in range(len(array) - 1 ):
        firstNum = array[i]
        for j in range(i + 1, len(array)):
            secondNum = array[j]
            if firstNum + secondNum == targetSum :
                return [firstNum,secondNum]
  return []

def main():
    array = {4 , 5, 5 , 7 , 3, 2 , 8, 6}
    targetSum = 10 
    print('so the the two number equal to target are:')
    print(twoNumberSum(array , targetSum))
if __name__=="__main__":
         main()