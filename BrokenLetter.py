#count the number of words that are valid after removing the characters in the brokenKeys

def Solution(text, brokenKeys):
    bk = list(brokenKeys)
    words = text.split()
    count = sum(1 for word in words if not any(char in bk for char in word.lower()))

    return count

text = "Hello World"
brokenKeys = "ad"

print(Solution(text,brokenKeys))
            