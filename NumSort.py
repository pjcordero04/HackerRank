#sort the number in odd index in decreasesing order
#then sort the number in even index in increasing order

def Solution(nums):
    odd_index = []
    even_index = []
    sort_merged = []
    for i in range(len(nums)):
        if(i%2==0):
            even_index.append(nums[i])
        else:
            odd_index.append(nums[i])
    even_index.sort()
    odd_index.sort(reverse=True)
    print(even_index)
    print(odd_index)
    for i in range(len(nums)):
        if(i%2==0):
            sort_merged.append(even_index[int(i/2)])
        else:
            sort_merged.append(odd_index[int((i-1)/2)])
    print(sort_merged)
    return sort_merged

nums = [8,4,1,2,3,5,7]
Solution(nums)
