
def count_overlapping_substrings(string, substring):
        count = start = 0
        while start < len(string):
            start = string.find(substring, start)  # Find next occurrence starting from 'start'
            if start == -1:
                break
            count += 1
            start += 1  # Move the start index forward to allow overlapping
        return count

def minion_game(string):
    # your code goes here
    string = string.upper()
    vowels = ['A','E','I','O','U']
    kevinSet = set()
    stuartSet = set()
    S_score = 0
    K_score = 0
    
    #"Take all the possible substrings for Kevin"
    for i in range(len(string)):
        if(string[i] in vowels):
            for j in range (len(string),i,-1):
                kevinSet.add(string[i:j])
                print(kevinSet)

    for i in range(len(string)):
        if(string[i] not in vowels):
            for j in range (len(string),i,-1):
                stuartSet.add(string[i:j])
                print(stuartSet)

    

    for element in kevinSet:
        K_score += count_overlapping_substrings(string, element)
        #print("word: ", element, "  word_count:", count_overlapping_substrings(string, element))
    print(K_score)

    for element in stuartSet:
        S_score += count_overlapping_substrings(string, element)
        #print("word: ", element, "  word_count:", count_overlapping_substrings(string, element))
    print(S_score)
    if(K_score>S_score):
        print("Kevin",K_score)
    elif(K_score<S_score):
        print("Stuart", S_score)
    else:
        print("Draw")

minion_game('banana')