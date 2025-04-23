'''
def Solution(nums):
    counter = 0
    nums.sort(reverse = False)
    while max(nums)>0:
        for num in nums:
            if num!=0:
                x = num
                break
        #print(nums)
        #print(x)
        for i in range(len(nums)):
            if(nums[i]>0 or nums[i]-x >= 0):
                nums[i]-=x
        counter+=1
        #print('counter: ', counter)
    return counter
 '''

#NumPy solution is 5x faster than the first solution
import numpy as np

'''def Solution(nums):
    nums = np.array(nums)
    counter = 0
    while np.any(nums > 0):
        # Get the minimum non-zero value
        min_non_zero = np.min(nums[nums > 0])
        
        # Subtract it from all elements greater than 0
        nums[nums > 0] -= min_non_zero
        counter += 1
    return counter
'''

#this is the fastest. The number of iterations is just the number of unique numbers minus the number of zeros
def Solution(nums):
    return len(set(nums) - {0})
# Example
nums = [1, 5, 0, 3, 5]
print(Solution(nums))  


