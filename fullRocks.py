def maxBag(capacity,rocks,additionalRocks):
    need = []
    num_bag = 0
    for i in range(len(capacity)):
        if(capacity[i]-rocks[i] == 0):
            num_bag += 1
        else:
            need.append(capacity[i]-rocks[i])
    need.sort(reverse=False)
    i = 0
    while additionalRocks >= need[i]:
        additionalRocks-=need[i]
        i+=1
        num_bag += 1
    return num_bag

capacity = [7,7,7,7]
rocks = [7,5,4,3]
additionalRocks = 6

print(maxBag(capacity,rocks,additionalRocks))
