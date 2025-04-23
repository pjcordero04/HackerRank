def CharSwap(s1,s2):
    if(s1==s2):
        return True
    if(len(s1)==len(s2)):
        diff = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff.append(s1[i])
        if(len(diff)>2):
            return False
        return True
    return False

s1 = "LOVE"
s2 = "LOVE"
print(CharSwap(s1,s2))

print(s1)