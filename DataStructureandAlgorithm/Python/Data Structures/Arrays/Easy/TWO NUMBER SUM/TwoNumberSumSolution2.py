#O(n) Time | O(1) Space
def twoNumberSumSolution2(array , targetSum):
    nums = {}
    for num in array:
        potentialMatch = targetSum - num
        if potentialMatch in nums:
            return[potentialMatch , num]
        else:
            nums[num] = True
    return []

array = {3, 5, -4, 8, 11, 1, -1, 6}
targetSum = 10
print('so the the two number equal to target are:/n')
print(twoNumberSumSolution2(array, targetSum))