#You're given an integer array arr. You can choose a set of integers and remove all 
# the occurences of these integers in the array.
#Return the minimum size of the set so that at least half of the integers of the array are
#removed

from collections import defaultdict
def Solution(arr:list):
    nums = set(x for x in arr)
    matched = defaultdict(int)
    counter = 0
    arr_size = len(arr)
    print('Array size:', arr_size)
    #count the number of each occurences
    for num in nums:
        matched[num] = arr.count(num)

    print(matched)
    matched = dict(sorted(matched.items(), key=lambda x: x[1], reverse=True))
    print('sorted: ',matched)
    for key in matched:
        arr_size -= matched[key]
        counter+=1
        if(arr_size<=(len(arr)/2)):
            break
    return counter

arr = [3,3,3,1,5,5,5,2,2,7,8,9,10,11,12,13,14,15] 
print(Solution(arr))


#from chat-GPT

from collections import Counter

def minSetSize(arr):
    freq = Counter(arr)
    sorted_freq = sorted(freq.values(), reverse=True)

    removed = 0
    set_size = 0
    half = len(arr) // 2

    for count in sorted_freq:
        removed += count
        set_size += 1
        if removed >= half:
            break

    return set_size