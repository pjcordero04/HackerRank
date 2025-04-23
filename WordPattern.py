def Solution(pattern,s):
    pattern_list = list(pattern)
    s_list = s.split()
    my_dict = dict(zip(pattern_list,s_list))
    print(pattern)
    print(s)
    print(my_dict)
    matched = 0
    if(len(pattern_list)==len(s_list)):
        for i in range(len(pattern_list)):
            if(my_dict[pattern_list[i]]==s_list[i]):
                matched += 1
        if(matched == len(pattern_list)):
            return True
    return False
pattern = 'banana'
s = 'ball ark nail ark nail ark'
print(Solution(pattern,s))